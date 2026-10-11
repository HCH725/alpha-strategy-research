---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: KDJ J/D golden-cross long with overbought-rail exit on BTCUSDT 1d bars
created: 2026-10-11
updated: 2026-10-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-02-01
sources:
  - https://www.fmz.com/strategy/440679
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/KDJ%E9%98%B3%E7%BA%BF%E7%AA%81%E7%A0%B4%E4%B9%B0%E5%85%A5%E7%AD%96%E7%95%A5KDJ-Golden-Cross-Long-Entry-Strategy.md
  - https://www.tradingview.com/pine-script-reference/v5/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# KDJ J/D golden-cross long with overbought-rail exit on BTCUSDT 1d bars

## Provenance

Primary source read end to end (immutable public mirror file plus its recorded FMZ canonical page, fetched 2026-10-11):

- Canonical page: https://www.fmz.com/strategy/440679 (fetched live over HTTPS during this cycle with HTTP 200, 770067 bytes of landing HTML). Page-wide token counts: `KDJ` 52, `Golden Cross` 14, `ChaoZhang` 2, `Profit Margin` 6, `Stop Loss Margin` 6, `Futures_Binance` 2, `BTC_USDT` 2. The page embeds the executable `/*backtest*/` header verbatim: `start: 2023-01-25 00:00:00`, `end: 2024-01-31 00:00:00`, `period: 1d`, `basePeriod: 1h`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`. The ZH/EN prose states the rule twice: K = 100 x (close − lowest low over N) / (highest high − lowest low over N), D = M-day moving average of K, J = 3K − 2D; a golden cross (J crossing above D) is the long entry, and J printing above 100 is the long exit (adopted as `source_as_of` 2024-02-01 from the mirror's `> Last Modified` stamp 2024-02-01 10:28:12). Word-boundary counts over the whole landing HTML: `Sharpe` 0, `Win Rate` 0, `Max Drawdown` 0, `Annualized` 0 — the page ships no performance numbers of any kind.
- Immutable mirror actually executed against (primary code source): repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (verified as the repository head via `git ls-remote` during this cycle — the same head pin as the merged KST, Schaff, TRIX, SQZMOM-LB, Aroon, Qstick, Stochastic-OTT, WaveTrend, T3-Tillson and STARC admissions), exact file path `KDJ阳线突破买入策略KDJ-Golden-Cross-Long-Entry-Strategy.md` (non-ASCII filename preserved verbatim; percent-encoded blob URL in Sources). File 8260 bytes, blob SHA `6a99677fadf314b9517d5322972d6467b6871e21` (verified with `git hash-object` reproducing the identical SHA on re-download). The mirror prints `> Author` = `ChaoZhang` (mirror porter), `> Detail` = https://www.fmz.com/strategy/440679, and its `[trans]` prose matches the canonical page rule quoted above. The executable Pine block is titled `strategy('KDJ NVDA', shorttitle='KDJ')` (cited, never redistributed beyond single-line declarations quoted for gate evidence).
- Full `//@version=5` block read in full (order-affecting lines: the `bcwsma` smoother, the RSV/K/D/J chain, the `go_long` edge, one guarded entry, one guarded close; everything else is inputs, the date-window harness, or display-only `plot` x4 feeding no order condition).
- Text census over the pinned code block: 1 `strategy(` (title/overlay plumbing only — no sizing, capital, cost, timing, or pyramiding argument ships anywhere in the declaration) / 1 `strategy.entry` (`"S"`/`strategy.long` inside a single `if (inDateRange and go_long)` guard, no `qty=`/`limit=`/`stop=` qualifiers) / 1 `strategy.close` (`"S"` inside `if (inDateRange and pJ > 100)`) / 0 active `strategy.exit` (exactly one `strategy.exit` line ships commented out — `// strategy.exit("S", limit=c*profit_m, stop=c*stop_m, comment="SL/SP")`, quoted verbatim, never silently activated) / 0 `strategy.order` / 0 active `stop=`/`limit=` / 1 `ta.crossunder` (`go_long = ta.crossunder(pD, pJ)`, the entry edge) / 0 `crossover` / 0 `cross(` / 1 `ta.highest` + 1 `ta.lowest` (the 9-bar RSV window) / 1 `math.avg` (the display-only `KDJ` plot line) / 1 `nz(` (the `bcwsma` recursion seed only) / 0 `volume` / 0 `security(` / 0 `request.*` / 0 `timeframe(` / 2 `time` + 2 `timestamp(` + 1 `syminfo.timezone` (all three inside the `inDateRange` backtest-window harness only — see derived declaration) / 0 `barstate` / 0 `timenow` / 0 `var` / 0 `pyramiding` / 0 `process_orders_on_close` / 0 `calc_on_every_tick` / 0 `max_bars_back` / 0 `initial_capital` / 0 `default_qty` / 0 `commission` / exactly 2 `input(` (`period = 9`, `signal = 3`) + 2 `input.float` (`Profit Margin = 1.20`, `Stop Loss Margin = 0.98`, both consumed only by the commented-out exit) + 6 `input.int` (the date-window harness). No portable economics of any kind ships anywhere — recorded as an absent-economics stub, never as zero-cost evidence.
- Prose/code divergence admitted plainly: the ZH/EN prose claims a stop-profit/stop-loss layer (`采用了止盈止损` / `Adopted stop profit and stop loss`), but the only coded stop/target line is commented out, so the executable rule has no stop and no target. This record follows the code, never the prose, and pins explicitly-no-stop/no-target (see Negative evidence).

Licence and rights: the executable block ships `// ## This source code is subject to the terms of the Mozilla Public License 2.0` via the public FMZ publication; this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly five: (1) market/frame pin `BTCUSDT 1d` (the executable `/*backtest*/` stanza itself backtests `Futures_Binance BTC_USDT` at `period: 1d`/`basePeriod: 1h` — this pin follows the stanza verbatim; only the symbol spelling is normalized, disclosed here, never presented as source-native); (2) removal of the `inDateRange` backtest-window harness gate (a 2023-01-25→2024-01-31 publication-window artifact gating both order lines — dropping a date harness is not dropping signal logic, disclosed here); (3) same-bar-close fills (the source ships no execution-timing argument — Pine default evaluates per completed bar and fills on the next bar; no `process_orders_on_close` ships anywhere, quoted verbatim in census); (4) an adopted 100-bar warmup with pre-warmup bars flat by record rule (covers the 9-bar RSV window plus the recursive `bcwsma` seed with margin — see Required data); (5) house sizing/capital/costs replacing the absent source economics (see Execution assumptions). The RSV/`bcwsma`/J construction, the `9`/`3` inputs, the `ta.crossunder(pD, pJ)` golden-cross edge, the `pJ > 100` rail exit, the long-only stance, the single-position `"S"`-id order path, and the no-stop/no-target posture are source-native and unmodified. No tie-break had to be invented: the entry is an edge detector with a single deterministic outcome per bar, and the exit is a strict inequality (see Negative evidence).

Pre-write dedup (2026-10-11): working-tree case-insensitive searches for `kdj`, `440679`, and `golden-cross-long` return zero hits in any strategy record — no `main` record evaluates a KDJ rule anywhere. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool record `stochastic-ott-dual-trend-btcusdt-1d` is a different mechanism class: Slow-Stochastic %K/%D chained to a dual OTT trailing-stop system (BigCoinHunter, FMZ 432849, its Stochastic confirmation leg disabled by default) — this record trades a Wilder-smoothed KDJ J-line golden-cross edge with a J > 100 overbought-rail exit, long-only, no trailing stop anywhere (ChaoZhang-ported, FMZ 440679). Indicator lineage (J-accelerated KDJ vs raw Stochastic), entry edge (J x D cross vs OTT-stop flips), exit leg (rail close vs trailing-stop system), direction (long-flat vs two-sided), and source identity all differ — not a trivial parameter variant.

## Economic mechanism

### Source-reported

Short-horizon momentum-ignition capture on an accelerating oscillator (mirror prose plus code): the RSV normalizes each close inside its own trailing 9-bar high-low range so the raw position is always a 0–100 rank, the double `bcwsma` smoothing strips single-bar spikes while keeping the turn, and the J line (3K − 2D) re-accelerates the smoothed displacement so the golden cross prints exactly when smoothed momentum bends upward faster than its own average. The design bets that a J-above-D ignition after Wilder-style smoothing marks a durable multi-day upswing rather than a one-bar spike, and that J printing above 100 — the oscillator's own overbought rail — marks the extension as exhausted, so the exit needs no target: the rail, not a level, takes the book flat. There is no short leg, no stop, no target, no flat-holding logic beyond the pre-first-entry flat.

### Research interpretation

Smoothed-ignition long-flat system, edge-triggered, single position. Unlike the Stochastic-OTT record, there is no trend filter, no trailing stop, and no second opinion anywhere: the J/D cross alone opens the book and the J > 100 rail alone closes it, so the system oscillates between exactly one long leg and flat. The entries fire only on the cross bar (an edge, not a latched state — bars that merely hold J above D never trade), which makes chop cheap by construction but strands nothing: a leg whose rail never prints is held until exhaustion or not at all, and alternating cross/rail prints re-enter cleanly because each close returns the book to flat. The commented-out stop/target line is prose aspiration, not executable behavior — the prescribed risk posture is rail-exit-only, disclosed as the principal risk. The bet is on Wilder-smoothed momentum ignition, not on any band break, slope test, volume confirmation, calendar effect, or second timeframe.

## Signal

Exact rule as pinned (`period = 9`, `signal = 3` frozen — any other value is a different, unpinned rule):

- Declarations (derived): single-position long-flat machine over `BTCUSDT 1d` with same-bar-close execution and house sizing/costs (see Execution assumptions). State ∈ {flat, long}; no short state exists anywhere.
- KDJ chain, pinned verbatim: `h(t) = highest(high, 9)`; `l(t) = lowest(low, 9)`; `RSV(t) = 100 x (close(t) − l(t)) / (h(t) − l(t))`; `pK = bcwsma(RSV, 3, 1)`; `pD = bcwsma(pK, 3, 1)`; `pJ = 3 x pK − 2 x pD`, where `bcwsma(s, l, m) = (m x s + (l − m) x nz(prior, 0)) / l` (so each smoothing stage is a 1/3-weight Wilder-style recursion seeded at 0). The `math.avg(pD, pJ, pK)` line is display-only and drives no order.
- Entry edge, pinned verbatim: `go_long(t) = crossunder(pD, pJ)(t)` — true on exactly the bar where pD passes from above to below pJ, i.e. the J-line golden cross above the D line. From flat, that bar opens `strategy.entry("S", strategy.long)`; from long (no pyramiding ships anywhere, and the book can only be flat-or-long) no additive exposure can print. Mere holding bars with J above D satisfy no edge and never trade.
- Exit rail, pinned verbatim: `pJ(t) > 100` → `strategy.close("S")` to flat. Strict inequality: a print of exactly 100 holds the leg. No stop, no target, no trailing, no time exit, no cooldown — pinned as written (the only coded stop/target line is commented out, quoted verbatim in Provenance), explicitly none, not invented.
- Direction: long-only with resting flat. A short leg would contradict the order block (the sole entry leg is `strategy.long` and the sole close leg closes `"S"`); long-only is prescribed, explicitly, never a researcher restriction.

## Required data

- Completed `1d` bars of BTCUSDT: `close` (RSV rank source), `high`/`low` (the trailing 9-bar RSV window only — no order-gating line reads them directly). No `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (derived pin following the stanza's own `period: 1d`; the body contains no `security(`/`request.*` call, so the derived rule is single-frame by construction).
- Warmup: the binding seed is the double `bcwsma` recursion (per-stage time constant ≈ 3 bars, negligible) behind the 9-bar RSV window; the na-propagation fence (see Negative evidence) already blocks any seeded value from trading. The adopted warmup is the first 100 completed `1d` bars flat by record rule (predeclared researcher choice — covers the window plus seed with two orders of margin; no traded bar reads a seeded value). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. Each bar's OHLC enters the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (derived pin following the executable header's own `Futures_Binance BTC_USDT` venue at `period: 1d` — venue transfer and symbol spelling are disclosed here, never presented as source-native). The rule is long-flat with no short leg, so a spot deployment expresses the full rule; no futures-only assumption is needed — disclosed.
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar fill (no execution-timing argument ships anywhere — quoted verbatim in census); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity, and the entry edge and the exit rail evaluate on the same completed close with deterministic precedence (an exit rail and a fresh cross on the same bar resolve flat-first by the shipped line order — entry `if` precedes exit `if`, and with no position a same-bar rail print is a no-op close; each bar's outcome is a single deterministic event: open, hold, close, or no-op).
- Sizing/capital/costs: the source ships no portable economics of any kind (no `initial_capital`, no `default_qty`, no commission/slippage/funding argument ships anywhere — recorded as an absent-economics stub, never as zero-cost evidence) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: single-position machine by single-id-plus-default construction — at most one `"S"` long leg; the cross edge cannot stack exposure (no `pyramiding` ships anywhere and only flat admits the entry); the rail close returns the book to flat; re-entry is allowed on the next fresh golden cross after any close (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The mirror ships the full construction (9-bar RSV window, double `bcwsma(., 3, 1)` smoothing, J = 3K − 2D, the `ta.crossunder(pD, pJ)` golden-cross edge, the `"S"` long entry, the `pJ > 100` rail close, the commented-out stop/target line, and the `/*backtest*/` stanza (2023-01-25→2024-01-31, `Futures_Binance BTC_USDT`, `period: 1d`/`basePeriod: 1h`)), plus the prose rule statement — quoted in Provenance. It ships no portable performance: no table, no figure, no metric — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden risk layer: the body contains zero active `strategy.exit` legs and zero `stop=`/`limit=` qualifiers; the single candidate stop/target line is commented out and quoted verbatim. The no-stop/no-target posture is prescribed, explicitly none, never hidden — and the prose's stop-profit/stop-loss claim is fenced as prose-only, never executed.
2. Edge-not-latch fenced: the entry is `ta.crossunder` (fires only on the cross bar), not a `J > D` holding state — post-cross bars with J still above D satisfy no entry guard, so no priority rule against the exit rail is needed beyond the shipped line order, and no bar can open twice.
3. Flat-first same-bar precedence stated plainly: entry `if` precedes exit `if` in the shipped order; with the book flat a same-bar `pJ > 100` print closes nothing, and with the book long a same-bar fresh cross cannot stack (no pyramiding ships anywhere). Every bar resolves to one deterministic event — no researcher precedence invented.
4. Zero-range and na determinism fenced: a zero-range 9-bar window (`h == l`) makes RSV `na`, which propagates through `bcwsma`/`pJ` so both the cross edge and the rail test resolve false — the bar holds by Pine na semantics, never by a researcher tie-break; combined with the record-rule 100-bar warmup flat, no seeded value ever trades.
5. Rail-boundary determinism fenced: `pJ > 100` is strict — exactly 100 holds the leg. The outcome falls directly out of the quoted operator; no alternative reading.
6. `bcwsma`-seed fence, stated plainly: `nz(prior)` with no default seeds each recursion at 0, and while any input is `na` the comparisons cannot print an edge — the seed shapes only the first few smoothed values, all inside the warmup flat.
7. Date-harness removal fenced: the dropped `inDateRange` gate reads `time`/`timestamp(`/`syminfo.timezone` — all three census-counted above and none of them feeds any indicator, edge, or rail. Removing the publication-window gate changes which calendar bars are eligible, never how any eligible bar is judged — disclosed, not hidden.
8. No future leakage in the stack, stated plainly: at decision bar `t` the slowest input is the 9-bar high/low window resolving at bar `t`'s close — every input is complete at the close. No `security()`, no `request.*`, no negative index, no `barstate`-gated path. All four `plot` calls render only and drive no order.
9. Long-only posture provably complete: the sole entry leg is `strategy.long` and the sole close leg closes `"S"` — no short state is reachable under the shipped declaration. Any two-sided reading would contradict the code and is explicitly not this record.
10. Derivation boundary fenced: the only non-source-native behaviors in this record are the `BTCUSDT 1d` market/frame pin, the dropped date harness, same-bar-close fills, the adopted 100-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the RSV/`bcwsma`/J construction, the `9`/`3` inputs, the golden-cross edge, the `"S"`-id order path, the rail exit, the long-only stance, and the risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, or timing of the source passes.
11. Network limitation disclosed: every formula line above was byte-verified in the pinned mirror file at commit `7853bb2` (8260 bytes, blob SHA recorded, `git hash-object` identical on re-download); the FMZ canonical page verified live the title, the `ChaoZhang` token, the `Golden Cross` rule prose, the `Profit/Stop Loss Margin` inputs, the `Futures_Binance BTC_USDT` backtest stanza, and the absence of any performance numbers — the division of evidence is disclosed here, not hidden.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: RSV(9) / double-`bcwsma(., 3, 1)` / J = 3K − 2D / `crossunder(pD, pJ)` edge / `pJ > 100` rail exit / no-stop-no-target posture / long-flat / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — J-acceleration relevance: replacing the J/D golden-cross trigger with a plain K/D golden-cross (same 9/3 smoothing, same rail exit) must not improve net expectancy; fail ⇒ the J-line acceleration adds nothing over the smoothed K/D cross.
- F2 — Rail-exit relevance: replacing the J > 100 rail exit with holding until the next opposite J/D cross (cross-to-cross holding, same trigger) must not improve net expectancy; fail ⇒ the overbought rail adds nothing over cross-to-cross holding.
- F3 — Fast-specification relevance: replacing the 9/3 pair with a slow 14/5 KDJ reading (same trigger, same rail) must not improve net expectancy; fail ⇒ the pinned fast specification adds nothing over a slow reading of the same oscillator.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (derived pin following the executable header's own `Futures_Binance BTC_USDT` venue at `period: 1d`). The RSV/`bcwsma` arithmetic ports across perpetual venues without structural change, but venue bar-construction differences touch `high`/`low` and hence the 9-bar window, every smoothed value, and every edge/rail test — disclosed above, not hand-waved. The rank normalization auto-scales in the asset's own price units, so no fixed-pip recalibration is needed across assets — cross-asset behavior differences are still real and unclaimed. The rule is long-flat with no short leg, so a spot deployment expresses the full rule — no futures-only assumption, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no session gating anywhere after the harness removal); decision boundaries are calendar-day bars of the venue feed, disclosed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source fills next-bar with no timing argument; this record executes same-bar-close on `1d` BTCUSDT. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- Derived market and frame: the stanza backtests `Futures_Binance BTC_USDT` at `1d`; this record pins `BTCUSDT 1d` with normalized symbol spelling. Cross-market and cross-frame behavior differences are real — the adaptation is disclosed, and this record makes no claim about any other market, frame, or the stanza's `1h` base period.
- Dropped date harness: the 2023-01-25→2024-01-31 `inDateRange` gate is removed as a publication-window artifact. Eligible calendar history differs from the stanza window by construction — disclosed, and no stanza-window performance is claimed anywhere.
- Rail-exit commitment: after entry the book's only guardrail is the J > 100 rail; adverse excursion with J pinned mid-range has no stop beyond the rail, and a leg whose rail never prints is held indefinitely. This is the prescribed posture (the coded stop/target line is commented out), disclosed as the principal risk — not smoothed, not supplemented.
- No source economics: beyond the bare `strategy(...)` title plumbing the source ships no capital, sizing, commission, slippage, funding, or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Seed coverage: the 9-bar window plus double recursion settle within a handful of bars; the first 100 `1d` bars are flat by record rule, so early-history signals never enter any evaluation.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- FMZ canonical strategy page (rule prose plus `Futures_Binance BTC_USDT` 1d backtest stanza verified live via HTTP-200 page record): https://www.fmz.com/strategy/440679
- Immutable mirror file at pinned commit `7853bb2bf262c4567ac238d3552d97f0e50cb801` (blob `6a99677fadf314b9517d5322972d6467b6871e21`, 8260 bytes): https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/KDJ%E9%98%B3%E7%BA%BF%E7%AA%81%E7%A0%B4%E4%B9%B0%E5%85%A5%E7%AD%96%E7%95%A5KDJ-Golden-Cross-Long-Entry-Strategy.md
- Pine strategy semantics (order calls, default execution, built-in `ta.highest`/`ta.lowest`/`ta.crossunder` semantics): https://www.tradingview.com/pine-script-reference/v5/
