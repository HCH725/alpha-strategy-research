---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Chande Kroll Stop ADX-gated reversal two-sided on BTCUSDT 1d bars
created: 2026-10-11
updated: 2026-10-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2022-05-09
sources:
  - https://www.fmz.com/strategy/362031
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/Chande-Kroll-Stop.md
  - https://www.tradingview.com/pine-script-reference/v5/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Chande Kroll Stop ADX-gated reversal two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (immutable public mirror file plus its recorded FMZ canonical page, fetched 2026-10-11):

- Canonical page: https://www.fmz.com/strategy/362031 (fetched live over HTTPS during this cycle with HTTP 200, 736887 bytes of landing HTML). Author token `ChaoZhang` × 2; prose describes the Chande Kroll stop pair (blue long-stop line, orange short-stop line) with close-cross signals plus an optional ADX chop filter (`Chande` 8, `Kroll` 7 on the page). Word-boundary counts over the whole landing HTML: `Sharpe` 0, `Win Rate` 0, `Max Drawdown` 0, `Annualized` 0, `Profit Factor` 0, `Take profit` 0, `Stop Loss` 0 — the sole `return` token is site-chrome JavaScript, not a performance figure. The page ships no performance numbers of any kind.
- Immutable mirror actually executed against (primary code source): repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (verified as the repository head via `git ls-remote` during this cycle — the same head pin as the merged Heikin-Ashi, Bollinger, PVT-EMA, KDJ, STARC, T3-Tillson, WaveTrend, Qstick, Aroon, SQZMOM-LB, TRIX, Schaff, KST, OBV-EMA and further admissions), exact file path `Chande-Kroll-Stop.md` (pure-ASCII filename, no encoding ambiguity). File 2166 bytes, blob SHA `23b56b88ee0e3833de9c13e0dbec64adf45e9f46` (verified with `git hash-object` reproducing the identical SHA on re-download, and matching the GitHub contents API `sha`/`size` at the pinned commit). The mirror prints `> Author` = `ChaoZhang`, `> Detail` = https://www.fmz.com/strategy/362031, `> Last Modified` = `2022-05-09 17:44:31` (date part adopted as `source_as_of`), the English prose quoted below, and the six-row Strategy Arguments table (`p = 10`, `x` row, `q = 9`, `ADX Smoothing = 14`, `DI Length = 14`, `minimum ADX threshold = 20`) matching the code defaults line for line except one disclosed porter artifact (see Negative evidence).
- Full `//@version=5` block read in full (order-affecting lines: the two first-stop declarations, the two `ta.highest`/`ta.lowest` stop-smoothing lines, the `dirmov`/`adx` custom-function block, and the two `if … and sig>ADX_sig` order lines; the two `plot(` calls are visual only and gate no order).
- Text census over the pinned code block: 1 `strategy(` (`Chande Kroll Stop`/`overlay=true` plumbing only) / 0 `study(` / 0 `indicator(` / 2 `strategy.entry` (`"long"`/`strategy.long`, `"short"`/`strategy.short`, no `qty=`/`limit=`/`stop=`/`when=` qualifiers) / 0 `strategy.exit` / 0 `strategy.order` / 0 `strategy.close` / 0 active `stop=`/`limit=`/`profit=`/`loss=` / 1 `ta.crossover` / 1 `ta.crossunder` / 2 `plot(` (visual only) / 2 `ta.highest` / 2 `ta.lowest` / 2 `ta.atr` / 4 `ta.rma` (the full Wilder smoothing stack) / 2 `ta.change` / 0 `request.security` / 6 `input` (4 `input.int`: 10, 1, 9, 20; plus 2 inferred-int `input(14, …)` ADX lengths) / 0 `pyramiding` / 0 `process_orders_on_close` / 0 `initial_capital` / 0 `commission` / 2 `na(` (the `na(up) ? na : …` seeding guards inside `dirmov`, deterministic, disclosed) / 0 `nz(` / 0 `barstate` / 0 `lookahead` / 0 bare `open` / 0 `volume`. `high`/`low` enter only through the stop/ADX construction; `close` enters only through the two cross tests. No portable economics beyond the two bare order calls ships anywhere — recorded as an absent-economics stub, never as zero-cost evidence.
- Licence and rights: the mirror file carries no licence header of its own; this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly four: (1) market/frame pin `BTCUSDT 1d` (the source ships no backtest stanza pinning a venue or frame — venue transfer, symbol spelling and frame choice are disclosed here, never presented as source-native); (2) completed-bar decisions with same-bar-close fills (the source ships no `process_orders_on_close` argument — Pine default would fill later; this record's timing is a predeclared derivation, disclosed here); (3) an adopted 300-bar warmup with pre-warmup bars flat by record rule (covers the ATR/RMA seeds plus the 10+9 stop windows plus the double RMA-14 ADX stack with margin — see Required data); (4) house sizing/capital/costs replacing the absent source economics (see Execution assumptions). The `10`/`1`/`9`/`14`/`14`/`20` inputs, the two-stage stop construction, the custom Wilder ADX gate, the `and sig>ADX_sig` conjunctions, the `"long"`/`"short"` order paths, the two-sided reversal stance, and the no-stop/no-target posture are source-native and unmodified. The prose/code side-mapping conflict is fenced in Negative evidence and resolved code-verbatim — no tie-break was invented beyond following the executable artifact.

Pre-write dedup (2026-10-11): working-tree case-insensitive filename search for `kroll` returns no strategy record, and no record cites FMZ page `362031` or mirror file `Chande-Kroll-Stop.md`. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool relatives: `chande-momentum-80-cross` (Chande Momentum Oscillator level-cross — a bounded momentum oscillator, no stop lines, no ADX gate), `chandelier-exit` open PR #89 (single highest-high/lowest-low ATR trailing-stop flip — no two-stage highest/lowest smoothing of first-stop lines, no ADX conjunction), and `dmi-swings-contrarian-adx` (DMI-swing contrarian — no stop-line cross events). None computes the `highest(highest(high,p)−x·ATR(p),q)` / `lowest(lowest(low,p)+x·ATR(p),q)` stop pair gated by a custom Wilder ADX threshold. Not a trivial parameter variant.

## Economic mechanism

### Source-reported

Two-stage ATR stop sandwich with a trend-strength gate (prose plus code): the first stop pair sits one ATR(10) inside the 10-bar extremes (`highest(high,10) − ATR(10)` below, `lowest(low,10) + ATR(10)` above), then each leg is smoothed again over 9 bars (`highest` of the high leg, `lowest` of the low leg) so the printed blue/orange lines hug developing trends and only yield on genuine extension. A close crossing through a stop line is the event; the custom Wilder ADX(14,14) > 20 conjunction mutes both legs in chop ("filter using ADX to minimize getting rekt in a choppy market"). The design bets that ADX-confirmed stop-line violations mark real regime shifts rather than noise; it ships no stop, no target, and no flat state — the book always carries the last gated signal.

### Research interpretation

Gated two-event reversal machine, edge-triggered, two-sided. Unlike state-latch records (Heikin-Ashi EMA color latch, RAVI threshold latch) there is no standing state re-asserted every bar: orders print only on the two cross events, each strictly conjunction-gated by `sig > 20`, so most bars print nothing and the book rests. Unlike single-stop flip systems (Chandelier #89, PSAR, SuperTrend #63) the trigger lines are doubly smoothed (extreme-window plus second max/min window) and neither leg can fire without the ADX gate — chop braids price through the lines without printing, which is the coded cost control. Unlike oscillator-cross records (CMO-80, Fisher zero-cross) the trigger is a price-through-derived-stop event, not a level crossing of a bounded oscillator. The bet is on ADX-confirmed stop-line violation as regime-shift evidence under a 10/1/9 stop stack, not on any price level, band penetration, single trailing stop, slope test, calendar effect, or second timeframe.

## Signal

Exact rule as pinned (`p = 10`, `x = 1`, `q = 9`, `adxlen = 14`, `dilen = 14`, `ADX_sig = 20` frozen — any other value is a different, unpinned rule):

- Declarations (derived): two-sided reversal machine over `BTCUSDT 1d` with same-bar-close execution and house sizing/costs (see Execution assumptions). State ∈ {flat, long, short}; flat exists only before the first post-warmup order; at most one unit is ever held.
- Stop construction, pinned verbatim: `first_high_stop = ta.highest(high, 10) - 1 * ta.atr(10)`; `first_low_stop = ta.lowest(low, 10) + 1 * ta.atr(10)`; `stop_short = ta.highest(first_high_stop, 9)` (orange); `stop_long = ta.lowest(first_low_stop, 9)` (blue).
- ADX gate, pinned verbatim: custom Wilder block — `dirmov(14)` builds `plusDM`/`minusDM` from `ta.change(high)`/`ta.change(low)` with the `na(up) ? na : …` seeding guards, smooths with `ta.rma(…, 14)` against `ta.rma(ta.tr, 14)`; `adx(14, 14)` returns `100 * ta.rma(abs(plus − minus) / (sum == 0 ? 1 : sum), 14)`; `sig` is that value and every order requires `sig > 20` (strict, pinned as written — equality does not fire).
- Orders, pinned verbatim (code governs; prose conflict fenced below): `if ta.crossunder(close, stop_long) and sig > ADX_sig` → `strategy.entry("long", strategy.long)`; `if ta.crossover(close, stop_short) and sig > ADX_sig` → `strategy.entry("short", strategy.short)`, evaluated on every completed bar. From flat the first gated event opens; from the same side the call is a no-op under the default no-pyramiding construction (no `pyramiding` argument ships anywhere); from the opposite side the call reverses the full unit in one step — reversal is the sole exit path, with no separate exit leg (zero `strategy.exit`/`strategy.close` legs anywhere). Both `if` lines are independent (no `else`), so a bar printing both crosses would attempt both entries in written order — disclosed; under single-unit no-pyramiding construction the second call resolves against the position left by the first, never stacking.
- Exits and risk, pinned verbatim: there are none besides reversal — zero `strategy.exit`/`strategy.close` legs, zero `stop=`/`limit=`/`profit=`/`loss=` qualifiers anywhere. No take-profit, no trailing, no time exit, no flat signal — pinned as written, explicitly none, not invented.
- Direction: two-sided with resting exposure. A long-only reading would contradict the `"short"`/`strategy.short` leg and is explicitly not this record.

## Required data

- Completed `1d` bars of BTCUSDT: `high`, `low`, `close` only (the 10-bar extremes, the ATR(10), the Wilder ADX stack, and the two close-cross tests; no bare `open` series is read by any code line, and no `volume`, funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read anywhere).
- Single decision timeframe `1d` (derived pin; zero `request.security` calls ship anywhere, so no second evaluated frame exists by construction).
- Warmup: the binding seed stack is ATR RMA-10 plus the 10-bar extremes feeding the 9-bar second smoothing window, plus the Wilder ADX double RMA-14 stack (each RMA-14 needs its own seed run). The adopted warmup is the first 300 completed `1d` bars flat by record rule (predeclared researcher choice — an order of magnitude beyond the ~40-bar structural seed with margin; no traded bar reads a seeded value). The `na(up) ? na : …` guards keep early `plusDM`/`minusDM` (and hence `sig`) `na`-seeded, and `na > 20` is false, so pre-warmup bars structurally cannot fire — the warmup absorbs the seed stack twice over, disclosed, never a researcher tie-break. No repainting, no negative shift, no future reference, no full-sample normalization, no `lookahead`, no `barstate`-gated order path; one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (derived pin; the source ships no venue/frame stanza, so venue transfer, symbol spelling and frame choice are disclosed here, never presented as source-native). The short leg needs a venue with short permission; futures satisfies this — disclosed.
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source ships no `process_orders_on_close` argument — Pine default would fill later; this record claims no source-native timing and no intrabar behavior. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere and at most the two written `if` events per bar, same-bar ordering follows written order, disclosed.
- Sizing/capital/costs: the source ships no portable economics of any kind (no capital amount, no commission/slippage/funding/margin argument ships anywhere — recorded as an absent-economics stub, never as zero-cost evidence) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: single-unit machine by default no-pyramiding construction — at most one unit long or short; same-side re-assertion prints nothing. No cooldown ships anywhere (explicitly none, not invented). No flat state is reachable after the first post-warmup order except by reversal; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The mirror ships the full construction (the `10`/`1`/`9`/`14`/`14`/`20` inputs, the two first-stop lines, the two second-window smoothing lines, the two `plot(` calls, the custom `dirmov`/`adx` Wilder block, the two `if … and sig>ADX_sig` order lines, the author stamp, the six-row arguments table, and the English prose describing the blue/orange stop lines with the ADX chop filter). It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden risk layer: the body contains zero `strategy.exit`/`strategy.close` legs and zero `stop=`/`limit=`/`profit=`/`loss=` qualifiers. The no-stop/no-target reversal-only posture is prescribed, explicitly none, never hidden.
2. Prose/code side-mapping conflict, resolved code-verbatim: the prose assigns the short signal to a cross under the orange (`stop_short`) line and the long signal to a cross over the blue (`stop_long`) line, while the executable lines pair `crossunder(close, stop_long)` with the `"long"`/`strategy.long` order and `crossover(close, stop_short)` with the `"short"`/`strategy.short` order. This record follows the executable artifact exactly as written and discloses the prose mismatch here — the reviewer can verify both sentences against the pinned file. No side was swapped to match the prose; no arbitration rule was invented.
3. Arguments-table artifact fenced: the table row for `x` prints its Default as `true` while the executable line pins `input.int(1, minval=1)`; this record follows the code (`x = 1`) and discloses the table artifact. All other rows (10, 9, 14, 14, 20) match their code lines exactly.
4. No third order path: the only order legs are the two written `if` lines — every bar resolves to zero, one, or (only if both crosses printed on one bar) the two written events in written order, so no precedence or cooldown rule was invented beyond written order under single-unit construction.
5. `>` strictness fenced: the gate is `sig > ADX_sig` — exact equality at 20 does not fire. A `>=` reading would contradict the code and is explicitly not this record.
6. `na`-guard behavior fenced: the `na(up) ? na : …` / `na(down) ? na : …` guards (2 `na(` hits, both inside `dirmov`) keep early Wilder inputs `na`, and `na > 20` never fires — the adopted 300-bar flat absorbs the entire seed stack structurally, so no seeded value ever trades. Structural, disclosed, never a researcher tie-break.
7. Single-frame fenced: zero `request.security` calls ship anywhere — there is no MTF pull, no cross-symbol pull, and no `lookahead`. Every input (`highest`/`lowest`/`atr`/`change`/`rma`) is a causal function of completed bars inclusive of the decision bar, computable point-in-time with no future leakage — stated plainly.
8. Visual-only plots fenced: the two `plot(` calls print the blue/orange lines and gate no order — a reader mistaking a plot touch for a signal would contradict the census. The signal is the `close`-through-line cross pair, nothing else.
9. Order-id completeness fenced: the sole long id is `"long"` and the sole short id is `"short"` — with no pyramiding anywhere there is at most one unit to reverse, so the opposite-side `strategy.entry` provably flattens-and-reopens in one step. No partial-fill residue is reachable by code.
10. Derivation boundary fenced: the only non-source-native behaviors in this record are the `BTCUSDT 1d` market/frame pin, completed-bar same-bar-close fills, the adopted 300-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the `10`/`1`/`9`/`14`/`14`/`20` inputs, the two-stage stop pair, the custom Wilder ADX construction, the strict `>` gate, the two `if` order lines, single-unit no-pyramiding state, the two-sided reversal stance, and the risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, parameter set, or timing of the source passes.
11. Network limitation disclosed: every formula line above was byte-verified in the pinned mirror file at commit `7853bb2` (2166 bytes, blob SHA recorded, `git hash-object` identical on re-download, contents-API `sha`/`size` matched); the FMZ canonical page verified live the title, the `ChaoZhang` token, the Chande Kroll stop prose with the ADX filter sentence, and the absence of any performance numbers — the division of evidence is disclosed here, not hidden.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `10` / `1` / `9` / Wilder ADX `14`/`14` / gate `20` / two-stage stop pair / strict `>` conjunction / `"long"`/`"short"` order pair / no-stop-no-target posture / two-sided single-unit / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Stop-smoothing relevance: replacing the second smoothing window (`highest`/`lowest` over 9 of the first-stop lines) with the raw first-stop lines (same 10/1 legs, same ADX gate, same risk posture) must not improve net expectancy; fail ⇒ the second smoothing layer adds nothing over the single-stage stops.
- F2 — ADX-gate relevance: removing the `sig > 20` conjunction (firing both cross legs raw, same stops, same risk posture) must not improve net expectancy; fail ⇒ the Wilder ADX gate adds nothing over ungated stop-line crosses.
- F3 — Stop-width relevance: replacing the `x = 1` ATR multiple with `x = 3` (same windows, same gate, same risk posture) must not improve net expectancy; fail ⇒ the pinned one-ATR stop hug adds nothing over a wider stop pair.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (derived pin; the source ships no venue stanza). The extremes-plus-ATR arithmetic ports across perpetual venues without structural change — no volume read means venue volume-reporting differences touch nothing, disclosed as a robustness property, not a portability proof. The two-sided stance requires a short-capable venue (futures satisfies this); a spot deployment would express only the long half and is a different, unpinned claim. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no session gating anywhere); decision boundaries are calendar-day bars of the venue feed, disclosed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source ships no `process_orders_on_close` argument; this record executes completed-bar same-bar-close on `1d` BTCUSDT and claims no source-native timing. Backtest economics of the timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about any other timing's performance.
- Derived market and frame: the source ships no venue/frame stanza; this record pins `BTCUSDT 1d`. Cross-market and cross-frame behavior differences are real — the adaptation is disclosed, and this record makes no claim about any other market or frame.
- Prose/code side-mapping conflict: followed code-verbatim and fenced above — a reader trusting only the prose sentences would assign each line to the opposite side. The conflict is disclosed, not smoothed.
- Reversal-only risk: there is no flat signal and no stop — adverse excursion reverses only on the next opposite gated cross, an ungated drift through one line prints nothing while ADX reads soft, and whipsaw under alternating gated crosses is the coded cost of the design, disclosed, not smoothed, not supplemented.
- No source economics: the source ships no capital amount, commission, slippage, funding, or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Seed coverage: the ATR/RMA/double-window seed stack settles within dozens of bars; the first 300 `1d` bars are flat by record rule, so early-history signals never enter any evaluation.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- FMZ canonical strategy page (Chande Kroll stop prose plus ADX-filter sentence verified live via HTTP-200 page record): https://www.fmz.com/strategy/362031
- Immutable mirror file at pinned commit `7853bb2bf262c4567ac238d3552d97f0e50cb801` (blob `23b56b88ee0e3833de9c13e0dbec64adf45e9f46`, 2166 bytes): https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/Chande-Kroll-Stop.md
- Pine strategy semantics (v5 order calls, `ta.highest`/`ta.lowest`/`ta.atr`/`ta.rma`/`ta.change`/`ta.crossover`/`ta.crossunder` built-ins): https://www.tradingview.com/pine-script-reference/v5/

