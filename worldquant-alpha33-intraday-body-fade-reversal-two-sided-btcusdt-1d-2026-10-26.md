---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: WorldQuant Alpha33 intraday-body fade reversal two-sided on BTCUSDT 1d bars
created: 2026-10-26
updated: 2026-10-26
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

# WorldQuant Alpha33 intraday-body fade reversal two-sided on BTCUSDT 1d bars

## Provenance

Primary sources read end to end during this cycle (2026-10-26), pinned:

- Paper (fresh fetch this cycle, 22 pages / 47,293 chars extracted, 244,416 bytes, sha256 `1f9c21afe32dcb3ee77b31548acdaea00451fbfa1c0ee10c907867bcc736fce9`, byte-identical to the admitted sibling records' bytes): `Zura Kakushadze`, `101 Formulaic Alphas`, arXiv `1601.00991` (manuscript dated `December 9, 2015` — record `source_as_of` is that manuscript date, never a fetch date; the paper states the formulas `are also computer code` once the operators are defined). Alpha#33 prints in Appendix A as `rank((-1 * ((1 - (open / close))^1))`. Operator pins from the paper's own §A.1 Functions and Operators: `abs(x), log(x), sign(x) = standard definitions`, same for `+ - * / > < ==`; `rank(x) = cross-sectional rank`; inputs (A.2) `open, close, high, low, volume = standard definitions for daily price and volume data`. Timing pin from §2: `delay-1 means that the alpha is traded on the day subsequent to the date of the most recent data used in computing it` (e.g. traded today `starting at the open`); footnote 11 names exactly four delay-0 alphas (`42, 48, 53 and 54`, `assumed to be traded at or as close as possible to the close of the trading day for which they are computed`) — Alpha#33 is not among them, so it is delay-1 by the paper's own exclusion. Direction pins from §2: the taxonomy sentence `A mean-reversion alpha has a sign opposite to the return on which it is based`, with the worked mean-reversion example `−ln(today's open / yesterday's close)` (positive exactly on a down-move, i.e. positive-score→long is a fade); and the Alpha#101 worked example (`if the stock runs up intraday (i.e., close > open and high > low), the next day one takes a long position` — a positive score maps to long, a negative score to short; see Negative evidence 1 for the exact strength of this pin).
- Audited pinned implementation (fetched live this cycle, verified byte-identical to the siblings' pinned audit bytes, sha256 `b54a820ca35fc06359f023cb590015ff4d4cd818c077322d587dc4e9cbf70316`): repository `https://github.com/OctopusTakopi/toraniko-alpha101`, head commit `4fc0627d2a720fd8d583708ef051b9d48d98aacd` (confirmed still the repository head via the GitHub commits API this cycle), exact file `toraniko/alpha101.py`: `def alpha033` returns `rank(self.open / self.close - 1)` (lines 373–374 — identical to the printed formula since `^1` is the identity and `open/close - 1 = -(1 - open/close)`); `def rank` is the cross-sectional percentile rank (lines 70–72). Alpha#33 needs no `delay`/`delta`, no `ts_rank`, no `scale`, no `IndNeutralize`, no `vwap`, no `adv`, no `returns`, no market-cap, no volume, and no threshold of any kind: the sole division is by `close`, which is strictly positive on every valid bar, so the inner value is always finite for finite inputs — no NaN branch exists anywhere in this formula.

Licence and rights: the paper is a public arXiv preprint; the implementation is public research software. This record cites and normalizes the rule (single-line formula and operator definitions only for gate evidence) and reproduces no source block beyond single-line facts.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the paper. The paper prints the Alpha#33 formula, the operator/input definitions, the delay-1 timing class, and the mean-reversion fade polarity, but ships no venue, no symbol, no single-asset side mapping (its own evaluation is cross-sectional), no order/fill semantics beyond the delay-1 open class, no warmup seed, and no risk leg. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` Binance USDT-M perpetual `1d` (the paper is daily U.S. equities with no venue — frame/venue pin disclosed, never a source claim; perpetual is the minimal realistic venue because the short leg needs margin); (2) completed-bar decisions with next-bar-open market fills (the paper's delay-1 class trades `on the day subsequent to the date of the most recent data`, `starting at the open` — deviation class identical to the admitted caporale-plastun, ehlers-cg, worldquant-alpha6/7/9/12/21/23/24/26/28/46/101 records' bar-port, disclosed, never an advantage claim); (3) the cross-sectional `rank` layer reduced to the inner value's zero-split for direction plus an adopted 5-completed-bar warmup with pre-warmup bars flat by record rule (structural minimum is the 1st completed bar — single-bar construction with zero delay/delta calls — plus margin per the admitted worldquant-alpha101 precedent; the rank wrapper is strictly increasing in the inner value, so the fade polarity survives the reduction, but the relative-order→absolute-split step itself is a researcher pin, fenced in Negative evidence 1 — never a source claim); (4) house sizing/costs with modeled funding while held (the paper ships no sizing, capital, fee, or slippage concept — never presented as source-native behavior). The open/close inner value, the `^1` identity, the fade polarity (long down-days, short up-days), the delay-1 next-day execution, the reversal-or-flatten exits, and the no-stop/no-target risk posture are source-grounded and unmodified.

Pre-write dedup (2026-10-26): working-tree case-insensitive searches for `alpha33`, `alpha_33`, `alpha-33`, `alpha#33`, and `alpha 33` return zero strategy records; the thirteen sibling `worldquant-alpha*` records (6, 7, 9, 12, 21, 23, 24, 26, 28, 46, 53, 54, 101) use different formulas (nearest neighbours fenced in Negative evidence 6). Open `research/*` PRs are #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), #251 (Swift 2-year MA multiplier zone-state long-flat), #304 (forven CCI oversold-recross long-flat), #331 (freqtrade AdxSmas ADX-gated SMA cross long-flat), #350 (freqtrade ClucMay72018 BB-discount EMA-gated long-flat), and #353 (freqtrade Heracles Keltner-Donchian band-ratio state long-flat) — different mechanisms, indicators, and sources. This is the fourteenth WorldQuant-101 record in the pool family, not a parameter variant of any admitted rule.

## Economic mechanism

### Source-reported

Coarse mean-reversion/momentum building blocks. The paper frames its universe coarsely: `one can think of alpha signals as based on mean-reversion or momentum`, where `a mean-reversion alpha has a sign opposite to the return on which it is based`, exemplified by `−ln(today's open / yesterday's close)`. Alpha#33 is a single delay-1 mean-reversion block in one line: the inner value `open/close − 1 = −(close − open)/close` is the negation of the bar's open-to-close return (up to the close divisor), so a positive score sits exactly on a down-day print and a negative score on an up-day print. The paper ships no behavioural, structural, or risk-premium mechanism beyond this measurement construction, and no stop, target, or risk leg of any kind.

### Research interpretation

Single-bar intraday-body fade book, two-sided, threshold-free. Every defined bar's inner sign trades on the next open: down-day bars (close below open) fire long, up-day bars fire short — the paper's own mean-reversion polarity, carried over exactly. Unlike sibling worldquant-alpha101 (the body-to-range ratio traded as momentum continuation — this rule takes the OPPOSITE side on every non-doji bar; verified structurally in-cycle, see Evidence), unlike sibling worldquant-alpha12 (a volume-change-signed 1-day close product — this rule never reads volume), unlike sibling worldquant-alpha9 (a 5-bar delta-sign streak ternary — this rule has no window and no streak), unlike pool double-seven-connors (a 7-day close-pullback object — never an open-anchored single-bar fade), unlike pool forven-gap-fill (an overnight-gap object — this rule reads the intraday body, never the overnight gap), unlike pool caporale-plastun (band-gated abnormal-return breakouts — never a raw body sign). The failure mode is plain: a steadily trending tape prints same-sign bodies day after day and pins the book against the trend with no scaling and no guardrail, while doji-neighbourhood bars flip the book on microstructure dust at the worst prints — disclosed, not upgraded.

## Signal

Exact rule as pinned (any other series, divisor, exponent, negation, fill, frame, book, or tie treatment is a different, unpinned rule):

- Inputs (paper A.2): `open[t]`, `close[t]` on completed `1d` bars. No `high`, no `low`, no `volume`, no vwap/adv/returns/market-cap/sector, no cross-sectional rank, no second asset or timeframe is read by any order-gating line.
- Inner value (paper Appendix A, pinned impl lines 373–374): `inner[t] = open[t] / close[t] − 1 = −(1 − open[t]/close[t])` — same-bar construction, `^1` identity applied exactly. The divisor `close[t]` is strictly positive on every valid bar, so the inner value is always finite for finite inputs; `inner[t] == 0` prints exactly when `open[t] == close[t]` (doji bar). Never seeded, never backfilled.
- Direction mapping (source-grounded, fenced in Negative evidence 1): `inner[t] > 0` → long signal (down-day fade); `inner[t] < 0` → short signal (up-day fade); `inner[t] == 0` → flat signal (exact-zero doji print — deterministic flat, never a held conviction). The entry fills at the next bar's open, one single unit, only if the book does not already carry that side (see position rule).
- Exit: the first opposite signal reverses the full unit in one step (close plus opposite entry at the same next-bar-open fill); a zero print flattens the full unit at the next open — reversal-or-flatten is the sole exit path by construction. No stop-loss, no take-profit, no trailing, no time exit (the paper ships no risk leg — carried over exactly, disclosed in Provenance adaptation (4), never upgraded into a source claim).
- Direction: two-sided (both signs are routinely attainable — up-days and down-days both print; verified structurally in-cycle). Shorts are native to USDT-M margin (no uptick rule, no borrow desk).
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further long-signal bars as no-ops (no pyramiding, no averaging), and symmetrically for shorts; flat-regime bars while already flat are no-ops. Re-entry re-arms on the next opposite or flat-exit signal only (no cooldown specified — explicitly none, not invented). Pre-first-signal bars are flat.

## Required data

- Completed `1d` bars of BTCUSDT: `open` and `close` only (the inner value's two inputs). No `high`/`low`/`volume`, no funding-signal, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar-table, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (no multi-timeframe call, no cross-sectional ranking — one asset, one frame; the inner value reads the same single bar, never a second feed).
- Warmup: 5 completed `1d` bars flat by record rule — structural minimum is the 1st completed bar (single-bar construction with zero delay/delta calls, each value needing 1 completed bar — pinned by code absence), plus margin per the admitted worldquant-alpha101 precedent. Pre-warmup bars are flat by record rule; missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (inner value reads completed bars only), no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance USDT-M perpetual under the house overlay (researcher choice — the paper names no venue and evaluates U.S. equities; no source-market equivalence is claimed; perpetual is the minimal realistic venue because the short leg needs margin).
- Order timing (paper-grounded derivation): completed-bar decision with next-bar-open market fills for entries, reversals, and flat-exits — the paper's delay-1 class trades `on the day subsequent to the date of the most recent data`, `starting at the open`, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) on the same verified primitive as the admitted caporale-plastun, ehlers-cg, and worldquant-alpha6/7/9/12/21/23/24/26/28/46/101 records' entries (verified this cycle's base). This record claims no other fill convention: no perfect-open print, no maker-touch, no intrabar-path-dependent fill.
- Stop/limit modeling: none — the derived spec carries zero stop/limit/trailing orders by record rule. No hidden Hummingbot stop-order defaults are relied upon, and with no stop/limit legs there is no same-bar TP/SL ordering ambiguity.
- Sizing/capital/costs: the paper ships no sizing, capital, fee, or slippage concept. The explicit house overlay (single-unit frame, pinned house taker fees both legs, modeled funding while held) applies to the derived evaluation here, never presented as source-native behavior. Funding is never zero-claimed: two-sided holds span the `00:00`/`08:00`/`16:00 UTC` funding stamps, so every held bar carries modeled funding.
- Concurrency: at most one single-asset engine position at any time; an opposite signal closes-and-reverses in one step and a zero signal closes-to-flat. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic, no hedge-mode requirement by construction.

## Evidence

### Source-reported

With exact provenance (fresh arXiv PDF bytes this cycle, read end to end): the `are also computer code` formula status; the Alpha#33 line `rank((-1 * ((1 - (open / close))^1))`; the A.1 operator definitions (standard arithmetic, `rank(x) = cross-sectional rank`); the A.2 input definitions (`open, close, high, low, volume = standard definitions for daily price and volume data`); the §2 delay-1 definition and the footnote-11 delay-0 exclusion list (`42, 48, 53 and 54` — Alpha#33 absent, hence delay-1); the §2 mixed building-block framing with the mean-reversion opposite-sign sentence and the `−ln(today's open / yesterday's close)` worked fade example; the §2 Alpha#101 direction sentence itself (`runs up intraday ... the next day one takes a long position`). With exact implementation provenance (pinned commit `4fc0627d`, file `toraniko/alpha101.py` lines 70–72 and 373–374, head re-confirmed via the commits API and byte-identical to the siblings' audit bytes this cycle): the executable `rank(open/close − 1)` semantics and the cross-sectional percentile rank. This record claims no source-reported performance number of any kind — no return, no win rate, no trade count, no per-alpha table figure is carried into the derived specification — and no reproduced performance exists.

### Independently reproduced

Not independently reproduced. Logic-only scratch self-check this cycle (`SELF-CHECK OK`): down-day→long / up-day→short / exact-doji→flat polarity; always-defined on extreme positive prints; `open/close − 1` identical to `−(1 − open/close)` on 10k random prints; 300-bar book simulation with two injected exact dojis showing strict enter/reverse/flat alternation with same-side no-ops (3 enters, 146 reversals, 2 flats); fade side exactly opposite the Alpha#101 continuation side on every non-doji bar. Pure rule verification, never a backtest.

### Negative evidence

1. Direction words fenced, admitted plainly: the paper never prints `buy`, `sell`, `long`, or `short` for Alpha#33. The fade polarity rests on the §2 mean-reversion taxonomy (`a mean-reversion alpha has a sign opposite to the return on which it is based`) together with the paper's own worked fade example (`−ln(today's open / yesterday's close)`, positive on a down-move) and the §2 Alpha#101 sign convention (positive score→long). The relative-order→absolute-zero-split step (cross-sectional rank reduced to the inner value's sign about zero) is a predeclared researcher pin, not a paper sentence — without it the single-asset side would be ambiguous, so it is pinned here rather than left to the reviewer. A reviewer must not graft any other direction convention onto this record.
2. Timeframe and venue fenced: the paper is daily U.S. equities and names no venue. `1d` BTCUSDT-perpetual is the disclosed researcher pin (Provenance adaptation (1)); a reviewer must not cite the paper as evidence for any frame or venue.
3. Risk silence fenced: the paper contains no stop, target, trailing, time exit, or risk paragraph for Alpha#33 — the no-guardrail posture is carried over exactly, never upgraded, never presented as a tested safety choice.
4. Cross-sectional machinery fenced: the paper's own evaluation ranks scores across thousands of stocks. Alpha#33's formula contains no `IndNeutralize`, no `scale(`, no `vwap`, no `adv`, no `returns`, and no sector/industry term — the single-asset sign map drops the cross-sectional rank-order layer entirely, disclosed as adaptation (3), never presented as the paper's traded portfolio.
5. Exact-zero determinism fenced: `inner[t] == 0` requires the computed `open[t]/close[t] − 1` to print exactly `0.0` (true doji prints; near-doji bars keep their dust-side — disclosed, not buffered). The flat treatment is a predeclared record rule, not a paper sentence.
6. Overlap fences, admitted plainly: sibling `worldquant-alpha101` trades the same two inputs as momentum continuation (takes the opposite side on every non-doji bar — different direction, different normalization, different guard); sibling `worldquant-alpha12` trades a volume-change-signed close product (reads volume, never the open-anchored body); sibling `worldquant-alpha9` trades a 5-bar delta-sign streak ternary (a history-purity object — never a single-bar sign); sibling `worldquant-alpha53` trades a 9-bar change of a close-location ratio at delay-0 same-close (different object, different timing); pool `double-seven-connors` trades 7-day close pullbacks (never an open-anchored body); pool `forven-gap-fill` trades overnight gaps (never the intraday body); pool `turnaround-tuesday` gates weekday bars on SMA/RSI/ATR (a gated calendar object — never a raw body sign); pool `1-3-1-red-green-candle-reversal` trades 1h streaks with fixed-RR exits (different frame, different exits); pool `caporale-plastun` gates abnormal-return breakouts on trailing bands (different event, different frame). Shared `open`/`close`/`intraday`/`reversal` vocabulary is not shared signal.
7. No hidden variants admitted: any other series, divisor, exponent, negation, threshold, stop/target/filter/cooldown, frame, fill, venue, or book is a different, unpinned rule. A reviewer must not pick among these to rescue or reshape the record.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `open/close − 1` / exact-zero flat / two-sided / delay-1 next-open fills / no-stop posture / `1d` BTCUSDT perpetual are frozen.

- F1 — Fade-direction relevance: a continuation twin (long on positive inner, short on negative inner — same formula, grid, fills, and reversal book) must not improve net expectancy; fail ⇒ the paper's mean-reversion fade polarity adds nothing over continuing the body's direction on this market.
- F2 — Open-anchor relevance: a close-to-close fade twin (sign of `−(close[t] − close[t−1])/close[t−1]` — same book, grid, fills, with a 6-bar adopted warmup) must not improve net expectancy; fail ⇒ the open anchor adds nothing over fading the plain daily close-change on this market.
- F3 — Horizon relevance: a two-bar persistence twin (trade only when two consecutive bars print the same inner sign, holding the first bar's signal through the confirmation bar — same construction, grid, fills) must not improve net expectancy; fail ⇒ the single-bar horizon adds nothing over the confirmed two-bar version, and the record is a horizon label rather than a horizon edge.

## Crypto portability

Pinned to BTCUSDT Binance USDT-M perpetual under the house overlay (declared port of a venue-free daily-equity formula). The rule reads completed daily bars only, so no pit-session, gap, roll, split/dividend-adjustment, or corporate-action logic ports (the paper's split/dividend close adjustment touches only delay-0 open-anchored alphas — a non-issue for this single-bar delay-1 score on crypto, disclosed, not modeled). The score is scale-free (a return-like ratio whose side alone trades) yet body-size behaviour differs across venues — the OHLC read is the kline print as-is with no normalization to invent. The rule is two-sided, so a spot-only deployment expresses only long-firing bars while short-firing bars stay venue-gated (never silently converted) — a spot-only variant would be a different, unpinned claim. No warmup history beyond 5 `1d` bars is consumed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- No price stop, no time stop: adverse excursion after a noise-fired single-bar signal has no guardrail before the opposite signal, by the carried-over paper design — the record's principal risk.
- Doji-dust whipsaw exposure: when closes print near opens, the book flips long-short on microstructure dust at the worst prints of each swing — the paper provides no buffer band and this record invents none.
- Persistent-regime pin risk: a steadily trending tape prints same-sign bodies for extended stretches and pins the book against the trend with no scaling — the raw-sign construction cuts both ways, disclosed.
- Exact-zero note: the flat branch fires only on exact-doji bars — rare on BTCUSDT, so the book is effectively always-in-market, disclosed.
- Single-venue port residual: paper-regime U.S. equities vs Binance perpetual execution (prints, fees, funding, range-definition, margin mechanics beyond the house model) is unclaimed, disclosed.
- Rank-reduction residual: the cross-sectional rank-order layer is replaced by an absolute zero-split — the fade polarity is source-grounded but the split point is a researcher pin, disclosed.
- Performance evidence is absent: nothing here is calibrated, fitted, or tuned to any backtest.
- Author scope: the paper presents production formulaic alphas as research objects, not a vetted retail trading system — this record is research-only and claims no live suitability.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior and never part of this admission — no Safety-Order/DCA event is admitted in this record's version. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Kakushadze, Z., `101 Formulaic Alphas`, arXiv:1601.00991 (manuscript December 9, 2015 — Alpha#33 formula, A.1 operator/input definitions, §2 delay-1 definition with footnote-11 delay-0 exclusion, §2 mean-reversion taxonomy with worked fade example and Alpha#101 direction sentence — fresh PDF bytes read end to end 2026-10-26, sha256 `1f9c21afe32dcb3ee77b31548acdaea00451fbfa1c0ee10c907867bcc736fce9`): https://arxiv.org/abs/1601.00991
- Same paper, PDF (formula appendix, operator/input definitions, empirical sections — read 2026-10-26): https://arxiv.org/pdf/1601.00991
- OctopusTakopi `toraniko-alpha101` (independent audited implementation — `alpha033` at `toraniko/alpha101.py` lines 373–374, `rank` at lines 70–72 — pinned to commit `4fc0627d2a720fd8d583708ef051b9d48d98aacd`, head re-confirmed via the GitHub commits API and byte-identical to the siblings' audit bytes 2026-10-26): https://github.com/OctopusTakopi/toraniko-alpha101
