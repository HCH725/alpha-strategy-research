---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Trix dual-line band-gated trend two-sided on BTCUSDT 1d bars
created: 2026-10-09
updated: 2026-10-09
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-10-08
sources:
  - https://www.fmz.com/strategy/428683
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/Trix%E7%AE%80%E5%8D%95%E8%B6%8B%E5%8A%BF%E8%B7%9F%E8%B8%AA%E7%AD%96%E7%95%A5Trix-Simple-Trend-Following-Strategy.md
  - https://www.tradingview.com/pine-script-reference/v3/
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Strategy prose states the fast/slow moving-average gate as a cross event (EMA13 crosses above/below SMA68), but the pinned code gates on persistent level state (ema13>sma68 / ema13<sma68 evaluated on the signal bar)."
  - "Strategy prose states the long is closed when Trix re-crosses back above the middle band, but the pinned code can only fire the Buy exit on bars where the long gate still holds (Trix<Middle_Band), i.e. on cross-DOWN-through-band bars; the mirror holds for the short side."
  - "Strategy prose and the ema13 variable name promise a 13-period EMA, but the pinned code computes ema13 as sma(close,13), a simple arithmetic mean."
---

# Trix dual-line band-gated trend two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (immutable public mirror file plus its recorded FMZ canonical page, fetched 2026-10-09):

- Canonical page: https://www.fmz.com/strategy/428683 (`Trix Simple Trend Following Strategy`, author nickname `ChaoZhang`). The canonical page itself was fetched over HTTP during this cycle: its body carries the full strategy-logic prose (dual-TRIX construction, MA gate, band filter, entry/exit description) and no performance numbers of any kind; its executable block sits behind the site login wall, so no code was taken from the canonical page itself.
- Immutable mirror actually executed against (primary code source): repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (commit date 2025-04-30 11:10:28 +0800, subject `update`; verified repository head at research time via the GitHub commits API), exact file path `Trix简单趋势跟踪策略Trix-Simple-Trend-Following-Strategy.md` (non-ASCII filename preserved verbatim; percent-encoded blob URL in frontmatter). File 8260 bytes, SHA-256 `e34628b1c87acc48052687a802b3782798719834e832caa0faf3ce9558fecd74`. The mirror prints `> Detail` = https://www.fmz.com/strategy/428683 and `> Last Modified` = 2023-10-08 12:17:21 (adopted as `source_as_of`).
- Page-embedded backtest header inside the mirror's fenced block (verbatim substance): `start: 2023-09-07 00:00:00`, `end: 2023-10-07 00:00:00`, `period: 1h`, `basePeriod: 15m`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`. Cited as provenance only: neither the mirror nor the canonical page ships any return, win rate, profit factor, trade count, or cost basis — this record claims no source-reported performance (see Evidence).
- Full Pine `//@version=3` block read in full (`strategy("Trix simple", overlay=true)`, byline `Made by Zan`, credit to Nmike's Chat — no `pyramiding`, no `process_orders_on_close`, no `calc_on_every_tick`, no `commission_*`, no `initial_capital`/`default_qty_*` lines). Source fills are therefore next-bar-open by Pine v3 default at language-default sizing; this record's same-bar-close execution and house sizing are separately identified researcher adaptations, never presented as source-native (see Execution assumptions).
- Pinned source inputs: `lengtha = input(7, minval=1)`, `lengtha1 = input(4, minval=1)`, `bb = input(20)`. This record pins all three defaults; retuning any of them would be a different, unpinned rule.
- Text census over the pinned block: 2 `strategy.entry` / 2 `strategy.exit` / 0 `strategy.close` / 0 `strategy.order` / 0 `stop=`/`limit=`/`profit=`/`loss=` / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `volume` / 0 `open`/`high`/`low` price reference (the only price read anywhere is `close`, via `log(close)` and two SMAs). Live order calls are exactly four: `strategy.entry("Buy", strategy.long, when = crossover(Trix1,Trix))`, `strategy.exit("Buy", when = cross(Trix,Middle_Band))`, `strategy.entry("Sell", strategy.short, when = crossunder(Trix1,Trix))`, `strategy.exit("Sell", when = cross(Trix,Middle_Band))`. Both entry/exit pairs sit inside `if (longCondition)` / `if (shortCondition)` blocks, so no order call executes unless its side's gate holds on that bar.
- Prose-vs-code facts, admitted honestly and pinned to the code: (a) the prose describes the MA gate as a cross event, but the code evaluates persistent state (`ema13>sma68` / `ema13<sma68`) — the gate is level, not edge; (b) the prose says the long closes when Trix re-crosses back above the band, but `strategy.exit("Buy")` only executes inside `if (longCondition)`, which requires `Trix<Middle_Band` on the same bar, so the Buy exit can only fire on cross-DOWN-through-band bars while the bullish gate still holds (mirror proof for the short side in Negative evidence); (c) the variable is named `ema13` and the prose promises EMA13, but the code computes `ema13 = sma(close,13)` — a 13-period simple mean, pinned as written; (d) the Risk section states plainly that the strategy lacks any stop-loss (`缺乏止损策略`), so the no-stop/no-target posture is source-declared, not a gap.
- Prose performance language is qualitative only ("can profit from larger trends", "reduce false signals") with no table, figure, or number — named here as unusable water; no performance claim of any kind enters this record.

Licence and rights: the canonical page is a public FMZ strategy publication by ChaoZhang; the mirror file carries the Zan byline. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly four: (1) research market/timeframe BTCUSDT `1d` (the script reads only `close` and is symbol-agnostic; the page header ran 1h BTC_USDT Binance futures); (2) same-bar-close fills via `process_orders_on_close=true` (the source fills next-bar-open); (3) an explicit atomic-bar evaluation order — exits before entries — specified here because the source leaves same-bar order interaction to the broker-emulator ordering (proven net-conservative in Negative evidence); (4) an adopted 100-bar warmup (structural minimum is 69 bars; the extra margin covers triple-EMA seed decay and is disclosed as a researcher choice). All four adaptations are predeclared here, confined to Provenance, Signal, Execution assumptions, and Limitations, with every original claim kept separate above. Indicator formulas, lookbacks, thresholds, gate logic, trigger semantics, pyramiding default, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-09): working-tree word-boundary searches for `trix`, `428683`, and `coppock`/`qqe`/`schaff` return zero strategy records using this source, author strategy, or mechanism — no pool file mentions TRIX at all. Same-author ChaoZhang records exist (e.g. the Aroon file, FMZ 438795) but carry a different canonical identity, different indicator family, and different order set. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #58 (ML/portfolio reconstruction batch — file list verified, no TRIX or indicator record), and #63 (SuperTrend ATR-flip trend long) — different mechanisms, indicators, and sources. Closest pool records are different mechanism classes: `stochastic-ott-dual-trend-btcusdt-1d` is a price-rank %K/%D system, `fisher-zero-cross-reversal-btcusdt-1d` is a normalized nonlinear-transform zero-cross system, `vidya-cmo-adaptive-slope-trend-btcusdt-1h` is an adaptive-average slope system. Five-axis distinction: mechanism differs (log-price triple-EMA rate-of-change dual-line cross gated by SMA-trend state plus SMA-band-sign filter, two-sided with reversal), signal construction differs (no pool record evaluates `10000*change(ema(ema(ema(log(close),7),7),7))` against a 4-length twin and its own 20-bar SMA band), exits differ (band-cross-while-gated signal exits plus reversal versus trailing/time/opposite-cross exits), source identity differs (FMZ 428683 October-2023 versus other FMZ IDs or TV authors), and direction handling differs (symmetric two-sided gated by trend state versus long-only or differently gated records).

## Economic mechanism

### Source-reported

Triple-smoothed momentum of log price, after Jack Hutson: instead of smoothing prices once, the indicator passes `log(close)` through three chained EMAs and reads the one-bar change, so isolated spikes die across the three layers while sustained pressure moves the reading. A faster twin (length 4) crossing the slower line (length 7) times the turn; the SMA13/SMA68 trend-state gate plus the sign of the 20-bar band keeps entries on the trend side (longs only while price sits above its 68-bar mean and the band reads positive). Exits are signal-only: a band cross against the position while the gate still holds, or a reversal by the opposite entry. The author ships no fixed stop, no target, no trailing order, and says so explicitly.

### Research interpretation

Two-sided smoothed-momentum harvesting with a slow refinancing gate. Unlike stochastic or Fisher records, the trigger is a pure acceleration statistic on log price — identical price paths produce different signals depending on persistence across the triple-EMA window, and gap-size distortion is damped by the log. The dual gate (SMA-trend state AND band sign) means the system sits out chop where price straddles its long mean; the band-cross exit then bounds adverse excursion without any price-level stop, at the cost that a gate break before any band cross leaves the exit to the reversal leg. No leverage, sizing, or cost edge is embedded in the signal; language-default sizing is replaced by the house overlay (see Execution assumptions).

## Signal

Exact rule as pinned (defaults quoted — inputs unmodified):

- Declaration (derived): `strategy("Trix simple", overlay=true, process_orders_on_close=true)` — the first line is the source verbatim except `process_orders_on_close=true`, which is the predeclared researcher adaptation (source declaration carries no such argument), and except sizing/capital, whose language-default lines are absent in the source and replaced by the house overlay (see Execution assumptions). `pyramiding` is unset (v3 language default 0: no additional same-direction entry while positioned, opposite-direction entry reverses — load-bearing here, pinned explicitly, see Execution assumptions). `calc_on_every_tick` is unset (default false: exactly one evaluation per completed bar).
- Indicator (lengths pinned): `Trix = 10000 * change(ema(ema(ema(log(close), lengtha), lengtha), lengtha))` with `lengtha = 7`; `Trix1 = 10000 * change(ema(ema(ema(log(close), lengtha1), lengtha1), lengtha1))` with `lengtha1 = 4`; `Middle_Band = sma(Trix, bb)` with `bb = 20`. The `overlay=true` pane changes nothing about order semantics.
- Trend gate (level state, pinned as code — not a cross): `sma68 = sma(close,68)`; `ema13 = sma(close,13)` (simple mean despite the name — pinned as written). Long gate: `longCondition = ema13>sma68 and Middle_Band>0 and Trix<Middle_Band`. Short gate: `shortCondition = ema13<sma68 and Middle_Band<0 and Trix>Middle_Band`.
- Entry long: inside `if (longCondition)`, `strategy.entry("Buy", strategy.long, when = crossover(Trix1,Trix))` — strict cross up of the fast twin through the slow line while the long gate holds, evaluated on the completed-bar close with same-bar-close execution under the derived declaration.
- Entry short: inside `if (shortCondition)`, `strategy.entry("Sell", strategy.short, when = crossunder(Trix1,Trix))` — strict cross down while the short gate holds.
- Exit long: inside `if (longCondition)`, `strategy.exit("Buy", when = cross(Trix,Middle_Band))` — whole-position market exit, which given the enclosing gate can only fire on cross-DOWN-through-band bars (proven in Negative evidence), same completed-bar close.
- Exit short: inside `if (shortCondition)`, `strategy.exit("Sell", when = cross(Trix,Middle_Band))` — fires only on cross-UP-through-band bars.
- Direction: symmetric two-sided by pinned code path; flat is entered only via the exit legs (no standalone flat signal). A short-side instrument is required for the short legs; on a spot-only venue they are inexpressible and the record would not be the same rule (see Crypto portability).
- Evaluation order (predeclared specification): on each completed bar, evaluate the executing side's exit leg first, then its entry leg; an entry against an open opposite position reverses it (Pine pyramiding-0 parity). At most one side's block executes per bar (gates proven mutually exclusive), so the order specification only resolves same-block entry/exit co-firings.
- Display isolation: the script carries no `plot`/`hline` calls feeding any order condition; order logic reads only the series above.

## Required data

- Completed `1d` bars of BTCUSDT: `close` only (via `log(close)` triple-EMA chains and two SMAs). No `open`, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d`. The script takes no timeframe input and makes no live `request.*`/`security(`/`timeframe(` call, so it is single-frame by construction; `1d` is adopted as the research frame because it is a campaign timeframe — never presented as anything beyond that (see Limitations).
- Warmup: `sma(close,68)` is only full from the 68th completed `1d` bar, and every trigger additionally reads one prior bar, so the structural minimum is the 69th completed bar; the adopted warmup is the first 100 completed `1d` bars flat (predeclared researcher margin covering triple-EMA seed decay). Pre-warmup bars are flat by language semantics (`na`-gated conditions never open or close anything). No repainting, no negative shift, no future reference, no full-sample normalization; `calc_on_every_tick=false` gives exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT under the house overlay (the rule reads close-price persistence only; venue transfer from the page's 1h Binance-futures header is never presented as source-native semantics).
- Order timing (predeclared derivation): `process_orders_on_close = true` with `calc_on_every_tick` unset (default false): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester. The source's own timing is next-bar-open (declaration carries no such argument — quoted verbatim in Provenance); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill. Both `strategy.exit` legs carry no stop/limit/profit/loss/trailing argument, hence no stop/limit order and no same-bar TP/SL ordering ambiguity anywhere in the rule; the only ordering specification is the predeclared exits-before-entries atomic evaluation.
- Sizing/capital: the source declaration codes no sizing, capital, or commission line (language defaults apply in its own backtest), replaced here by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions, never presented as source-native behavior.
- Concurrency: `pyramiding` is unset (v3 default 0: no same-direction add while positioned; opposite-direction entry reverses). The default is load-bearing and therefore pinned explicitly: repeat trigger bars during an open same-side position are rejected no-ops, and re-entry is allowed immediately on the next qualifying gated cross after any exit (no cooldown specified — explicitly none, not invented). `strategy.exit` legs with no matching open position are deterministic no-ops. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The mirror file ships the log-triple-EMA TRIX construction (lengths 7 and 4), the 20-bar SMA band, the SMA13/SMA68 gate, the gated twin-cross entries, the band-cross exits, the explicit no-stop-loss admission, the six-item advantage/risk/optimization prose, and the 1h BTC_USDT Binance-futures backtest header with its 2023-09-07–2023-10-07 window. It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.close`, 0 `strategy.order`, 0 `stop=`/`limit=`/`profit=`/`loss=` — the band-cross `strategy.exit` pair plus opposite-entry reversal is the sole exit path by construction, and the optimization section's stop-loss wishes are explicitly future work, never rules.
2. Side blocks are mutually exclusive on every bar: `longCondition` needs `ema13>sma68 and Middle_Band>0 and Trix<Middle_Band` while `shortCondition` needs the strict mirror on all three comparisons — no single bar satisfies both, and equality on any comparison fires neither, so no same-bar long/short conflict exists to resolve.
3. Exit-leg reachability, proven: `strategy.exit("Buy")` executes only inside `if (longCondition)`, which requires `Trix<Middle_Band` on the same bar; combined with `cross(Trix,Middle_Band)=true` this admits only cross-DOWN-through-band bars (a cross-up bar has `Trix>Middle_Band`, contradicting the gate). The Buy exit therefore never fires on the prose-described re-cross above the band. The Sell mirror holds: it fires only on cross-UP-through-band bars while `Trix>Middle_Band`.
4. Entry/exit co-firing inside one block resolves conservatively under the predeclared exits-first order: a bar firing both the Buy entry and the Buy exit first flattens (or no-ops) then opens long — net long, identical to the source's net whenever the source's emulator orders the same two calls on the next open; the Sell mirror yields net short. No transition is invented by the ordering.
5. Boundary ties and flat ranges fire nothing: strict comparisons plus strict cross semantics (equality on either compared bar is not a cross); an indicator pinned exactly on the band across consecutive bars holds; `na` warmup bars open and close nothing.
6. Flat-state determinism: both `strategy.exit` legs with no matching open position are no-ops; same-side repeat triggers while positioned are rejected under pinned pyramiding 0; opposite-side gated triggers reverse; the seed bars satisfy no order condition by themselves (each cross needs a settled prior bar, the gate needs 68 bars).
7. The lengths (7/4/20/68/13), the SMA (not EMA) construction of `ema13`, the level-state (not cross) gate, the two-sided direction, reversal semantics, and no-stop/no-target/no-cooldown posture are pinned, not removed: retuning any length, restoring a true EMA13, converting the gate to a cross event, symmetrizing the exit to the prose description, adding a stop/target/cooldown/volume filter, or disabling a side would each be a different, unpinned rule — none is admitted here.
8. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT-`1d` research frame, same-bar-close fills, the exits-first atomic evaluation order, the adopted 100-bar warmup, and house sizing — all predeclared above; every signal, threshold, default, and risk posture is source-verbatim. This record is therefore never evidence that the original next-bar-open 1h source itself passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: TRIX(7)/twin(4) gated crosses / 20-bar band / SMA13-vs-SMA68 level gate with band-sign filter / band-cross-while-gated exits / two-sided with reversal / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Twin-trigger relevance: replacing the Trix1/Trix cross with a single-line Trix zero-cross (same gate and exit structure) must not improve net expectancy; fail ⇒ the dual-line cross adds nothing over a plain zero-line read.
- F2 — Band-exit relevance: dropping the two band-cross exit legs (reversal-only exits) must not improve net expectancy; fail ⇒ the while-gated band exits add nothing over plain reversal trading.
- F3 — Gate relevance: dropping the SMA13/SMA68-plus-band-sign gates (ungated twin-cross both sides) must not improve net expectancy; fail ⇒ the record is a gate-label variant of a plain TRIX-cross system.

## Crypto portability

Pinned to BTCUSDT under the house overlay. The close-only log-smoothing logic ports across perpetual venues without structural change; the short legs require a shortable instrument, so a spot-only deployment cannot express this rule (disabling the short side would be a different, unpinned rule). No funding-dependent leg, no stablecoin-specific assumption, no session, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (`open`/`high`/`low` are never referenced), so session-gap behavior is simply absent rather than approximated. `log(close)` needs strictly positive prices, true of every BTCUSDT bar. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing and frame: the source fills next-bar-open on 1h bars; this record executes same-bar-close on `1d` bars. Backtest economics of the two timings and frames differ by construction — the adaptations are disclosed, not hidden, and this record makes no claim about the source timing's performance.
- No price stop: adverse excursion after entry has no guardrail beyond the band cross or the reversal; a vertical-against move exits only when the twin lines re-cross the band or the opposite gate fires, which can be far.
- Gate-break stranding: if the trend gate breaks before any band cross, the side's exit leg stops executing and the position relies solely on a future opposite gated trigger — the source provides no time stop and this record invents none.
- Warmup cost: the adopted 100-bar warmup means the system is blind for the first 100 bars of any 1d evaluation window (structural minimum 69).
- Performance evidence is absent: the canonical page and mirror report no numbers at all (the Sep–Oct-2023 1h header is a run window, not a result, and its praise is qualitative prose); nothing here is calibrated, fitted, or tuned to any backtest.
- Prose-code divergence: the MA gate, the exit direction, and the EMA13 label in the prose all disagree with the pinned code in the ways fenced above; future readers must trust the code section, never the prose.

## Implementation status

Not implemented. No Hummingbot controller/executor, no Qlib screening, no Paper/Testnet/Live run has been performed from this record. Admission claims pinned-engine expressibility only (see Execution assumptions), subject to independent six-gate review.

## Adoption boundary

Research-only. Not approved for any downstream screening, parity run, or trading authorization. Only a `PASS` under the live six-gate contract may merge this record into `main`; any `NOT_LOSSLESS` finding closes the PR lane without promotion.

## Related Wiki records

None.

## Sources

- Canonical strategy page (fetched 2026-10-09; prose read, code login-walled): https://www.fmz.com/strategy/428683
- Immutable mirror file read end to end (fmzquant/strategies @ `7853bb2bf262c4567ac238d3552d97f0e50cb801`, 8260 bytes, SHA-256 `e34628b1c87acc48052687a802b3782798719834e832caa0faf3ce9558fecd74`): https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/Trix%E7%AE%80%E5%8D%95%E8%B6%8B%E5%8A%BF%E8%B7%9F%E8%B8%AA%E7%AD%96%E7%95%A5Trix-Simple-Trend-Following-Strategy.md
- Pine v3 strategy semantics (declaration defaults, order calls, close-evaluated execution): https://www.tradingview.com/pine-script-reference/v3/
- Pine strategy concepts: https://www.tradingview.com/pine-script-docs/concepts/strategies/
