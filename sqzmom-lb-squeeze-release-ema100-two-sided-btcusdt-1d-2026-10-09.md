---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: SQZMOM-LB squeeze-release linreg-momentum EMA100-gated two-sided on BTCUSDT 1d bars
created: 2026-10-09
updated: 2026-10-09
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-02-23
sources:
  - https://www.tradingview.com/script/G40dtEbK-Squeeze-Momentum-Indicator-Strategy-LazyBear-PineIndicators
  - https://www.tradingview.com/script/nqQ1DT5a-Squeeze-Momentum-Indicator-LazyBear/
  - https://www.tradingview.com/pine-script-reference/v5/
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Strategy prose states the long entry requires momentum positive (val>0), but the pinned code requires only val>val[1] and val above the trailing 100-bar low — no sign test exists anywhere in the order logic."
  - "Strategy prose states the short entry fires on squeeze release (gray after black), but the pinned code fires the short on the opposite transition (scolor==black with scolor[1]==gray, i.e. squeeze turning ON)."
  - "Strategy prose states the short entry requires momentum negative, but the pinned code requires only val<val[1] and val below the trailing 100-bar high — no sign test exists."
  - "The input mult=2.0 titled 'BB MultFactor' is never referenced: the Bollinger deviation is computed as multKC*stdev (1.5 sigma), so the effective BB is SMA20 +/-1.5 sigma, not the advertised 2.0."
  - "Strategy prose states position size is 8% of equity, but the pinned code computes qty=strategy.equity*8/close, i.e. 8x-equity notional, not 8%."
---

# SQZMOM-LB squeeze-release linreg-momentum EMA100-gated two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (canonical TradingView open-source strategy page, fetched 2026-10-09):

- Canonical page: https://www.tradingview.com/script/G40dtEbK-Squeeze-Momentum-Indicator-Strategy-LazyBear-PineIndicators (`Squeeze Momentum Indicator Strategy [LazyBear + PineIndicators]`, author `PineIndicators`, page date `Feb 23, 2025`, adopted as `source_as_of`). The page body carries the full strategy-logic prose (squeeze construction, momentum breakdown, entry/exit lists, position-sizing and risk-management sections) and the complete open-source Pine v5 block (55 lines, `View in Pine Editor・55 lines`), both read in full during this cycle — no login wall, no missing fragment.
- Lineage stated on the page: an automated strategy built on LazyBear's `Squeeze Momentum Indicator`, itself a modification of John Carter's `TTM Squeeze` concept (`Mastering the Trade`, chapter 11). The original LazyBear indicator page (https://www.tradingview.com/script/nqQ1DT5a-Squeeze-Momentum-Indicator-LazyBear/) is cited as lineage only; every pinned rule below comes from the PineIndicators strategy block, never from the indicator page or the book.
- Full declaration read verbatim: `strategy(shorttitle='SQZMOM_LB Strategy', title='Squeeze Momentum Indicator Strategy [LazyBear + PineIndicators]', overlay=false)` — no `pyramiding`, no `process_orders_on_close`, no `calc_on_every_tick`, no `commission_*`, no `initial_capital`/`default_qty_*` lines. Source fills are therefore next-bar-open at language-default sizing under single evaluation per completed bar; this record's same-bar-close execution and house sizing are separately identified researcher adaptations, never presented as source-native (see Execution assumptions).
- Pinned source inputs: `length=20` (BB Length), `mult=2.0` (BB MultFactor — dead input, never referenced; see contradictions), `lengthKC=20` (KC Length), `multKC=1.5` (KC MultFactor), `useTrueRange=true`. This record pins all effective defaults; retuning any of them would be a different, unpinned rule.
- Text census over the pinned block: 2 `strategy.entry` / 0 `strategy.exit` / 2 `strategy.close` / 0 `strategy.order` / 0 `stop=`/`limit=`/`profit=`/`loss=` / 0 `request.*` / 0 `input.timeframe` / 0 volume/open-gap/session reference. Live order calls are exactly four: `strategy.entry('L', strategy.long, qty=qty)`, `strategy.close('L')`, `strategy.entry('S', strategy.short, qty=qty)`, `strategy.close('S')`.
- Prose-vs-code facts, admitted honestly and pinned to the code: (a) prose promises a `val>0` long filter and a `val<0` short filter, but the code tests only direction (`val>val[1]` / `val<val[1]`) plus the trailing-extreme filter — sign is never tested; (b) prose promises both entries on squeeze release, but the short leg is coded on the squeeze-ON transition (`scolor==black` with `scolor[1]==gray`); (c) the `mult=2.0` BB input is dead — BB deviation uses `multKC` (1.5); (d) prose promises 8%-of-equity sizing, but `qty=strategy.equity*8/close` is 8x-equity notional. All five are fenced in frontmatter `contradictions` and Negative evidence; the code governs everywhere.
- Risk prose (`Risk Management` section) advises the reader to add stop-losses precisely because the script ships none — the no-stop/no-target posture is therefore source-declared absence, not a gap (cf. the merged TRIX record's no-stop precedent).
- Page performance language is qualitative only ("often precede explosive price movements", "most effective on higher timeframes") with no table, figure, or number — named here as unusable water; no performance claim of any kind enters this record.

Licence and rights: the canonical page is a public TradingView open-source publication by PineIndicators. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly five: (1) research market/timeframe BTCUSDT `1d` (the script reads only OHLCV and is symbol-agnostic; the prose recommends stocks/indices/forex on 1H/4H/Daily); (2) same-bar-close fills via `process_orders_on_close=true` (the source fills next-bar-open); (3) an explicit atomic-bar evaluation order — closes before entries — specified here because the source leaves same-bar order interaction to the broker-emulator ordering (proven net-conservative in Negative evidence); (4) an adopted 150-bar warmup (structural minimum is 120 bars; the extra margin covers EMA100 seed decay and is disclosed as a researcher choice); (5) house sizing/capital replacing the script's 8x-equity `qty` line (see Execution assumptions). All five adaptations are predeclared here, confined to Provenance, Signal, Execution assumptions, and Limitations, with every original claim kept separate above. Indicator formulas, lookbacks, thresholds, transition logic, pyramiding default, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-09): working-tree word-boundary searches for `sqzmom`, `linreg`, `squeeze` (signal use), `G40dtEbK`, `PineIndicators`, and `TTM` return zero strategy records using this source, author script, or mechanism — the only `squeeze`/`lazybear` hits anywhere are passing mentions inside older records' dedup paragraphs (closed PR #6 LazyBear WaveTrend oscillator-cross, never on `main`) and Wiki links. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #58 (ML/portfolio reconstruction batch — file list verified, no squeeze or band-compression record), and #63 (SuperTrend ATR-flip trend long) — different mechanisms, indicators, and sources. Closest pool records are different mechanism classes: `keltner-momentum-breakout-gated-btcusdt-1d` is a pure Keltner-channel breakout (no Bollinger compression test, no linreg momentum, no EMA gate), `stochastic-ott-dual-trend-btcusdt-1d` is a stochastic/OTT trailing system, `donchian-20-10-breakout-btcusdt-1h` is a highest/high-low breakout. Five-axis distinction: mechanism differs (BB-inside-KC volatility-compression regime plus linreg-of-detrended-price momentum plus EMA100 trend gate, two-sided with asymmetric transitions), signal construction differs (no pool record evaluates `linreg(close-avg(avg(highest(high,20),lowest(low,20)),sma(close,20)),20,0)` against squeeze-state transitions and a 100-bar trailing extreme), exits differ (any-bar momentum-downtick/up-tick closes versus band/trailing/opposite-cross exits), source identity differs (TV `G40dtEbK` February-2025 versus other TV authors or FMZ IDs), and direction handling differs (asymmetric two-sided: longs on release, shorts on squeeze-ON — versus symmetric or long-only records).

## Economic mechanism

### Source-reported

Volatility compression precedes expansion: when Bollinger Bands sit inside Keltner Channels the market is coiling (black cross on the midline); when the bands push back outside, stored energy releases (gray cross). The strategy takes the release in the direction of a linear-regression momentum readout — long if momentum is rising off a trailing 100-bar low while price holds above its 100-bar mean and ticks up, short on the mirror while price holds below its mean. Any momentum downtick flattens a long; any uptick flattens a short. The author ships no stop, no target, no trailing order, and tells the reader to arrange their own stops.

### Research interpretation

Two-sided compression-release harvesting with a slow refinancing gate. Unlike pure breakout records, the trigger is a regime transition (band geometry) ANDed with a detrended-regression momentum filter and a 100-bar mean gate, so entries require compression, impulse, and trend agreement at once. The exit is deliberately hair-trigger — a single adverse momentum tick — which bounds adverse excursion without any price-level stop, at the cost of chopping out of slow-burn moves. The coded short leg is notably contrarian in timing (it enters as compression turns ON, not on release), so the two sides are not mirrors; each side must be judged on its own coded leg, never on the prose symmetry the page advertises.

## Signal

Exact rule as pinned (defaults quoted — effective inputs unmodified, dead `mult` fenced):

- Declaration (derived): `strategy(shorttitle='SQZMOM_LB Strategy', title='Squeeze Momentum Indicator Strategy [LazyBear + PineIndicators]', overlay=false, process_orders_on_close=true)` — the first line is the source verbatim except `process_orders_on_close=true`, which is the predeclared researcher adaptation (source declaration carries no such argument), and except sizing/capital, whose `qty` line is replaced by the house overlay (see Execution assumptions). `pyramiding` is unset (v5 language default 0: no additional same-direction entry while positioned, opposite-direction entry reverses — load-bearing here, pinned explicitly, see Execution assumptions). `calc_on_every_tick` is unset (default false: exactly one evaluation per completed bar).
- Compression geometry (lengths pinned): `basis=sma(close,20)`; `dev=1.5*stdev(close,20)` (via `multKC` — the `mult=2.0` input is dead, pinned as written); `upperBB/lowerBB=basis±dev`. `ma=sma(close,20)`; `rangema=sma(TR,20)` with True Range (`useTrueRange=true` default); `upperKC/lowerKC=ma±rangema*1.5`. States: `sqzOn = lowerBB>lowerKC and upperBB<upperKC` (BB strictly inside KC); `sqzOff = lowerBB<lowerKC and upperBB>upperKC` (BB strictly outside KC); `noSqz` = neither. Plot color `scolor`: blue when `noSqz`, black when `sqzOn`, gray otherwise.
- Momentum (pinned): `val=linreg(close-avg(avg(highest(high,20),lowest(low,20)),sma(close,20)),20,0)` — linear regression (offset 0) of close minus the average of the 20-bar Donchian midpoint and the 20-bar SMA. Histogram color only (lime/green/red/maroon) is display, never order-gating.
- Trend and microstructure gates (pinned): `ta.ema(close,100)`; `ta.lowest(val,100)[1]` / `ta.highest(val,100)[1]` (trailing 100-bar extremes excluding the signal bar); `close` vs `close[1]`.
- Entry long: `scolor==gray and scolor[1]==black and val>val[1] and val>lowest(val,100)[1] and close>close[1] and close>ema(close,100)` → `strategy.entry('L', strategy.long)` — squeeze-release transition with rising momentum above its trailing 100-bar low, uptick close above the 100-EMA, evaluated on the completed-bar close with same-bar-close execution under the derived declaration. No `val>0` test exists — pinned as written.
- Entry short: `scolor==black and scolor[1]==gray and val<val[1] and val<highest(val,100)[1] and close<close[1] and close<ema(close,100)` → `strategy.entry('S', strategy.short)` — squeeze-ON transition (coded opposite of the prose release claim) with falling momentum below its trailing 100-bar high, downtick close below the 100-EMA. No `val<0` test exists — pinned as written.
- Exit long: `val<val[1]` → `strategy.close('L')` — whole-position close on any momentum downtick, same completed-bar close, unconditional (fires even on the entry bar's evaluation when momentum falls).
- Exit short: `val>val[1]` → `strategy.close('S')` — mirror.
- Direction: asymmetric two-sided by pinned code path; flat is entered only via the close legs (no standalone flat signal). A short-side instrument is required for the short legs; on a spot-only venue they are inexpressible and the record would not be the same rule (see Crypto portability).
- Evaluation order (predeclared specification): on each completed bar, evaluate the closing legs first, then the entry legs; an entry against an open opposite position reverses it (Pine pyramiding-0 parity). At most one entry leg can fire per bar (long needs `scolor==gray`, short needs `scolor==black` — mutually exclusive), so the order specification only resolves same-bar close/entry co-firings.
- Display isolation: `plot`/`plot.style_histogram`/`plot.style_cross` calls feed no order condition; order logic reads only the series above.

## Required data

- Completed `1d` bars of BTCUSDT: `close`, `high`, `low` (via BB/KC SMAs, stdev, True Range, Donchian midpoint, linreg input, EMA100, close-vs-prior). No `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d`. The script takes no timeframe input and makes no live `request.*` call, so it is single-frame by construction; `1d` is adopted as the research frame because it is a campaign timeframe — never presented as anything beyond that (see Limitations).
- Warmup: `val` needs 20 valid bars of highest/lowest/SMA (valid from the 20th completed bar); `lowest(val,100)[1]`/`highest(val,100)[1]` need 100 prior valid `val` bars, so the trailing-extreme filter is only full on the 120th completed `1d` bar; EMA100 is full from the 100th bar. Structural minimum is therefore the 120th completed bar; the adopted warmup is the first 150 completed `1d` bars flat (predeclared researcher margin covering EMA seed decay). Pre-warmup bars are flat by language semantics (`na`-gated conditions never open or close anything). No repainting, no negative shift, no future reference, no full-sample normalization; `calc_on_every_tick=false` gives exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT under the house overlay (the rule reads OHLCV geometry only; venue transfer from the prose's stock/index/forex recommendation is never presented as source-native semantics).
- Order timing (predeclared derivation): `process_orders_on_close = true` with `calc_on_every_tick` unset (default false): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester. The source's own timing is next-bar-open (declaration carries no such argument — quoted verbatim in Provenance); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill. Both close legs are whole-position market closes with no stop/limit argument, hence no same-bar TP/SL ordering ambiguity anywhere in the rule; the only ordering specification is the predeclared closes-before-entries atomic evaluation.
- Sizing/capital: the source's `qty=strategy.equity*8/close` line (8x-equity notional as coded, 8%-of-equity as advertised — both disowned) is replaced here by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions, never presented as source-native behavior.
- Concurrency: `pyramiding` is unset (v5 default 0: no same-direction add while positioned; opposite-direction entry reverses). The default is load-bearing and therefore pinned explicitly: repeat trigger bars during an open same-side position are rejected no-ops, and re-entry is allowed immediately on the next qualifying transition after any close (no cooldown specified — explicitly none, not invented). `strategy.close` legs with no matching open position are deterministic no-ops. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The canonical page ships the BB/KC compression construction (lengths 20/20, factors 2.0-advertised/1.5), the linreg momentum definition, the EMA100 gate, the trailing-100-bar extreme filter, the release/transition entries, the momentum-tick exits, the 8% sizing claim, the no-stop risk advice, and the higher-timeframe recommendation. It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=`/`profit=`/`loss=` — the two `strategy.close` momentum-tick legs plus opposite-entry reversal are the sole exit path by construction, and the Risk Management section's stop-loss wishes are explicitly reader-side advice, never rules.
2. Entry legs are mutually exclusive on every bar: the long needs `scolor==gray` while the short needs `scolor==black` on the same bar — no single bar satisfies both, and the transitional `blue` state fires neither, so no same-bar long/short conflict exists to resolve.
3. Exit-leg reachability, proven: `strategy.close('L')` fires on every bar with `val<val[1]` regardless of squeeze state, so a long always has an exit path; the Sell mirror holds. Unlike gate-conditioned exits (cf. the merged TRIX record), no position can be stranded by a regime break — stranding would require momentum to never tick against the position again.
4. Entry/exit co-firing inside one bar resolves conservatively under the predeclared closes-first order: a bar firing both the long close and the long entry first flattens (or no-ops) then opens long — net long, identical to the source's net whenever the source's emulator orders the same two calls on the next open; the Sell mirror yields net short. No transition is invented by the ordering. Note the long entry itself implies `val>val[1]`, which contradicts the long-close condition on the same bar, so a long close+entry co-fire is impossible by construction; only opposite-side close+entry co-fires (e.g. short close via `val>val[1]` on a long-entry bar) can co-occur, and those resolve to the entered side under both orders.
5. Boundary ties and flat ranges fire nothing: strict inequalities throughout (`>`, `<`, strict inside/outside BB-vs-KC); equality on any comparison fires neither entry; a `val` pinned exactly flat fires no close and no entry (`val>val[1]` and `val<val[1]` both false); `na` warmup bars open and close nothing.
6. Flat-state determinism: both `strategy.close` legs with no matching open position are no-ops; same-side repeat triggers while positioned are rejected under pinned pyramiding 0; opposite-side transition triggers reverse; the seed bars satisfy no order condition by themselves (each entry needs a settled prior bar for `scolor[1]`, `val[1]`, `close[1]`, and the trailing extremes).
7. The lengths (20/20/100/100), the factors (effective BB 1.5 via `multKC`, KC 1.5), True-Range KC, the linreg detrending construction, the asymmetric transitions (long on release, short on squeeze-ON), the absent sign tests, the hair-trigger momentum-tick exits, the two-sided direction, reversal semantics, and no-stop/no-target/no-cooldown posture are pinned, not removed: retuning any length, restoring `mult=2.0` to the BB, symmetrizing the short leg to the prose release claim, adding sign tests, adding a stop/target/cooldown/ADX filter, or disabling a side would each be a different, unpinned rule — none is admitted here.
8. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT-`1d` research frame, same-bar-close fills, the closes-first atomic evaluation order, the adopted 150-bar warmup, and house sizing — all predeclared above; every signal, threshold, default, transition, and risk posture is source-verbatim. This record is therefore never evidence that the original next-bar-open multi-market source itself passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: BB20-1.5σ/KC20-1.5×TR compression states / linreg-20 detrended momentum / release-vs-squeeze-ON asymmetric transitions / trailing-100-bar extremes / EMA100 gate / momentum-tick closes / two-sided with reversal / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Compression relevance: dropping the squeeze-state transition (any-bar momentum-plus-EMA100 entries) must not improve net expectancy; fail ⇒ the BB/KC compression test adds nothing over a plain momentum-EMA system.
- F2 — Momentum-exit relevance: replacing the hair-trigger tick closes with opposite-entry-only exits must not improve net expectancy; fail ⇒ the tick closes add nothing over plain reversal trading.
- F3 — Gate relevance: dropping the EMA100-plus-trailing-extreme gates (transition plus momentum direction only) must not improve net expectancy; fail ⇒ the record is a gate-label variant of a plain squeeze-transition system.

## Crypto portability

Pinned to BTCUSDT under the house overlay. The OHLCV-geometry logic ports across perpetual venues without structural change; the short legs require a shortable instrument, so a spot-only deployment cannot express this rule (disabling the short side would be a different, unpinned rule). No funding-dependent leg, no stablecoin-specific assumption, no session, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (`open` is never referenced), so session-gap behavior is simply absent rather than approximated. True Range needs non-degenerate high/low, true of every BTCUSDT bar. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing and frame: the source fills next-bar-open on author-recommended higher timeframes across stocks/indices/forex; this record executes same-bar-close on `1d` BTCUSDT. Backtest economics of the two timings, frames, and venues differ by construction — the adaptations are disclosed, not hidden, and this record makes no claim about the source timing's performance.
- No price stop: adverse excursion after entry has no guardrail beyond the next opposing momentum tick; a vertical-against move exits only when momentum ticks back, which can be far in notional terms on a momentum-persistent spike.
- Hair-trigger exits chop: the same tick-sensitivity that bounds losses will flatten slow-burn winners on the first flat-to-down momentum bar; this is the coded trade, not a tunable parameter here.
- Asymmetric short timing: the short leg enters as compression turns ON (coded), contrary to the prose release story — backtest behavior of the short side will not match a reader's prose-derived expectation, and this record must be read from the code section, never the prose.
- Warmup cost: the adopted 150-bar warmup means the system is blind for the first 150 bars of any 1d evaluation window (structural minimum 120).
- Performance evidence is absent: the canonical page reports no numbers at all (its praise is qualitative prose and timeframe advice); nothing here is calibrated, fitted, or tuned to any backtest.
- Prose-code divergence: the momentum-sign filters, the short-side transition, the BB factor, and the sizing percentage in the prose all disagree with the pinned code in the ways fenced above; future readers must trust the code section, never the prose.

## Implementation status

Not implemented. No Hummingbot controller/executor, no Qlib screening, no Paper/Testnet/Live run has been performed from this record. Admission claims pinned-engine expressibility only (see Execution assumptions), subject to independent six-gate review.

## Adoption boundary

Research-only. Not approved for any downstream screening, parity run, or trading authorization. Only a `PASS` under the live six-gate contract may merge this record into `main`; any `NOT_LOSSLESS` finding closes the PR lane without promotion.

## Related Wiki records

None.

## Sources

- Canonical strategy page (fetched 2026-10-09; prose and full 55-line Pine v5 block read end to end): https://www.tradingview.com/script/G40dtEbK-Squeeze-Momentum-Indicator-Strategy-LazyBear-PineIndicators
- LazyBear indicator lineage page (lineage only, no rule taken): https://www.tradingview.com/script/nqQ1DT5a-Squeeze-Momentum-Indicator-LazyBear/
- Pine v5 strategy semantics (declaration defaults, order calls, close-evaluated execution): https://www.tradingview.com/pine-script-reference/v5/
- Pine strategy concepts: https://www.tradingview.com/pine-script-docs/concepts/strategies/
