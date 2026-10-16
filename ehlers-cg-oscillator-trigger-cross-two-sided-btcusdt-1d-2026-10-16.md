---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Ehlers Center of Gravity oscillator trigger-cross two-sided on BTCUSDT 1d bars
created: 2026-10-16
updated: 2026-10-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2002-05-01
sources:
  - https://mesasoftware.com/papers/TheCGOscillator.pdf
  - https://ta-lib.org/functions/cg.html
  - https://traders.com/Documentation/FEEDbk_docs/2002/08/TradersTips/TradersTips.html
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Ehlers Center of Gravity oscillator trigger-cross two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end during this cycle (2026-10-16), pinned:

- Author manuscript (fetched live this cycle, 46938 bytes, SHA-256 `bb80a787ff9786e07d26d8c58e40f6674541d2561d158d2229495fd70cfff9d7`, 4 PDF pages, read end to end): `John Ehlers`, `The CG Oscillator`, author's PDF of the article published as `The Center Of Gravity Oscillator`, `Technical Analysis of Stocks & Commodities, May 2002` (record `source_as_of` is that issue month, never the fetch date). The paper prints the full EasyLanguage listing (Figure 1), the trigger construction, and the crossover-signal reading — every order-gating line below traces to a printed line (see Signal).
- Independent formula corroboration (read this cycle): TA-Lib `CG — Center of Gravity Oscillator` reference, which documents the identical balance-point ratio, the `(H+L)/2` median-price input convention, the default period, and Ehlers' own trading usage: `Ehlers reads turning points from it and trades its crossings with a copy of itself delayed by one bar`.
- Third-party implementation census (read this cycle, fenced — never adopted): `Traders' Tips — August 2002` (traders.com) collects vendor implementations of the May-2002 article, including a 3%-profit-target trading system and a 5-bar-SMA signal-line variant. Both are third-party additions, quoted here only to fence them out (see Negative evidence 4–5).

Licence and rights: the author's manuscript is publicly distributed from his own site. This record cites and normalizes the rule (short quoted declarations only for gate evidence) and reproduces no source block beyond single-line facts.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the paper. The paper prints the oscillator formula, the `Length = 10` worked example, the `(H+L)/2` price input, the one-bar-delayed trigger, and the crossover-signal reading, but ships no venue, no timeframe stamp, no order/fill semantics, no warmup seed, and no risk leg. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` Binance USDT-M perpetual `1d` (the paper's example chart carries no timeframe stamp and no venue — frame/venue pin disclosed, never a source claim; perpetual is the minimal realistic venue because the short leg needs margin); (2) completed-bar crossover decisions with next-bar-open market fills (the paper evaluates per bar with no fill convention — deviation class identical to the admitted caporale-plastun record's bar-port, disclosed, never an advantage claim); (3) an 11-completed-bar warmup with pre-warmup bars flat by record rule (the paper seeds nothing — covers the 10-bar window plus the two lagged CG reads the first cross needs; see Required data); (4) house sizing/costs with modeled funding while held (the paper ships no sizing, capital, fee, or slippage concept — never presented as source-native behavior). The `(H+L)/2` input, `Length = 10`, the `−Num/Denom` ratio, the `CG[1]` trigger, the crossover-signal reading, the in-phase direction mapping, the reversal-only exits, and the no-stop/no-target risk posture are source-grounded and unmodified.

Pre-write dedup (2026-10-16): working-tree case-insensitive searches for `center of gravity`, `cg oscillator`, `cg trigger`, `CGOscillator`, `mesasoftware`, `balance point`, and `balance-point` return zero strategy records using this source, author article, or formula — the single `Center Of Gravity` hit anywhere is fencing prose inside the bandpass record's own dedup census (a searched term, never an order-gating line). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Closest pool records are different Ehlers constructions: `cyber-cycle-signal-self-cross-loss-escape` (highpass-filtered cycle recursion with a 9-lag smoothed signal line, deliberate inversion, and an openprofit loss-escape flat leg), `ehlers-decycler-oscillator-cross` (decycler smoothing-ratio oscillator), `bandpass-filter-reversed-cycle-sign` (cosine-derived resonator sign state), `ehlers-sinewave-phase-cross-flip` (Hilbert sine/lead phase cross), `ehlers-trendflex-fast-slow-cross` (TrendFlex fast/slow cross), and `fisher-zero-cross` (Fisher-warped zero-sign latch — a level reference, never a trigger cross). No pool record computes the `−Σ(1+k)·price/Σprice` balance-point ratio or trades its crossings against its own one-bar-delayed copy. This is a new family, not a parameter variant.

## Economic mechanism

### Source-reported

Near-zero-lag balance-point turning-point detection: substituting window prices for weights on a ruler, the window's center of gravity `moves to the right when prices increase sharply` and `to the left when prices decrease`; `measured as the distance from the most recent price, the CG decreased when prices rose and increased when they fell`, so Ehlers writes `all I had to do was to invert the sign of the CG to get a smoothed oscillator that was both in phase with the price swings and had essentially zero lag`. Because `the CG is smoothed, an effective crossover signal is produced simply by delaying the CG by one bar`, and `every major price turning point is identified by the CG Oscillator and the crossovers formed by its trigger with zero lag`. The paper ships no behavioural, structural, or risk-premium mechanism beyond this measurement claim, and no stop, target, or risk leg of any kind.

### Research interpretation

Balance-point reversal, two-sided trigger-cross. Unlike the CyberCycle record (which filters price through a highpass recursion and crosses a 9-lag smoothed signal with an inversion plus a loss-escape flat), the signal here performs no filtering at all: it weighs each of the last 10 median prices by its age-rank, reads where the mass sits, and fires only when that balance point crosses its own prior-bar print — entries therefore trigger on the rotation of price-mass inside the window, not on any level, band, or smoothed-average cross. Unlike the Fisher record (zero-sign latch on a Gaussianized warp, always-in), the reference is self-relative: a flat market parks CG and trigger together and prints nothing, so the book rests between rotations rather than carrying a permanent conviction. Unlike every band-breakout record (Bollinger/STARC/EHMA/Keltner — level rails with multi-bar holds), there is no rail anywhere; the trigger breathes with the oscillator itself. The failure mode is made plain: the paper's own length discussion admits a too-short window turns the oscillator `a little too nervous for profitable trading`, and with no guardrail leg a whipsaw rotation reverses the full unit straight into the opposite side — the trigger cross is the entire risk control, disclosed, not upgraded.

## Signal

Exact rule as pinned (any other length, price input, trigger lag, fill, frame, book, or tie treatment is a different, unpinned rule):

- Price input (source Figure 1): `price[t] = (high[t] + low[t]) / 2` on completed `1d` bars. `Length = 10` (the paper's printed input default and worked example — see Negative evidence 7).
- Oscillator (source Figure 1, verbatim arithmetic): `Num[t] = Σ(k=0..9) (1+k)·price[t−k]`; `Den[t] = Σ(k=0..9) price[t−k]`; `CG[t] = −Num[t]/Den[t]` under the source guard `If Denom <> 0` (retained as a dead-branch convention: crypto median prices are strictly positive so `Den[t] > 0` on every live bar; a `Den = 0` bar would hold the prior `CG` per the EasyLanguage persistence in the listing — disclosed convention, never reachable on live tape).
- Trigger (source Figure 1, `Plot2(CG[1])`): `Trig[t] = CG[t−1]` — the oscillator delayed by exactly one bar. No smoothing, no average, no second parameter (third-party smoothed-trigger variants are fenced in Negative evidence 5).
- Cross events (completed-bar evaluation, strict with prior-bar equality admitted — total and mutually exclusive): `crossUp[t] = (CG[t−1] ≤ Trig[t−1]) and (CG[t] > Trig[t])`; `crossDown[t] = (CG[t−1] ≥ Trig[t−1]) and (CG[t] < Trig[t])`. An exact-equality bar (`CG[t] = Trig[t]`) prints no event and holds the book. Both predicates can never fire on the same bar.
- Direction mapping (source-grounded, fenced in Negative evidence 1): the paper's inverted CG is `in phase with the price swings`, and Ehlers `trades its crossings with a copy of itself delayed by one bar` — so `crossUp` (oscillator turning up through its trigger) → long signal; `crossDown` (turning down through its trigger) → short signal. The entry fills at the next bar's open, one single unit, only if the book does not already carry that side (see position rule).
- Exit to the opposite side: the first opposite cross reverses the full unit in one step (close plus opposite entry at the same next-bar-open fill) — reversal is the sole exit path by construction. No stop-loss, no take-profit, no trailing, no time exit (the paper ships no risk leg — carried over exactly, disclosed in Provenance adaptation (4), never upgraded into a source claim).
- Direction: two-sided (long leg and short leg are both native). Shorts are native to USDT-M margin (no uptick rule, no borrow desk).
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further `crossUp` prints as no-ops (no pyramiding, no averaging), and symmetrically for shorts. Re-entry re-arms on the next opposite cross only (no cooldown specified — explicitly none, not invented). Pre-first-event bars are flat.

## Required data

- Completed `1d` bars of BTCUSDT: `high`/`low` only (via the median input). No `open`, no `close`, no `volume`, no funding-signal, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar-table, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (no multi-timeframe call, no cross-sectional ranking — one asset, one frame; the trigger is a one-bar self-delay, never a second feed).
- Warmup: 11 completed `1d` bars — the 10-bar window is only full from the 10th bar and the first cross additionally reads `CG[t−2]`, so the first evaluable event bar is the 11th completed bar. Pre-warmup bars are flat by record rule; missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (window and trigger read completed bars only), no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance USDT-M perpetual under the house overlay (researcher choice — the paper names no venue; no source-market equivalence is claimed; perpetual is the minimal realistic venue because the short leg needs margin).
- Order timing (predeclared derivation): completed-bar decision with next-bar-open market fills for both entries and reversals — compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) on the same verified primitive as the admitted caporale-plastun record's entries (verified this cycle's base). This record claims no other fill convention: no perfect-trigger-touch fill, no maker-touch, no intrabar-path-dependent fill.
- Stop/limit modeling: none — the derived spec carries zero stop/limit/trailing orders by record rule. No hidden Hummingbot stop-order defaults are relied upon.
- Sizing/capital/costs: the paper ships no sizing, capital, fee, or slippage concept. The explicit house overlay (single-unit frame, pinned house taker fees both legs, modeled funding while held) applies to the derived evaluation here, never presented as source-native behavior. Funding is never zero-claimed: two-sided holds span the `00:00`/`08:00`/`16:00 UTC` funding stamps, so every held bar carries modeled funding.
- Concurrency: at most one single-asset engine position at any time; an opposite cross closes-and-reverses in one step. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic, no hedge-mode requirement by construction.

## Evidence

### Source-reported

With exact provenance (author manuscript of the S&C May-2002 article, read end to end this cycle): the ruler/balance-point analogy and directional statement (CG right on sharp rises, left on falls); the sign inversion producing the in-phase zero-lag oscillator; the Figure 1 EasyLanguage listing (`Price((H+L)/2)`, `Length(10)`, the `(1+count)`-weighted numerator, the unweighted denominator, `CG = -Num/Denom`, `Plot1(CG)`, `Plot2(CG[1])`); the trigger sentence (`an effective crossover signal is produced simply by delaying the CG by one bar`); the turning-point claim (`every major price turning point is identified by the CG Oscillator and the crossovers formed by its trigger with zero lag`, Figure 2); the length-selection guidance (ideal length half the dominant cycle; too-long desensitizes, too-short turns nervous). The paper ships zero performance numbers — no return, no win rate, no trade count, no sample period table — and this record claims no source-reported performance of any kind. The TA-Lib reference independently corroborates the formula, the median-price input, the default period, and the trade-the-delayed-copy usage.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Direction words fenced, admitted plainly: the paper never prints `buy`, `sell`, `long`, or `short`. The up-cross→long / down-cross→short mapping rests on two printed facts — the inverted oscillator is `in phase with the price swings` (rises with price) and Ehlers `trades its crossings with a copy of itself delayed by one bar` (TA-Lib's reading of his usage) — not on any order verb in the manuscript. A reviewer must not graft any other direction convention onto this record.
2. Timeframe and venue fenced: the manuscript's example chart carries no timeframe stamp and names no market or venue. `1d` BTCUSDT-perpetual is the disclosed researcher pin (Provenance adaptation (1)); a reviewer must not cite the paper as evidence for any frame or venue.
3. Risk silence fenced: the manuscript contains no stop, target, trailing, time exit, or risk paragraph of any kind — the no-guardrail posture is carried over exactly, never upgraded, never presented as a tested safety choice.
4. Third-party system fenced: the Traders' Tips August-2002 collection builds a CG trading system with a 3% profit-target exit (plus a cross-back exit). That target is a vendor addition, never Ehlers' text — not adopted here; adopting it would be a different, unpinned rule.
5. Smoothed-trigger variants fenced: the same Tips collection smooths CG with a 5-bar moving-average signal line (NeoTicker) and eSignal/NeuroShell ports add their own trigger treatments. This record uses only the author's `CG[1]` — every smoothed trigger is a different, unpinned rule.
6. Book-recentering immateriality fenced: Ehlers' 2004 book form adds `(N+1)/2` to recenter the oscillator around zero (TA-Lib notes). Adding the same constant to both CG and its one-bar trigger preserves every cross event bit-for-bit — the recentering is therefore event-neutral to this record and is neither adopted nor needed as a separate claim.
7. Length guidance fenced: the paper recommends half the dominant cycle and works the `Length = 10` example; it prints no BTC-tuned length. `10` stands on the printed example alone — retuning the window for any market or cycle estimate would be a different, unpinned rule.
8. Overlap fences, admitted plainly: pool `cyber-cycle-signal-self-cross-loss-escape` smooths `hl2`, recurses a highpass cycle with `alpha = 0.07`, crosses a 9-lag smoothed signal with a deliberate inversion, and escapes on openprofit loss (filtered-cycle signal plus loss flat — never a balance-point ratio, never a one-bar self-delay); pool `fisher-zero-cross` latches the sign of a Fisher-warped position readout against the fixed zero reference (level reference, never a trigger cross); pool `bandpass/decycler/sinewave/trendflex` records cross filtered-cycle constructions with their own estimators (different formulas, different triggers, different sources). Shared `Ehlers`/`cross`/`signal` vocabulary is not shared signal.
9. No hidden variants admitted: any other length, any other price input, any smoothed trigger, any zero-reference, any stop/target/filter/cooldown, any other frame, fill, venue, or book is a different, unpinned rule. A reviewer must not pick among these to rescue or reshape the record.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `(H+L)/2` / `Length = 10` / `−Num/Denom` ratio / `CG[1]` trigger / strict cross with prior-bar equality / two-sided / next-open fills / no-stop posture / `1d` BTCUSDT perpetual are frozen.

- F1 — Direction-mapping relevance: a fade twin (short on `crossUp`, long on `crossDown` — same oscillator, trigger, grid, fills, and reversal book) must not improve net expectancy; fail ⇒ the paper's in-phase mapping adds nothing over fading the trigger cross on this market.
- F2 — Trigger relevance: a trigger-free twin (hold long while `CG[t] > CG[t−1]`, hold short while `CG[t] < CG[t−1]`, flat only pre-first-print — the raw first-difference state on the identical oscillator) must not improve net expectancy; fail ⇒ the one-bar-delayed trigger adds nothing over trading the oscillator's own bar-to-bar turn, and the paper's whipsaw-smoothing claim does no work here.
- F3 — Weighting relevance: a triangular-average twin (10-bar WMA slope-sign state with the same one-bar-lagged trigger construction — same window, same cross mechanics, plain age-rank averaging instead of the price-weighted balance-point ratio) must not reproduce-or-beat net expectancy; fail ⇒ the balance-point weighting adds nothing over an ordinary weighted-average slope and the record is a label variant of a WMA-slope cross.

## Crypto portability

Pinned to BTCUSDT Binance USDT-M perpetual under the house overlay (declared port of a venue-free oscillator study). The rule reads completed daily bars only, so no pit-session, gap, roll, or corporate-action logic ports. The oscillator is scale-free (a ratio of price-weighted sums — percent-level portability with no price-level recalibration), yet 24/7 crypto's volatility clustering vs the paper's original market regime is unclaimed and undisguised (see Negative evidence). The rule is two-sided, so a spot-only deployment expresses only long-firing bars while short-firing bars stay venue-gated (never silently converted) — a spot-only variant would be a different, unpinned claim. No warmup history beyond 11 `1d` bars is consumed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- No price stop, no time stop: adverse excursion after a trigger cross has no guardrail before the opposite cross, by the carried-over paper design — the record's principal risk, sharpened by the paper's own warning that short windows turn nervous.
- Whipsaw rotation exposure: in a sideways market CG and its one-bar trigger can alternate crosses on consecutive bars, printing long-short reversal pairs with no structural filter — the paper provides none beyond smoothing and this record invents none.
- Trigger-lag cost: the trigger is the oscillator itself delayed a bar, so every signal is confirmed one bar after the rotation begins — the paper's `zero lag` describes the oscillator, not the cross; the cross always pays the confirmation bar plus the next-open fill.
- Single-venue port residual: the author's market vs Binance perpetual execution (prints, fees, funding, margin mechanics beyond the house model) is unclaimed, disclosed.
- Performance evidence is absent: the manuscript reports no numbers at all; nothing here is calibrated, fitted, or tuned to any backtest.
- Author scope: the paper presents a measurement oscillator with a signal reading, not a vetted trading system — this record is research-only and claims no live suitability.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior and never part of this admission — no Safety-Order/DCA event is admitted in this record's version. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Ehlers, John, `The CG Oscillator` (author manuscript of `The Center Of Gravity Oscillator`, Technical Analysis of Stocks & Commodities, May 2002 — formula, Figure 1 listing with `Price((H+L)/2)` / `Length(10)` / `CG = -Num/Denom` / `Plot2(CG[1])`, trigger sentence, turning-point claim, length guidance — read end to end via live fetch 2026-10-16): https://mesasoftware.com/papers/TheCGOscillator.pdf
- TA-Lib `CG — Center of Gravity Oscillator` reference (independent formula/usage corroboration: balance-point ratio, median-price input, default period, trade-the-one-bar-delayed-copy — read 2026-10-16): https://ta-lib.org/functions/cg.html
- Traders' Tips, Technical Analysis of Stocks & Commodities, August 2002 (third-party CG implementations census — 3%-target system and smoothed-trigger variants, fenced as not adopted, read 2026-10-16): https://traders.com/Documentation/FEEDbk_docs/2002/08/TradersTips/TradersTips.html
