---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Wick reversal hammer/shooting-star momentum-context long-flat on BTCUSDT 1d bars
created: 2026-10-16
updated: 2026-10-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-09-02
sources:
  - https://github.com/hasnocool/tradingview-pine-scripts/blob/e031cab2819a7d56fb8bb9d000252f51439986e2/Wick%20Reversal.pine
  - https://in.tradingview.com/script/Yl9lDJxU-Wick-Reversal/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Wick reversal hammer/shooting-star momentum-context long-flat on BTCUSDT 1d bars

## Provenance

Primary source read end to end (pinned immutable GitHub file, live raw fetch 2026-10-16 at pin):

- Canonical file: https://github.com/hasnocool/tradingview-pine-scripts/blob/e031cab2819a7d56fb8bb9d000252f51439986e2/Wick%20Reversal.pine (repo `hasnocool/tradingview-pine-scripts`, file commit `e031cab2819a7d56fb8bb9d000252f51439986e2` dated 2023-09-02 — the sole commit touching this path; record `source_as_of` is that commit date, never the fetch date. Script author `OHM_INSTITUTIONAL_BROKING`; TradingView canonical page `Wick Reversal — Strategy by OHM_INSTITUTIONAL_BROKING`, script id `Yl9lDJxU`: https://in.tradingview.com/script/Yl9lDJxU-Wick-Reversal/ — the page description ships the whole thesis in one sentence: "Hi the given strategy is based on detecting hammer and shooting star patterns to trade early reversals.")
- Pinned blob SHA `21e5676347d4e3e75bfc707164f132b399a89689`, 1697 bytes on disk; the copy fetched at the pinned commit is byte-identical to the copy inspected, SHA-256 `24ec93eb2533544749fcf23dc2517f87f400a3b0b8fb60e0c4fe0965056b6afa`.
- The file is a TradingView page scrape whose embedded verbatim Pine v4 block is the complete 21-line program (`Expand (35 lines)` covers the header plus every code line; `//@version=4`, `strategy("Wick Reversal", shorttitle="wickreversal", overlay=true, pyramiding=1)` — a real executable `strategy(`, not an indicator). Full census of the pinned bytes: 1 `strategy(` / 0 `study(` / 0 `indicator(` / 1 `strategy.entry` (`"BUY"`, `strategy.long`) / 1 `strategy.close` (`"BUY"`) / 0 `strategy.exit` / 0 `strategy.order` / 0 `strategy.close_all` / 0 `strategy.short` / 0 `crossover` / 0 `crossunder` / 0 `ta.*` (v4 bare builtins) / 0 `request.*` / 0 `security(` / 0 `process_orders_on_close` (language default governs, recorded as source-declared-by-default) / 0 `calc_on_every_tick` / 0 `initial_capital` / 0 `default_qty` / 0 `commission` / 0 stop/limit/profit/trail reads of any kind / 6 `input(` (all date-window: From/To Month/Day/Year).
- State rule read verbatim: `buySignal = ((close/close[15])-1)<-0.05 and (min((close[1]-low[1]),(open[1]-low[1]))>((high[1]-low[1])/2)) and low > low[1]` → `strategy.entry("BUY", strategy.long, when=window())`; `sellSignal = ((close/close[15])-1)>0.05 and (min((high-close),(high-open))>((high-low)/2))` → `strategy.close("BUY", when=window())`. No other order path exists. `window()` under shipped defaults spans 1000-01-01 to 9999-01-01 (`FromYear=1000`, `ToYear=9999`), so every real bar passes — no cherry-picked sample is baked in, recorded as source-declared-by-default.
- The TradingView page itself was not opened this run (extraction backend unnecessary); the pinned file's embedded verbatim block carries every gate fact, and the TV URL is fenced as lineage/identity-only.

Licence and rights: the embedded block carries no licence header. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly four: (1) research market BTCUSDT Binance spot `1d` (the pinned rule names no market, venue, or timeframe in-code; long-only needs no margin, so spot is the minimal realistic venue — no source-market equivalence is claimed); (2) an adopted 100-bar warmup with pre-warmup bars flat by record rule (structural minimum is the 16th completed bar — see Required data); (3) an explicit single-unit pin with repeat signals while long as no-ops (the file codes `pyramiding = 1` explicitly; to the extent that setting would permit an additional same-direction unit on a repeated signal, that add is excluded by record rule — predeclared, never silent); (4) house sizing/capital/costs replacing the wholly absent source economics (see Execution assumptions). The 15-bar ±5% momentum context, the half-range wick fractions, the higher-low confirmation, the next-open fill convention under the language default, the always-true window under shipped defaults, the long-only stance, and the no-risk-leg posture are source-verbatim or source-declared-by-default.

Pre-write dedup (2026-10-16): working-tree case-insensitive filename search for `wick`, `hammer`, `shooting`, `marubozu`, `pinbar`, `pin-bar`, `doji` returns zero strategy records trading those signals (`hammer`/`shooting`/`marubozu` have zero content hits pool-wide; `doji`/`wick` hits are fencing prose inside otherwise-named records — e.g. the soldiers record's anti-doji filter and the engulfing record's wick discussion, never order-gating lines; `close[15]` has zero hits). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Closed-unmerged PR #220 (TA-Lib morning-star/evening-star gap-penetration flip two-sided, never in `main`) trades 3-bar gap-penetration star patterns two-sided — different pattern construction (3-bar gap stars vs 1-bar wick plus 15-bar momentum context), different book (two-sided flip vs long-flat), different source. Closest pool records differ in mechanism class (see Negative evidence 6). This is a new family, not a parameter variant: no pool record computes wick-dominance fractions or trades this event.

## Economic mechanism

### Source-reported

Early-reversal capture off single-bar rejection wicks: a hammer printed after a sold-off stretch (15-bar return below −5%) with a higher low evidences capitulation plus stabilization, so the rule goes long; a shooting star printed after an extended stretch (15-bar return above +5%) evidences exhaustion, so the rule stands aside to flat. The author claims no channel beyond the pattern thesis itself ("detecting hammer and shooting star patterns to trade early reversals") — no behavioural, structural, or risk-premium mechanism ships in-source.

### Research interpretation

Sold-off-hammer plus higher-low confirmation long, overbought-shooting-star flat — a pure price-action reversal timer on a momentum context gauge. Unlike every indicator record in the pool, the rule never smooths, never normalizes through an oscillator, and never votes across stacked averages: the event is wick geometry (lower wick over half the prior range; upper wick over half the current range) gated by a 15-bar close-to-close return. Unlike the multi-candle pattern records (soldiers' three-body sequence, engulfing's two-bar coverage, consecutive-run counts, fractal swings), the trigger is one bar's wick fraction, and the context is a return threshold, not a count or a swing structure. The failure mode is made plain: with no stop, no trailing, and no regime filter, a hammer that marks only a pause in a waterfall realizes the full further excursion until a shooting star prints — the shooting-star close is an exhaustion guillotine, not risk control.

## Signal

Exact rule as pinned (15-bar lookback / ±5% / half-range wick / higher-low frozen — any other tuple is a different, unpinned rule):

- Declaration (source-native): Pine v4 program (`//@version=4`) with v4 semantics observed. Bare `open`/`high`/`low`/`close` builtins only (0 `ta.*`, 0 `request.*` / 0 `security(`). The `overlay=true` display flag and `shorttitle="wickreversal"` gate no order. The single-side stance is source-coded: no short leg exists anywhere.
- Entry long (pinned, source-verbatim): prior-bar hammer plus sold-off context plus higher-low confirmation — `((close/close[15])-1)<-0.05` and `min(close[1]-low[1], open[1]-low[1]) > (high[1]-low[1])/2` and `low > low[1]` → enter long one unit (`strategy.entry("BUY", strategy.long)`, gated by the always-true `window()` under shipped defaults).
- Exit to flat (pinned, source-verbatim): current-bar shooting star plus extended context — `((close/close[15])-1)>0.05` and `min(high-close, high-open) > (high-low)/2` → close the long in full (`strategy.close("BUY")`, same always-true window).
- No entry/exit ambiguity exists anywhere in this record: the two 15-bar conditions (`<-0.05` vs `>+0.05`) are mutually exclusive on every bar, so conflict priority is provably irrelevant — no tie-break is admitted or needed. Non-signal bars are explicit no-ops with position carried. Pre-first-signal bars are flat (no standing position exists until the first hammer bar).
- Position rule (predeclared researcher pin): single-unit; repeat entry predicates while already long are no-ops (no pyramiding, no averaging, no second unit — to the extent source `pyramiding = 1` would permit an additional same-direction unit, that add is excluded here and only here). Re-entry after a close needs only the next qualifying hammer bar (no cooldown specified — explicitly none, not invented).
- Risk posture (pinned): no stop-loss, no take-profit, no trailing, no time exit beyond the shooting-star close, no cooldown (no stop/limit/profit/trail text of any kind exists anywhere in-source — each risk leg is explicitly none, not invented).
- Direction: long-only. The short side is explicitly absent (0 `strategy.short` tokens anywhere); spot venue suffices and no margin-short permission is needed.

## Required data

- Completed `1d` bars of BTCUSDT: `open`, `high`, `low`, `close` only (deepest references `close[15]`, `open[1]`, `high[1]`, `low[1]`). No `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar-table, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (0 `request.*` / 0 `security(` anywhere; the six `input(` calls are date-window constants at shipped always-true defaults, read by no signal arithmetic).
- Single decision timeframe `1d` (researcher choice — the pinned rule names no timeframe). One evaluation per completed bar; all signal reads reference completed bars only (`[15]`/`[1]` lags and the current completed bar); no intrabar path is read.
- Date-window semantics pinned: `window()` under shipped defaults (`FromYear=1000`, `ToYear=9999`) is true for every real bar, so no date gating enters the derived spec — recorded as source-declared-by-default, never re-tuned.
- Warmup: pinned 100-bar warmup — the rule's deepest lag is `close[15]`, so window history is complete on the 16th completed bar (structural minimum); pre-100 bars are flat by record rule (predeclared researcher choice, covering return-seeding transients). No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance spot under the house overlay (researcher choice — the pinned rule names no market in-code, and no source-market equivalence is claimed). Long-only needs no leverage and no margin-short permission, realistic on any spot venue.
- Order timing (source-declared-by-default): completed-bar decision with next-bar-open market fills — the file sets no `process_orders_on_close`, so the language default governs (entry and close both fill at the next `1d` open), compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). This record claims no other fill convention.
- Stop/limit modeling: none — the derived spec carries zero stop/limit/trailing/time orders by record rule. No hidden Hummingbot stop-order defaults are relied upon.
- Sizing/capital/costs: the source ships no sizing, capital, fee, slippage, or funding concept of any kind (no `initial_capital`, no `default_qty_*`, no `commission_*`, no `slippage` anywhere). The explicit house overlay (Base 6% + Safety 6% + Safety 6% sizing frame where applicable to a single-unit long, pinned house cost assumptions — fees; no hypothetical funding claimed) applies to the derived evaluation here, with the single-unit/no-add position pin from Signal, never presented as source-native behavior. Spot venue carries no funding leg; any perpetual-ported evaluation must carry the full house funding load instead.
- Concurrency: at most one long position at any time after the first hammer entry; the shooting-star close returns to flat in full in one step; re-entry after a close needs only the next qualifying hammer bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

With exact provenance (read end to end this cycle): the pinned file ships the complete rule (Pine v4 `strategy(` declaration with `pyramiding = 1`, the `buySignal`/`sellSignal` assignments with 15-bar ±5% context, half-range wick fractions, and higher-low confirmation, the `window()` gate at always-true shipped defaults, the one `strategy.entry` long leg and the one `strategy.close` flat leg, the author/description lineage). It ships zero performance numbers for this rule: no return, win rate, trade count, date range, or cost table — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden risk layer: 0 `strategy.exit` / 0 `strategy.order` tokens anywhere — the sole position-closing path is the shooting-star full close. The absence is coded (the program ends at the `strategy.close` leg), disclosed in Signal for the reviewer rather than upgraded into a source claim.
2. No short leg exists: 0 `strategy.short` tokens — a reviewer must not graft a short entry, a symmetric exit-to-short, or a reversal book onto this record.
3. Mutual exclusivity is structural, admitted plainly: the entry context (`<-0.05`) and the exit context (`>+0.05`) cannot co-hold, so no bar can fire both legs — conflict priority is provably irrelevant and no tie-break is admitted. Boundary ties hold their side: an exactly −5%/+5% print or a wick exactly half the range satisfies neither strict inequality, so no order fires and the book carries the prior state; warmup bars are flat by record rule.
4. No baked-in sample window: the shipped date defaults (1000-01-01 to 9999-01-01) admit every real bar. The Range Filter scrapes in the same repo carry restrictive 2020–2024 backtest windows — different, unpinned rules for the order path, fenced and never adopted here.
5. Sibling variants fenced, never adopted: the same repo's Forex Pin-Bar, Hammers & Stars, Doji swing, Pure Morning Doji, Marubozu, Big Bar, 3LS/3-Candle Strike, and 80-20 (indicator-only — zero order calls) files, plus the different-author Wick Reversal indicator/scripts (Gavi, JamesK318 SIM, PivotBoss Wick Reversal Setup — different wick-multiplier/close-percent/confirmation rules), are different, unpinned rules — a reviewer must not graft any of their ratios, confirmations, stops, or targets onto this record.
6. Overlap fences, admitted plainly: pool `three-white-soldiers-black-crows-flip` trades a three-candle body sequence two-sided with an anti-doji filter (different pattern, book, and direction); pool `dual-ema-engulfing-volume-long` trades two-bar engulfing gated by EMA plus a volume gate (different pattern and filter); pool `1-3-1-red-green` / `three-down-three-up` / `eight-day-run` trade consecutive-bar counts with no wick geometry (different event); pool `catching-the-bottom-rsi-dip` / `double-seven-connors-pullback` / `wvf-stochrsi-filtered-bottom` / `oversold-rsi-tight-sl` trade oscillator-gated dips (different construction — no wick fraction anywhere); pool `mcginley-ema-touch` / `support-resistance-fractal` / `williams-fractal` trade average-touch or swing-point events (different triggers); closed-unmerged PR #220 trades 3-bar gap-penetration morning/evening stars two-sided off a different source (different pattern, book, gap logic — never in `main`). Shared `reversal`/`dip`/`wick`-mention vocabulary is not shared signal.
7. Asymmetric confirmation, admitted plainly: entry keys off the prior bar's hammer plus the current bar's higher low (a one-bar confirmation lag is baked into the source rule), while exit fires on the current bar's shooting star with no confirmation — chop that prints hammer then immediate shooting star pays full round trips plus fees, disclosed, not tuned away.
8. No hidden variants admitted: any other lookback, any other return threshold, any other wick fraction, any symmetric or two-sided legs, any stop/target/filter/cooldown, any other frame, fill, or venue is a different, unpinned rule. A reviewer must not pick among these to rescue or reshape the record.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `close/open/high/low` inputs / 15-bar return context as pinned / ±5% thresholds / half-range wick fractions / higher-low confirmation / single-unit long-flat book / next-open fills / no-stop posture / `1d` BTCUSDT spot are frozen.

- F1 — Momentum-context relevance: a pure-wick twin (both ±5% 15-bar conditions removed — enter every prior-hammer plus higher low, exit every shooting star, same book and timing) must not improve net expectancy; fail ⇒ the sold-off/extended context adds nothing over raw wick signals.
- F2 — Higher-low confirmation relevance: a confirmation-free twin (the `low > low[1]` leg removed — enter on the prior hammer alone, same context and exit) must not improve net expectancy; fail ⇒ the higher-low confirmation adds nothing over the hammer print itself.
- F3 — Sold-off-precondition relevance: an inverted-context twin (enter on hammers only when the 15-bar return exceeds +5% — chasing extended rallies instead of sold-off stretches, same exit) must not match the pinned rule's trade-event structure; fail ⇒ the sold-off precondition (not the hammer shape alone) carries the entry edge.

## Crypto portability

Pinned to BTCUSDT Binance spot under the house overlay (declared port of a market-free listing). The rule reads completed daily OHLC only, so no pit-session, gap, roll, or corporate-action logic ports. Every threshold is a scale-free ratio (15-bar close-to-close return, wick-over-range fractions), so no price-level recalibration crosses venues — yet crypto's 24/7 volatility clustering vs the listing's undeclared market prior is a real mismatch: hammers print far more often in high-volatility chop, unclaimed and undisguised (see Negative evidence 7). The rule is long-flat, so spot and futures both express it without venue gating; the spot pin carries no funding leg. No warmup history beyond 100 daily bars is consumed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- No price stop, no time stop: adverse excursion after a hammer entry has no guardrail before the shooting-star close, by the prescribed source design — the record's principal risk.
- Next-open lag: each signal is detected at the completed-bar close and filled at the next open, systematically one bar late on V-turns and exhaustion prints.
- Asymmetric confirmation exposure: entries wait a bar for the higher low while exits fire same-bar — whipsaw markets pay full entry-to-exit round trips plus fees, disclosed, not tuned away.
- Context-threshold stranding: deep waterfalls that never print a qualifying hammer never enter, and parabolic rallies exit on the first shooting star — the ±5%/half-range cutoffs strand both tails by design.
- Single-venue daily port: market-free provenance vs 24/7 BTCUSDT daily execution is a declared derivation with unclaimed portability residual (prints, fees, margin mechanics beyond the house model).
- Performance evidence is absent: no source reports a number for this exact rule, and none is claimed here.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior and never part of this admission — no Safety-Order/DCA event is admitted in this record's version. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- hasnocool/tradingview-pine-scripts, `Wick Reversal.pine` at commit `e031cab2819a7d56fb8bb9d000252f51439986e2` (sole commit touching this path, 2023-09-02; blob SHA `21e5676347d4e3e75bfc707164f132b399a89689`, 1697 bytes, SHA-256 `24ec93eb2533544749fcf23dc2517f87f400a3b0b8fb60e0c4fe0965056b6afa` — Pine v4 strategy with 15-bar ±5% momentum context, half-range wick fractions, higher-low confirmation, one long entry plus one flat close, no stops — read end to end via live raw fetch 2026-10-16): https://github.com/hasnocool/tradingview-pine-scripts/blob/e031cab2819a7d56fb8bb9d000252f51439986e2/Wick%20Reversal.pine
- Wick Reversal — Strategy by OHM_INSTITUTIONAL_BROKING, script id `Yl9lDJxU` (one-sentence hammer/shooting-star thesis — lineage/identity only, page not opened this run): https://in.tradingview.com/script/Yl9lDJxU-Wick-Reversal/
