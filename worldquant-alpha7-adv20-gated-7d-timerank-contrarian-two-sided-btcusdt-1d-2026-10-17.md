---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: WorldQuant Alpha7 adv20-gated 7-day time-rank contrarian two-sided on BTCUSDT 1d bars
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

# WorldQuant Alpha7 adv20-gated 7-day time-rank contrarian two-sided on BTCUSDT 1d bars

## Provenance

Primary sources read end to end during this cycle (2026-10-17), pinned:

- Paper (live-fetch arXiv PDF this cycle, 22 pages / 47,293 chars extracted, sha256 `1f9c21afe32dcb3ee77b31548acdaea00451fbfa1c0ee10c907867bcc736fce9`): `Zura Kakushadze`, `101 Formulaic Alphas`, arXiv `1601.00991` (manuscript dated `December 9, 2015` — record `source_as_of` is that manuscript date, never a fetch date; the paper states the formulas `are also computer code` once the operators are defined). Alpha#7 prints in Appendix A across two lines as `((adv20 < volume) ? ((-1 * ts_rank(abs(delta(close, 7)), 60)) * sign(delta(close, 7))) : (-1 * 1))`. Operator pins from the paper's own definitions section: `abs(x), log(x), sign(x) = standard definitions` (same for `+ - * / > <`); `delay(x, d) = value of x d days ago`; `delta(x, d) = today's value of x minus the value of x d days ago`; `ts_rank(x, d) = time-series rank in the past d days`; non-integer lookbacks convert to `floor(d)` (all Alpha#7 windows are integers, so no flooring is exercised); inputs `open, close, high, low, volume = standard definitions for daily price and volume data`, `adv{d} = average daily dollar volume for the past d days` (dollar definition fenced in Negative evidence 5). Timing pin from §2: `delay-1 means that the alpha is traded on the day subsequent to the date of the most recent data used in computing it` (e.g. traded today `starting at the open`); footnote 11 names exactly four delay-0 alphas (`42, 48, 53 and 54`, traded at or as close as possible to the close of the computed day) — Alpha#7 is not among them, so it is delay-1 by the paper's own exclusion. Direction pin from the §2 worked example: `Alpha#101 ... is a delay-1 momentum alpha: if the stock runs up intraday (i.e., close > open and high > low), the next day one takes a long position` — a positive score maps to long, a negative score to short (see Negative evidence 1); the paper's own taxonomy adds that `a mean-reversion alpha has a sign opposite to the return on which it is based`, which is exactly the gate-pass leg's construction here.
- Audited pinned implementation (fetched live this cycle): repository `https://github.com/OctopusTakopi/toraniko-alpha101`, head commit `4fc0627d2a720fd8d583708ef051b9d48d98aacd` (confirmed still the repository head via the GitHub commits API this cycle), exact file `toraniko/alpha101.py`: `def alpha007` returns `_if_else(adv20 < self.volume, -ts_rank(np.abs(change), 60) * np.sign(change), -1.0, adv20, self.volume)` with `change = delta(self.close, 7)` and `adv20 = self._adv(20)` (lines 262–265); `def _adv` is `sma(self.volume, window)` (lines 235–236); `def _window` floors fractional lookbacks (lines 42–44); `def _rank_1d` assigns tie-averaged ordinal ranks `1..n` divided by `n` (lines 47–67), so every defined time-rank sits in `(0, 1]` and is strictly positive; `def delay` emits the value shifted by the lookback and `def delta` is `x - delay(x, period)` (lines 74–82, first rows undefined by construction); `_rolling` emits undefined values before the window is full and requires an all-finite block (lines 85–93); `def ts_rank` normalizes like cross-sectional rank over the trailing window (lines 154–157); `def correlation` is the full-window trailing Pearson with undefined values before the window is full and a defined zero-variance window reading as zero (lines 120–135, not exercised by this formula beyond precedent); `_if_else` preserves undefined condition inputs as NaN (lines 192–199). Alpha#7 needs no floor, no cross-sectional rank, no scale, no vwap, no cap, no IndNeutralize, and no zero-division branch of its own: after the trailing windows exist every input is finite and the only exact-zero print is the zero-change flat.

Licence and rights: the paper is a public arXiv preprint; the implementation is public research software. This record cites and normalizes the rule (single-line formula and operator definitions only for gate evidence) and reproduces no source block beyond single-line facts.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the paper. The paper prints the Alpha#7 formula, the operator/input definitions, the delay-1 timing class, and the positive-score→long convention, but ships no venue, no symbol, no single-asset side mapping (its own evaluation is cross-sectional), no order/fill semantics beyond the delay-1 open class, no warmup seed, and no risk leg. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` Binance USDT-M perpetual `1d` (the paper is daily U.S. equities with no venue — frame/venue pin disclosed, never a source claim; perpetual is the minimal realistic venue because the short leg needs margin); (2) completed-bar decisions with next-bar-open market fills (the paper trades delay-1 `on the day subsequent to the date of the most recent data`, `starting at the open` — deviation class identical to the admitted caporale-plastun, ehlers-cg, and worldquant-alpha6/alpha12/alpha101 records' bar-port, disclosed, never an advantage claim); (3) an adopted 72-completed-bar warmup with pre-warmup bars flat by record rule (structural minimum is the 67th completed bar — the 7-day change needs 8 bars and the 60-bar time-rank over finite changes needs 59 more, while the 20-bar average needs 20 bars — plus margin per the admitted worldquant-alpha6 precedent; see Required data); (4) house sizing/costs with modeled funding while held (the paper ships no sizing, capital, fee, or slippage concept — never presented as source-native behavior). The `adv20 < volume` gate, the `-ts_rank(abs(delta(close,7)),60) * sign(delta(close,7))` contrarian leg, the `-1.0` short-default leg, the strict-`<` equality treatment, the exact-zero flat tie, the delay-1 next-day execution, the positive→long / negative→short mapping, the reversal-or-flatten exits, and the no-stop/no-target risk posture are source-grounded and unmodified.

Pre-write dedup (2026-10-17): working-tree case-insensitive searches for `alpha7`, `alpha07`, `alpha#7`, `alpha-007`, `adv20`, `delta(close, 7)`, and `ts_rank`/`Ts_Rank` return zero strategy records embodying this rule — the nine sibling `worldquant-alpha*` records (6, 9, 12, 23, 24, 46, 53, 54, 101) use different formulas, and the only `volume-gate` vocabulary hit (`alma-cross-volume-gate`) is an ALMA-cross record with an EMA-volume-oscillator gate and fixed-percentage exits (see Negative evidence 6). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Closed-reviewer precedents (#6 WaveTrend tie semantics, #10 golden-cross spot/short, #17 MACD-hist seeding, #20 Ichimoku-RSI always-in-market funding) are different rules. This is the tenth WorldQuant-101 record in the pool family, not a parameter variant of any admitted rule.

## Economic mechanism

### Source-reported

Coarse mean-reversion/momentum building blocks. The paper frames its universe coarsely: `one can think of alpha signals as based on mean-reversion or momentum`, where `a mean-reversion alpha has a sign opposite to the return on which it is based`, and adds that `in complex alphas elements of mean-reversion and momentum can be mixed`. Alpha#7 is a volume-gated mean-reversion block in one line: when today's volume prints above its 20-day average, the score is the negated 60-bar time-rank of the 7-day close-change magnitude, signed against that change — a score opposite in sign to the trailing 7-day move, scaled by how extreme the move is relative to its own 60-bar history. When volume prints at or below its average, the score is a flat `-1` short default. The paper ships no behavioural, structural, or risk-premium mechanism beyond this measurement construction, and no stop, target, or risk leg of any kind.

### Research interpretation

Volume-regime-gated 7-day contrarian with time-rank magnitude, two-sided, threshold-free. Unlike sibling worldquant-alpha6 (a single negated 10-day open-volume correlation with no gate, no ternary, and no magnitude object) this rule never correlates anything: its gate is a level comparison of volume against its own average, and its signal leg multiplies a magnitude rank by a change sign. Unlike sibling worldquant-alpha12 (a 1-day bilinear product `sign(volume-change) × (−price-change)` with no window, no average, and no gate) this rule's memory is 60+ bars deep and its volume read is a regime gate, not a signed multiplier. Unlike pool `alma-cross-volume-gate` (ALMA 60/120 trend cross gated by an EMA volume oscillator with fixed 2%/2.5% take/stop exits) there is no moving-average trend object, no oscillator, and no stop/target of any kind. Unlike weekly-momentum or run-length records (liu-tsyvinski-1w Sunday-log momentum, double-seven Connors pullback channel, eight-day-run SMA5 run reversal) there is no calendar week, no Donchian-style channel, and no run counter — the memory object is a time-rank of absolute 7-day changes. The failure mode is plain: the else-branch defaults to short, so a quiet tape sits short through drift with no guardrail, and a volume spike into a fast move fires the contrarian leg at the worst print of the swing — disclosed, not upgraded.

## Signal

Exact rule as pinned (any other lookback, series, gate, magnitude, sign treatment, fill, frame, book, or tie treatment is a different, unpinned rule):

- Inputs (paper A.2): `close[t]`, `volume[t]` on completed `1d` bars — the kline prints as-is (base-asset volume, no quote conversion, no normalization). No `open`, no `high`, no `low`, no vwap/cap/sector, no cross-sectional rank, no second asset or timeframe is read by any order-gating line.
- Average (pinned impl lines 235–236): `adv20[t] = mean(volume[t-19 .. t])` — trailing 20-bar simple average of the same volume series. Paper-dollar definition fenced in Negative evidence 5; this record implements the pinned implementation literally.
- Change (paper A.1, pinned impl lines 74–82): `change[t] = close[t] − close[t-7]` — undefined on the first 7 completed bars by construction.
- Magnitude (paper A.1, pinned impl lines 47–67 and 154–157): `mag[t] = ts_rank(abs(change), 60)[t]` — trailing 60-bar time-rank of the 7-day-change magnitude with tie-averaged ordinals divided by 60, hence in `[1/60, 1]` and strictly positive whenever defined; undefined before 60 consecutive finite changes exist (see Required data).
- Score (paper Appendix A, pinned impl lines 262–265): `score[t] = -mag[t] * sign(change[t])` if `adv20[t] < volume[t]` (strict `<`: equality takes the else-branch), else `score[t] = -1.0`. Undefined (NaN-preserving per pinned `_if_else`) while `adv20[t]` or `volume[t]` is non-finite — flat by the warmup rule, never traded.
- Direction mapping (source-grounded, fenced in Negative evidence 1): `score[t] > 0` → long signal (fires exactly when the gate passes and the 7-day change is negative — the contrarian long); `score[t] < 0` → short signal (gate passes with a positive 7-day change, or any gate-fail bar via the `-1.0` default); `score[t] == 0` → flat signal (exact-zero prints only when `change[t]` is exactly zero, because `mag[t]` is strictly positive whenever defined — deterministic flat, never a held conviction). The entry fills at the next bar's open, one single unit, only if the book does not already carry that side (see position rule).
- Exit: the first opposite signal reverses the full unit in one step (close plus opposite entry at the same next-bar-open fill); a zero print flattens the full unit at the next open — reversal-or-flatten is the sole exit path by construction. Consecutive same-side bars (including consecutive `-1.0` gate-fail bars) extend one continuous hold, never re-enter. No stop-loss, no take-profit, no trailing, no time exit (the paper ships no risk leg — carried over exactly, disclosed in Provenance adaptation (4), never upgraded into a source claim).
- Direction: two-sided (long leg fires on gated 7-day falls; short leg fires on gated 7-day rises and on every gate-fail bar). Shorts are native to USDT-M margin (no uptick rule, no borrow desk).
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further long-signal bars as no-ops (no pyramiding, no averaging), and symmetrically for shorts. Re-entry re-arms on the next opposite or flat-exit signal only (no cooldown specified — explicitly none, not invented). Pre-first-signal bars are flat.

## Required data

- Completed `1d` bars of BTCUSDT: `close` and `volume` only (the change leg reads closes; the gate and average read volumes). No `open`, no `high`, no `low`, no funding-signal, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar-table, or cross-venue state is read by any order-gating line. The `volume` read is the kline's printed base-asset volume as-is.
- Single decision timeframe `1d` (no multi-timeframe call, no cross-sectional ranking — one asset, one frame; every operator reads trailing completed bars of the same two series, never a second feed).
- Warmup: 72 completed `1d` bars flat by record rule — structural minimum is the 67th completed bar (the 7-day change is first defined on the 8th bar; the 60-bar time-rank needs 59 further finite changes; the 20-bar average needs 20 bars), plus margin per the admitted worldquant-alpha6 precedent. Pre-warmup bars are flat by record rule; missing bars are skipped on available completed bars only — prices and volumes are never fabricated. No repainting (every operator reads completed bars only), no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance USDT-M perpetual under the house overlay (researcher choice — the paper names no venue and evaluates U.S. equities; no source-market equivalence is claimed; perpetual is the minimal realistic venue because the short leg needs margin).
- Order timing (paper-grounded derivation): completed-bar decision with next-bar-open market fills for entries, reversals, and flat-exits — the paper's delay-1 class trades `on the day subsequent to the date of the most recent data`, `starting at the open`, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) on the same verified primitive as the admitted caporale-plastun, ehlers-cg, and worldquant-alpha6/alpha12/alpha101 records' entries (verified this cycle's base). This record claims no other fill convention: no perfect-open print, no maker-touch, no intrabar-path-dependent fill.
- Stop/limit modeling: none — the derived spec carries zero stop/limit/trailing orders by record rule. No hidden Hummingbot stop-order defaults are relied upon, and with no stop/limit legs there is no same-bar TP/SL ordering ambiguity.
- Sizing/capital/costs: the paper ships no sizing, capital, fee, or slippage concept. The explicit house overlay (single-unit frame, pinned house taker fees both legs, modeled funding while held) applies to the derived evaluation here, never presented as source-native behavior. Funding is never zero-claimed: gate-fail stretches hold short across the `00:00`/`08:00`/`16:00 UTC` funding stamps, so every held bar carries modeled funding.
- Concurrency: at most one single-asset engine position at any time; an opposite signal closes-and-reverses in one step and a zero signal closes-to-flat. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic, no hedge-mode requirement by construction.

## Evidence

### Source-reported

With exact provenance (live-fetch arXiv PDF bytes this cycle, read end to end): the `are also computer code` formula status; the Alpha#7 two-line formula `((adv20 < volume) ? ((-1 * ts_rank(abs(delta(close, 7)), 60)) * sign(delta(close, 7))) : (-1 * 1))`; the A.1 operator definitions (`abs/log/sign` standards, `delay(x, d)`, `delta(x, d)`, `ts_rank(x, d)`, integer-safe floor rule); the A.2 input definitions (`volume = standard definitions`, `adv{d} = average daily dollar volume`); the §2 delay-1 definition and the footnote-11 delay-0 exclusion list (`42, 48, 53 and 54` — Alpha#7 absent, hence delay-1); the §2 mixed building-block framing with the mean-reversion opposite-sign sentence; the §2 Alpha#101 direction sentence itself (`runs up intraday ... the next day one takes a long position`). With exact implementation provenance (pinned commit `4fc0627d`, file `toraniko/alpha101.py` lines 42–44, 47–67, 74–82, 85–93, 154–157, 192–199, 235–236, and 262–265, head re-confirmed via the commits API this cycle): the executable gate/magnitude/sign semantics, the full-window-undefined convention, the strictly-positive time-rank convention, and the NaN-preserving conditional. This record claims no source-reported performance number of any kind — no return, no win rate, no trade count, no per-alpha table figure is carried into the derived specification — and no reproduced performance exists.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Direction words fenced, admitted plainly: the paper never prints `buy`, `sell`, `long`, or `short` for Alpha#7. The positive→long / negative→short mapping rests on the §2 Alpha#101 worked example (a positive intraday score takes `a long position` the next day) together with the implementation report's long-top / short-bottom construction — not on any order verb attached to Alpha#7 itself. Supporting (never substituting) evidence: the paper's own taxonomy sentence that `a mean-reversion alpha has a sign opposite to the return on which it is based` describes exactly the gate-pass leg (`-mag × sign(change)`). A reviewer must not graft any other direction convention onto this record.
2. Timeframe and venue fenced: the paper is daily U.S. equities and names no venue. `1d` BTCUSDT-perpetual is the disclosed researcher pin (Provenance adaptation (1)); a reviewer must not cite the paper as evidence for any frame or venue.
3. Risk silence fenced: the paper contains no stop, target, trailing, time exit, or risk paragraph for Alpha#7 — the no-guardrail posture (including the short-default else-branch sitting through drift) is carried over exactly, never upgraded, never presented as a tested safety choice.
4. Cross-sectional machinery fenced: the paper's own evaluation ranks scores across thousands of stocks. Alpha#7's printed formula contains no `rank(`, no `IndNeutralize`, no `scale(`, no `vwap`, no `cap`, and no sector/industry term (verified by token filter over the extracted Alpha#7 lines this cycle) — the single-asset gate-and-sign map drops the cross-sectional portfolio layer entirely, disclosed as adaptation, never presented as the paper's traded portfolio.
5. Dollar-volume definition fenced: the paper defines `adv{d}` as average daily *dollar* volume while the printed gate compares it against `volume`. This record implements the pinned implementation literally — `adv20` as the 20-bar SMA of the kline base-asset volume series compared against that same series (impl lines 235–236, 265) — with no invented quote conversion. A dollar/quote-volume variant of the gate would be a different, unpinned rule. A reviewer must not substitute it.
6. Overlap fences, admitted plainly: sibling `worldquant-alpha6` trades a single negated 10-day open-volume correlation with no gate, no ternary, and no magnitude object (different construction, different inputs); sibling `worldquant-alpha12` trades a 1-day product `sign(volume-change) × (−price-change)` with no window, no average, and no gate; pool `alma-cross-volume-gate` crosses ALMA 60/120 gated by an EMA volume oscillator with fixed 2%/2.5% take/stop exits (trend-cross object with risk legs — this record has neither); pool `liu-tsyvinski-1w-momentum` holds Sunday-close log momentum for whole UTC weeks, long-flat (calendar object, no gate, no contrarian leg); pool `double-seven` trades a Connors MA200-regime 7-day channel pullback, long-only (channel object, no average gate, no time-rank); pool `eight-day-run` reverses SMA5 run-length extremes (run counter, no volume read at all); pool `ehlers-correlation-trend` correlates closes against a deterministic ramp with fixed thresholds, long-flat (different second series, no gate, no ternary). Shared `volume`/`7-day`/`contrarian`/`correlation` vocabulary is not shared signal.
7. No hidden variants admitted: any other lookback, any other gate series or threshold, any volume normalization, any threshold, any stop/target/filter/cooldown, any other frame, fill, venue, or book is a different, unpinned rule. A reviewer must not pick among these to rescue or reshape the record.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `adv20 < volume` gate / `-ts_rank(abs(delta(close,7)),60) × sign(change)` / `-1.0` else / strict-`<` equality / exact-zero flat / two-sided / delay-1 next-open fills / no-stop posture / `1d` BTCUSDT perpetual are frozen.

- F1 — Gate relevance: a gate-blind twin (always the contrarian leg `-mag × sign(change)` — same magnitude, book, grid, fills) must not improve net expectancy; fail ⇒ the `adv20 < volume` regime gate adds nothing over the ungated contrarian on this market.
- F2 — Direction-mapping relevance: a with-trend twin (long on positive change, short on negative change — same gate, magnitude, grid, fills, and reversal book) must not improve net expectancy; fail ⇒ the paper's contrarian mapping adds nothing over following the 7-day move on this market.
- F3 — Horizon relevance: a 21-day twin (`delta(close, 21)` with the same gate, 60-bar magnitude, grid, fills, and an 85-bar adopted warmup for the 80-bar structural minimum) must not improve net expectancy; fail ⇒ the 7-day horizon adds nothing over the same construction at triple the scale, and the record is a horizon label rather than a horizon edge.

## Crypto portability

Pinned to BTCUSDT Binance USDT-M perpetual under the house overlay (declared port of a venue-free daily-equity formula). The rule reads completed daily bars only, so no pit-session, gap, roll, split/dividend-adjustment, or corporate-action logic ports (the paper's split/dividend close adjustment touches only delay-0 open-anchored alphas — a non-issue for this trailing completed-bar construction on crypto, disclosed, not modeled). The magnitude leg is scale-free (a time-rank in `(0, 1]` whose sign alone trades with the change) yet the gate compares raw volume levels — the volume read is the kline print as-is with no normalization to invent, and volume-scale behaviour differs across venues. The rule is two-sided, so a spot-only deployment expresses only long-firing bars while short-firing bars stay venue-gated (never silently converted) — a spot-only variant would be a different, unpinned claim. No warmup history beyond 72 `1d` bars is consumed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- No price stop, no time stop: the short-default else-branch can sit short through extended drift, and a volume-spiked contrarian entry has no guardrail before the opposite signal, by the carried-over paper design — the record's principal risk.
- Short-default bias: quiet tapes (volume at or below average) print `-1.0` indefinitely — the book rests short, not flat, through low-activity stretches, disclosed.
- Near-zero whipsaw exposure: when the 7-day change hovers around zero, the gated leg flips long-short on microstructure noise at the worst prints of each swing — the paper provides no buffer band and this record invents none.
- Magnitude saturation: a steadily growing |change| trend pins `mag` near 1.0, so the rank stops discriminating while the sign keeps firing — the construction cuts both ways, disclosed.
- Exact-zero note: the flat branch fires only on exact-zero 7-day changes — rare on BTCUSDT, so the book is effectively always-in-market, disclosed.
- Single-venue port residual: paper-regime U.S. equities vs Binance perpetual execution (prints, fees, funding, volume-definition per Negative evidence 5, margin mechanics beyond the house model) is unclaimed, disclosed.
- Performance evidence is absent: nothing here is calibrated, fitted, or tuned to any backtest.
- Author scope: the paper presents production formulaic alphas as research objects, not a vetted retail trading system — this record is research-only and claims no live suitability.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior and never part of this admission — no Safety-Order/DCA event is admitted in this record's version. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Kakushadze, Z., `101 Formulaic Alphas`, arXiv:1601.00991 (manuscript December 9, 2015 — Alpha#7 formula, A.1 operator definitions, A.2 daily price/volume/adv inputs, §2 delay-1 definition with footnote-11 delay-0 exclusion, §2 mean-reversion taxonomy and Alpha#101 direction worked example — live-fetch PDF bytes read end to end 2026-10-17, sha256 `1f9c21afe32dcb3ee77b31548acdaea00451fbfa1c0ee10c907867bcc736fce9`): https://arxiv.org/abs/1601.00991
- Same paper, PDF (formula appendix, operator/input definitions, empirical sections — read 2026-10-17): https://arxiv.org/pdf/1601.00991
- OctopusTakopi `toraniko-alpha101` (independent audited implementation — `alpha007` at `toraniko/alpha101.py` lines 262–265, `_adv` at lines 235–236, `_window`/`_rank_1d`/`delay`/`delta`/`_rolling`/`ts_rank`/`_if_else` at lines 42–44, 47–67, 74–93, 154–157, 192–199 — pinned to commit `4fc0627d2a720fd8d583708ef051b9d48d98aacd`, head re-confirmed via the GitHub commits API 2026-10-17): https://github.com/OctopusTakopi/toraniko-alpha101
