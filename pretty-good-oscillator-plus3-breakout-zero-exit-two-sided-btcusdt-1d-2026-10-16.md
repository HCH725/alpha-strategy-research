---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Pretty Good Oscillator ±3 breakout with zero exit two-sided on BTCUSDT 1d bars
created: 2026-10-16
updated: 2026-10-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-04-19
sources:
  - https://github.com/mementum/backtrader/blob/master/backtrader/indicators/prettygoodoscillator.py
  - http://user42.tuxfamily.org/chart/manual/Pretty-Good-Oscillator.html
  - https://figurebetter.com/guides/indicators/pretty-good-oscillator
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Pretty Good Oscillator ±3 breakout with zero exit two-sided on BTCUSDT 1d bars

## Provenance

Primary sources read and re-verified end to end during this cycle (2026-10-16), pinned:

- Pinned implementation (fetched twice this cycle — once via `master`, once via the pinned commit path — byte-identical, sha256 `7311adb7d02597a5234dd9e6dff43e15a98e919f10d65845688c54c3c285d050`): `mementum/backtrader`, file `backtrader/indicators/prettygoodoscillator.py`, pinned to master head commit `b853d7c90b6721476eb5a5ea3135224e33db1f14` (2023-04-19, confirmed still the repository head via the GitHub commits API this cycle). The class docstring prints the complete system: the `Pretty Good Oscillator (PGO) by Mark Johnson measures the distance of the current close from its simple moving average of period Average), expressed in terms of an average true range (see Average True Range) over a similar period`; the worked reading (`a PGO value of +2.5 would mean the current close is 2.5 average days' range above the SMA`); the full trading rule (`Johnson's approach was to use it as a breakout system for longer term trades. If the PGO rises above 3.0 then go long, or below -3.0 then go short, and in both cases exit on returning to zero (which is a close back at the SMA)`); and the formula (`pgo = (data.close - sma(data, period)) / atr(data, period)`). Code pins: `params = (('period', 14), ('_movav', MovAv.Simple),)` (numerator is a 14-bar Simple moving average by default) and construction `atr = ATR(self.data, period=self.p.period)` with `self.lines.pgo = (self.data - movav) / atr`.
- Pinned ATR definition (same commit, `backtrader/indicators/atr.py`, fetched this cycle): `AverageTrueRange`, defined by `J. Welles Wilder, Jr. in 1978`, `params = (('period', 14), ('movav', MovAv.Smoothed))`, `self.lines.atr = self.p.movav(TR(self.data), period=self.p.period)` — the denominator is Wilder-smoothed (RMA, α = 1/14) True Range over 14 bars by default. The source prints no fill-timing sentence and no stop/target/cooldown/pyramiding sentence of any kind.
- Independent corroboration (read this cycle): Kevin Ryde's Chart manual v275 §10.29 `Pretty Good Oscillator` (`http://user42.tuxfamily.org/chart/manual/Pretty-Good-Oscillator.html`, GPL) prints the same object and the same rule words verbatim (`PGO = (close - SMA[N] of closes) / EMA[N] of true range`; the `+2.5` worked reading; `breakout system for longer term trades`, `rises above 3.0 then go long, or below -3.0 then go short, and in both cases exit on returning to zero (which is a close back at the SMA)`). Its denominator prose says `EMA[N]` where backtrader pins `Smoothed` — fenced as corroborating prose, never a second spec (see Negative evidence 3).
- Interpretation corroboration (fetched and text-extracted this cycle): the FigureBetter `Pretty Good Oscillator` guide prints the same formula (`PGO = (Close − SMA(N)) ÷ ATR(N)`), the same `+2.5` worked example, and the same breakout polarity (`beyond +3` is a thrust to join, not to fade; exit keyed to the oscillator decaying back toward zero). It defaults its own examples to 89 periods — fenced as a different claim, never this record's pin (see Negative evidence 2).

Licence and rights: backtrader is public GPL research software; the Chart manual is public GPL documentation; the guide is a public explainer. This record cites and normalizes the rule (formula, parameters, thresholds, exit) and reproduces no source block beyond short factual quotations for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any single source file. The sources print the PGO formula, the 14-bar defaults, the ±3 breakout thresholds, and the return-to-zero exit, but ship no venue, no symbol, no timeframe, no order/fill sentence, no warmup seed, and no risk leg. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` Binance USDT-M perpetual `1d` (no source names any venue — frame/venue pin disclosed, never a source claim; perpetual is the minimal realistic venue because the rule fires a short leg and needs margin); (2) completed-bar decisions with next-bar-open market fills for entries, exits, and flips (no source prints a fill sentence — the pin follows backtrader order semantics and reuses the admitted next-bar-open primitive of the `caporale-plastun`, `ehlers-cg`, `worldquant-alpha6`, `worldquant-alpha9`, `worldquant-alpha12`, and `worldquant-alpha23` records' bar-port, disclosed, never an advantage claim; explicitly never same-bar-close); (3) an adopted 30-completed-bar warmup with pre-warmup bars flat by record rule (structural minimum is the 14th completed bar — SMA14 needs 14 closes and Wilder ATR14 needs 14 TR prints per the pinned code — plus margin for the Wilder-seed transient, disclosed); (4) house sizing/costs with modeled funding while held (no source ships any sizing, capital, fee, or slippage concept — never presented as source-native behavior). The SMA14 numerator, the Wilder-ATR14 denominator, the strict ±3 thresholds, the zero exit, the two-sided mapping, and the no-stop/no-target risk posture are source-grounded and unmodified.

Pre-write dedup (2026-10-16): working-tree case-insensitive searches for `pretty.?good`, `mark.?johnson`, and `pgo` return zero strategy records embodying this rule. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. The closest pool neighbours share only oscillator vocabulary, never the signal (see Negative evidence 7). No pool record computes `(close − SMA14) / ATR14` with ±3 breakout thresholds and a return-to-zero exit.

## Economic mechanism

### Source-reported

Volatility-normalized breakout thrusts. Both primary implementations frame PGO as a distance-from-mean meter in ATR units and quote Johnson's use as a breakout (continuation) system for longer-term trades: pushes beyond ±3 are strength to join, and positions end when price returns to its mean — coarse momentum/trend-continuation building blocks. No source prints any economic rationale beyond this thrust-and-decay description, and no source ships any stop, target, or risk paragraph.

### Research interpretation

Single-asset ATR-unit breakout book, two-sided with a deadband. `PGO[t] = (close[t] − SMA14[t]) / ATR14[t]` reads how many daily ranges the close sits from its own 14-bar mean. Beyond `+3` the market has thrust three ranges above its mean (long); below `−3` it has thrust three ranges under it (short); between the thresholds the book holds its state; a return to the mean (`PGO = 0`, i.e. close back at the SMA) ends the ride. Unlike pool `cci-threshold-extreme-reversal` (which fades extremes), this rule joins them — opposite polarity on purpose. Unlike pool `cmf-velocity`/`chaikin-oscillator` (volume-weighted money-flow oscillators), this rule never reads volume. Unlike signal-line-cross oscillators (`pmo`, `ppo`, `tsi`, `kst`), this rule crosses fixed levels, not a signal line. Magnitude beyond the threshold never sizes the book — only the side trades (single unit), so ATR-collapse spikes change timing, never exposure. The failure mode is plain: a thrust that immediately reverses is ridden all the way back to the mean with no guardrail — disclosed, not upgraded.

## Signal

Exact rule as pinned (any other period, series, smoothing, threshold, exit, fill, frame, book, or tie treatment is a different, unpinned rule):

- Inputs (pinned code): `open/high/low/close` on completed `1d` bars only — `high/low/close` feed the True Range and ATR, `close` feeds the SMA. No `volume`, no funding/OI/mark-index, trade, book, on-chain, options, sentiment, macro, session, calendar, or cross-venue state is read by any order-gating line.
- Construction (pinned code, period 14 throughout): `TR[t] = max(high[t] − low[t], |high[t] − close[t−1]|, |low[t] − close[t−1]|)` (Wilder definition per the pinned ATR docstring); `ATR14[t]` = Wilder-smoothed (RMA, α = 1/14) average of `TR` over 14 bars; `SMA14[t]` = Simple mean of `close[t−13..t]`; `PGO[t] = (close[t] − SMA14[t]) / ATR14[t]`. `ATR14[t] == 0` (fully flat window) leaves the quotient undefined → NaN → flat by record rule, never interpolated or seeded.
- State machine, evaluated once per completed bar in fixed priority (strict inequalities throughout): (0) non-finite `PGO[t]` → target FLAT; (1) `PGO[t] > +3.0` → target LONG (enter if flat, flip if short, hold if long); (2) `PGO[t] < −3.0` → target SHORT (enter if flat, flip if long, hold if short); (3) LONG and `PGO[t] <= 0` → target FLAT; (4) SHORT and `PGO[t] >= 0` → target FLAT; (5) otherwise hold. Exact `±3.0` prints take the hold/exit path (never entries); exact `0` exits any held position. Under the single-unit no-pyramid book, cross-through and level-hold entries are event-identical; the pin is level-with-no-op, never a cross-counting variant.
- Exits: return-to-zero only (rules 3–4), plus the NaN flat (rule 0). Flips (rules 1–2 against the held side) close and reopen as one deterministic next-open event pair with a single net position — never two concurrent positions. No stop-loss, no take-profit, no trailing, no time exit (no source ships any risk leg — carried over exactly, disclosed in Provenance adaptation (4), never upgraded into a source claim).
- Direction: two-sided overall (long on upside thrusts, short on downside thrusts, flat in the deadband and at the mean).
- Position rule (predeclared researcher pin): single-unit long-flat-short; already-positioned bars repeating the held side are no-ops (no pyramiding, no averaging, no scaling by PGO magnitude); flat-regime bars while flat are no-ops. Re-entry re-arms on the next threshold bar after a flat exit only (no cooldown specified — explicitly none, not invented). Pre-first-signal bars (before the adopted warmup completes) and any NaN-score bars are flat by record rule.

## Required data

- Completed `1d` bars of BTCUSDT: `open`, `high`, `low`, `close` only (the sole series the construction reads; `volume` is never read).
- Single decision timeframe `1d` (no multi-timeframe call, no cross-sectional ranking — one asset, one frame; the oscillator reads the same single bar stream, never a second feed).
- Warmup: 30 completed `1d` bars flat by record rule — structural minimum is the 14th completed bar (SMA14 needs 14 closes; Wilder ATR14 needs 14 TR prints per the pinned code; backtrader `minperiod` is the period), plus margin for the Wilder-smoothing seed transient. Pre-warmup and any NaN-score bars are flat by record rule; missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (construction reads completed bars only), no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance USDT-M perpetual under the house overlay (researcher choice — no source names any venue; no source-market equivalence is claimed; perpetual is the minimal realistic venue because the firing rule includes a short leg and needs margin).
- Order timing (disclosed researcher pin, source-silent): completed-bar decision with next-bar-open market fills for entries, exits, and flips — compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) on the same verified next-bar-open primitive as the admitted `caporale-plastun`, `ehlers-cg`, `worldquant-alpha6`, `worldquant-alpha9`, `worldquant-alpha12`, and `worldquant-alpha23` records' bar-port (verified this cycle's base). This record claims no other fill convention: no same-bar-close print, no maker-touch, no intrabar-path-dependent fill.
- Stop/limit modeling: none — the derived spec carries zero stop/limit/trailing orders by record rule. No hidden Hummingbot stop-order defaults are relied upon; each bar's outcome is a single deterministic event (hold, enter, exit, or flip at one next-open price).
- Sizing/capital/costs: no source ships any sizing, capital, fee, or slippage concept. The explicit house overlay (single-unit frame, pinned house taker fees on every fill leg, modeled funding while held long or short) applies to the derived evaluation here, never presented as source-native behavior. Funding is never zero-claimed: held bars span the `00:00`/`08:00`/`16:00 UTC` funding stamps, so every held bar carries modeled funding.
- Concurrency: at most one single-asset position (long, short, or flat) at any time; flips resolve to one net position in one step. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic, no hedge-mode requirement by construction.

## Evidence

### Source-reported

With exact provenance (pinned commit `b853d7c`, re-verified live this cycle): the Johnson attribution and distance-from-mean framing; the `+2.5` worked reading; the complete rule sentence (`rises above 3.0 then go long, or below -3.0 then go short, and in both cases exit on returning to zero (which is a close back at the SMA)`); the formula line (`pgo = (data.close - sma(data, period)) / atr(data, period)`); the `period = 14` and `_movav = Simple` code defaults; the ATR construction (`period = 14`, `movav = Smoothed`, Wilder 1978). With independent corroboration (Chart manual v275 §10.29, read this cycle): the identical formula shape, the identical `+2.5` reading, and the identical rule words. With interpretation corroboration (FigureBetter guide, fetched and text-extracted this cycle): the identical formula, the identical worked example, the breakout-join polarity, and the decay-to-zero exit key. This record claims no source-reported performance number of any kind — no return, no win rate, no trade count, no table figure is carried into the derived specification — and no reproduced performance exists.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Fill words fenced, admitted plainly: no source prints any fill sentence for this rule. Next-bar-open is the disclosed researcher pin (backtrader order semantics; verified admitted primitive) — never a source claim. A reviewer must not swap it to same-bar-close, maker-touch, or any intrabar fill.
2. Period fenced: `14` is the pinned code default (both the PGO class and the ATR class). The FigureBetter guide's `89` and third-party (e.g. Wickra-style `21`) defaults are different, unpinned claims — a reviewer must not swap any other period into this record.
3. Smoothing fenced: the denominator is Wilder-`Smoothed` TR per the pinned ATR code. The Chart manual's `EMA[N] of true range` prose corroborates the rule but is not a second executable spec, and vendor variants computing `(Close − (HH+LL)/2) / StdDev` under the same `PGO` name are a different indicator — never substituted here.
4. Entry-phrasing fenced: `rises above 3.0` reads as a cross, the position book pins level-with-no-op; under single-unit no-pyramid semantics the two are event-identical (first qualifying bar enters, repeats no-op). A reviewer must not graft any cross-counting, consecutive-bar, or confirmation variant onto this record.
5. Exit fenced: `returning to zero` is pinned as inclusive (`LONG and PGO <= 0`, `SHORT and PGO >= 0`) — exact-zero prints exit. Without this pin the touch would be ambiguous, so it is pinned here rather than left to the reviewer.
6. Undefined determinism fenced: `ATR == 0` (fully flat 14-bar window) yields NaN → flat; any non-finite input yields NaN → flat; pre-warmup bars are flat. All are predeclared record-rule flats, not source sentences — without them the degenerate prints would be ambiguous.
7. Overlap fences, admitted plainly: pool `cci-threshold-extreme-reversal` fades `(price − MA) / mean-deviation` extremes (a fade object with a different normalizer and opposite polarity — never this join-breakout); pool `cci-ema-rsi-cross` crosses an EMA with RSI confirmation (a confirmation object — never a fixed-level breakout); pool `cmf-velocity` and `chaikin-oscillator` weight by volume (money-flow objects — this record never reads volume); pool `pmo`/`ppo`/`tsi`/`kst` cross signal lines (signal-cross objects — never fixed-level thresholds); pool `elder-ray-123reversal-combo` builds Bulls/Bears Power against EMA13 with a 1-2-3 reversal combo (an Elder-Ray object — never an ATR-unit distance); pool `percent-b-mfi` crosses %B/MFI thrust lines (a dual-thrust object — never this ratio). Shared `close`/`SMA`/`ATR` vocabulary is not shared signal.
8. No hidden variants admitted: any other period, series, smoothing, threshold, exit, fill, frame, venue, book, stop, filter, or cooldown is a different, unpinned rule. A reviewer must not pick among these to rescue or reshape the record.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `(close − SMA14) / Wilder-ATR14` / strict `±3.0` / return-to-zero exit / two-sided single-unit book / next-bar-open fills / no-stop posture / `1d` BTCUSDT perpetual are frozen.

- F1 — Threshold relevance: a `±1.5`-threshold twin (same construction, exits, grid, fills, thresholds `3.0 → 1.5` only) must not improve net expectancy; fail ⇒ the ±3 breakout level adds nothing over a hair-trigger level, and the record is a threshold label rather than a thrust edge.
- F2 — Zero-exit relevance: an opposite-threshold-exit twin (same construction, grid, fills, exits on the opposite `∓3` print instead of zero) must not improve net expectancy; fail ⇒ riding thrusts back to the mean adds nothing over holding for the mirror thrust, and the exit is a label rather than an edge.
- F3 — ATR-normalization relevance: a Simple-SMA(TR,14)-denominator twin (same construction, thresholds, exits, grid, fills, Wilder smoothing → Simple mean of TR only) must not improve net expectancy; fail ⇒ the pinned Wilder normalization adds nothing over flat-window scaling, and the record is a smoothing label rather than a scaling edge.

## Crypto portability

Pinned to BTCUSDT Binance USDT-M perpetual under the house overlay (declared port of a venue-free rule). The signal is scale-free — a ratio in ATR units, so unlike absolute-dollar thresholds it ports across venues without re-scaling (the same cross-market comparability the guide notes) — yet its ATR-collapse hypersensitivity differs across venues' range microstructure (a dead-flat window prints NaN→flat here; a near-flat window prints outsized |PGO| thrusts elsewhere), disclosed without re-tuning, and any other period or divisor normalization would be a different, unpinned claim. The rule reads completed daily bars only, so no pit-session, gap, roll, split/dividend-adjustment, or corporate-action logic ports (equity-only adjustments are a non-issue on crypto — disclosed, not modeled). The rule is two-sided with a real short leg, so a spot-only deployment cannot express short-firing bars (they stay venue-gated, never silently converted to long or to always-flat within this record) — a spot-only variant would be a different, unpinned claim. No warmup history beyond 30 `1d` bars is consumed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- No price stop, no time stop: a thrust that immediately reverses is ridden the full distance back to the mean, by the carried-over source design — the record's principal risk.
- Flip-risk: a single bar printing the opposite threshold reverses the full unit immediately (exit and re-entry at one next-open print) — disclosed, not dampened with any confirmation or cooldown.
- ATR-collapse hypersensitivity: near-zero-range windows inflate |PGO|, firing ±3 thrusts on economically meaningless drift — disclosed, not capped or floored.
- Wilder-seed transient: early post-warmup ATR values still carry seeding memory; the 30-bar margin dampens rather than eliminates it — disclosed.
- Single-venue port residual: the rule's home regime is venue-free daily bars; Binance perpetual execution (prints, fees, funding, open-definition, margin mechanics beyond the house model) is unclaimed, disclosed.
- Next-open latency idealization: any live slippage between the signal bar's close and the realized next-open fill differs by construction — disclosed, research-only.
- Performance evidence is absent: nothing here is calibrated, fitted, or tuned to any backtest.
- Author scope: the implementations present Johnson's oscillator as a research object, not a vetted retail trading system — this record is research-only and claims no live suitability.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior and never part of this admission — no Safety-Order/DCA event is admitted in this record's version. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- mementum `backtrader` (independent pinned implementation — `PrettyGoodOscillator` formula, Johnson attribution, ±3/zero-exit rule, `period = 14`, Simple-MA numerator, ATR denominator in `backtrader/indicators/prettygoodoscillator.py`; Wilder `Smoothed` ATR definition in `backtrader/indicators/atr.py` — pinned to commit `b853d7c90b6721476eb5a5ea3135224e33db1f14`, verified live 2026-10-16): https://github.com/mementum/backtrader/blob/master/backtrader/indicators/prettygoodoscillator.py
- Same library, API docs (formula appendix, rule paragraph — read 2026-10-16): https://cloudquant.github.io/backtrader/en/api/indicators/backtrader.indicators.prettygoodoscillator.html
- Kevin Ryde `Chart` manual v275 §10.29 (independent corroboration — identical formula shape, worked reading, and rule words — read 2026-10-16): http://user42.tuxfamily.org/chart/manual/Pretty-Good-Oscillator.html
- FigureBetter `Pretty Good Oscillator` guide (interpretation corroboration — formula, worked example, breakout-join polarity, decay-to-zero exit — fetched and text-extracted 2026-10-16): https://figurebetter.com/guides/indicators/pretty-good-oscillator
