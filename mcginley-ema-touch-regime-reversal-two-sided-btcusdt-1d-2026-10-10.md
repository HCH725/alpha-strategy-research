---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: McGinley-regime EMA-touch reversal two-sided on BTCUSDT 1d bars
created: 2026-10-10
updated: 2026-10-10
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-09-02
sources:
  - https://github.com/hasnocool/tradingview-pine-scripts/blob/e031cab2819a7d56fb8bb9d000252f51439986e2/McGinley%20Dynamic%20Indicator.pine
  - https://www.tradingview.com/script/WHMsbRLs/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# McGinley-regime EMA-touch reversal two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (pinned immutable GitHub file, live raw fetch 2026-10-10, byte-identical at pin):

- Canonical file: https://github.com/hasnocool/tradingview-pine-scripts/blob/e031cab2819a7d56fb8bb9d000252f51439986e2/McGinley%20Dynamic%20Indicator.pine (repo `hasnocool/tradingview-pine-scripts`, file commit `e031cab2819a7d56fb8bb9d000252f51439986e2` dated 2023-09-02 — the sole commit touching this path; record `source_as_of` is that commit date, never the fetch date. Script author `LucasZancheta`; TradingView canonical page `McGinley Dynamic Indicator`, shorttitle `Maguila`, open-source, published 2020-05-28: https://www.tradingview.com/script/WHMsbRLs/).
- Full Pine v4 block read verbatim (`//@version=4`, `strategy(shorttitle="Maguila", title="McGinley Dynamic Indicator", overlay=true)` — a real executable `strategy(`, not an indicator): 1 `strategy(` / 0 `study(` / 2 `strategy.entry` (`"Compra"` long, `"Venda"` short, each `qty=1`, each gated by `when=` plus the date window) / 2 `strategy.exit` (one fixed `profit=20` tick target per side) / 3 `strategy.close` (two conditional loss-closes plus one `strategy.close_all()` outside the window) / 0 `strategy.order`. 11 `input(` declarations: `MA1Period = 21`, `MA2Period = 42` (both EMA on close), six backtest-window integers (start 28/05/2019, end 28/05/2020), McGinley `period = 20`, McGinley `k = 0.6`, price source `closePrice = close`. 1 `crossover(` (short leg, `high` over MA1), 1 `crossunder(` (long leg, `low` under MA1), 0 `request.*`, 0 `security(`, 0 `time(`, 0 `process_orders_on_close` (language default governs, recorded as source-declared-by-default), 0 `pyramiding` (default `0` governs, recorded likewise), 0 `calc_on_every_tick` (default `false` governs).
- State rule read verbatim: `MA1 = ema(close, 21)`; `MA2 = ema(close, 42)`; `aboveAverage = MA1 >= MA2`; `hunderAverage = MA2 >= MA1` (sic — both true when the EMAs are exactly equal, fenced below); McGinley recursion `mdi := na(mdi[1]) ? closePrice : mdi[1] + (closePrice - mdi[1]) / max(k * period * pow(closePrice / mdi[1], 4), 1)` with `mdi = 0.0` declaration (self-seeding at the first close, denominator floored at `1`, disclosed). Long leg: `buySignal = aboveAverage and closePrice > mdi and crossunder(low, MA1) and close > MA1` → `strategy.entry("Compra", strategy.long, qty=1, when=buySignal)` inside `inDateRange`; long loss-leg `buyLoss = closePrice < mdi and close < MA1 and close < MA2` → `strategy.close("Compra", qty=1, when=buyLoss)`; long scalp `strategy.exit("Gain da compra", "Compra", qty=1, profit=20)`. Short leg mirrors exactly (`sellSignal = hunderAverage and closePrice < mdi and crossover(high, MA1) and close < MA1`; `sellLoss` triple-above; `strategy.exit("Gain da venda", "Venda", qty=1, profit=20)`). Outside the window: `strategy.close_all()`.
- Source-reported venue (mirror header, corroboration only — never a gate fact): "The chart used for the backtest was the Bovespa Futures Index (WIN1! Continuous: current contract in front)". The TradingView page itself was not opened this run (extraction backend unavailable); the pinned GitHub block above carries every gate fact, and the TV URL is fenced as lineage-only.

Licence and rights: the pinned file carries the author's MPL-2.0 header (`© LucasZancheta`). This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly six: (1) same-bar-close fills on the traded market's own `1d` bars (the source sets no `process_orders_on_close`, so TradingView fills entries next-bar-open by default; this record pins completed-bar decision with same-bar-close execution for 1:1 pinned-backtester compatibility, predeclared); (2) the date window pinned constant-true — the eight date inputs and both `timestamp(` values compute a 2019-05-28→2020-05-28 gate in-source, but the BTCUSDT-`1d` research deployment evaluates every bar with `strategy.close_all()`-outside-window removed and pre-warmup bars flat by record rule instead (predeclared; the dead inputs are pinned as dead, not repurposed); (3) the `profit=20` tick scalp exits dropped as a non-portable market-microstructure artifact (source unit is WIN-future ticks — 20 ticks on BTCUSDT perpetual pricing is degenerate sub-spread dust with no coded percentage/ATR equivalent anywhere to port; the derived exits are therefore the triple-condition signal closes plus opposite-signal reversal only, predeclared — see Signal); (4) research market BTCUSDT Binance perpetual `1d` (the source names no market in-code; the porter's `WIN1!` header is not adopted); (5) an adopted 150-bar warmup with pre-warmup bars flat by record rule (covers EMA-42 seeding transient plus McGinley recursion settling plus margin — see Required data); (6) house sizing/capital/costs replacing the wholly absent source economics (see Execution assumptions). The `ema(close,21)` / `ema(close,42)` pair / `McGinley(20, 0.6)` recursion / wick-touch cross pair / strict `close ≷ mdi` regime filter / triple-condition loss-closes / both-sides stance / `qty=1` single-unit / default-`0` pyramiding are source-verbatim.

Pre-write dedup (2026-10-10): working-tree case-insensitive searches for `mcginley`, `mcginley-dynamic`, `maguila`, `lucaszancheta`, and `waddah` return zero strategy records using this source, author script, indicator, or mechanism. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #58 (reconstruction batch — file list verified, no moving-average-touch record), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit stop-flip long), and #92 (SSL channel state reversal) — different mechanisms, indicators, and sources. Closed research PRs (#1–#96 reviewed by title) contain no McGinley record. Closest pool EMA-touch records differ in mechanism class: `dual-ema-engulfing-volume-long-btcusdt-1h-2026-10-07.md` enters on bullish-engulfing confirmation plus a volume filter (long-only, no adaptive regime line, no wick-touch trigger, no triple-condition exits); `ema-20-50-cross-btcusdt-1h-2026-10-06.md` trades the plain fast/slow EMA cross itself (no touch logic, no McGinley line, no regime veto). Four-axis distinction: signal construction differs (adaptive McGinley speed-ratio recursion as the regime line — no pool record computes `mdi[1] + (close - mdi[1]) / max(0.6*20*(close/mdi[1])^4, 1)`), trigger differs (wick-touch edge events `crossunder(low, EMA21)` / `crossover(high, EMA21)` with the close required back on the regime side — not a line-cross or a candle-pattern confirmation), exits differ (triple-condition signal closes `close ≶ mdi AND close ≶ MA1 AND close ≶ MA2` plus full-unit reversal, with the tick scalp explicitly dropped — no fixed stop/limit order survives in the derived spec), and source identity differs (LucasZancheta `Maguila` 2020-05-28 via hasnocool pin `e031cab`).

## Economic mechanism

### Source-reported

Adaptive-trend pullback-touch with a speed-sensitive regime veto: the McGinley Dynamic adjusts its smoothing to market speed (the `pow(close/mdi, 4)` denominator accelerates the line when price displaces far and slows it when price hugs it), so `close ≷ mdi` reads as the adaptive trend side. Entries buy/sell only the fast-EMA-side regime (`EMA21 ≷ EMA42`) when the bar's wick touches the fast EMA (`low` dipping to `EMA21` with the close holding above for longs; mirror for shorts) — a pullback-to-support entry inside an adaptive uptrend, exited at a 20-tick scalp or when price closes against all three references at once. The author's framing is preserved: an adaptive average that "tracks the market better than existing moving average indicators" by adjusting for shifts in market speed.

### Research interpretation

Edge-triggered two-sided pullback-touch reversal system on an adaptive-MA regime, without any bracket. Unlike plain EMA-cross records (the cross itself is the trade) the cross here never trades: `EMA21 ≷ EMA42` is only a regime permission, and the McGinley line is only a side veto — the trade fires solely on the wick-touch edge (`low` crossing under `EMA21` while the close stays above, with price also above McGinley). Unlike engulfing/pattern records, no candle shape beyond the touch-plus-close-back-above relation is read. As derived to BTCUSDT daily pullbacks, the bet is on fast-EMA support holding inside McGinley-confirmed drift — the failure mode is the missing stop made plain: with the tick scalp dropped and no stop coded anywhere, adverse excursion after a touch is realized in full until the triple-condition close (or the opposite touch) fires, so a V-through-the-EMA bar sequence is the record's principal risk, disclosed, not smoothed over.

## Signal

Exact rule as pinned (`MA1Period = 21`, `MA2Period = 42`, McGinley `period = 20`, `k = 0.6`, `closePrice = close` frozen — any other values are a different, unpinned rule):

- Declaration (derived): Pine v4 builtins (`ema`, `crossover`, `crossunder`, `na`, `max`, `pow`, `strategy.entry`, `strategy.close`) with v4 `na` semantics observed. Single-timeframe by construction (0 `request.*` / 0 `security(`). The `plot`/`barcolor` calls and all eight date inputs render or compute dead values only and gate no order. Both legs live — single-side variants would be different, unpinned rules.
- State (pinned, source-verbatim): `MA1 = ema(close, 21)`; `MA2 = ema(close, 42)`; `mdi` by the recursion above, self-seeded at the first close with the denominator floored at `1` (a displacement ratio that would drive the divisor below `1` is clamped — pinned, not repaired).
- Orders (source-coded, derivation only in fill timing, window, and scalp removal): a bar with `MA1 >= MA2` and `close > mdi` and `crossunder(low, MA1)` and `close > MA1` → enter long one unit; a bar with `MA2 >= MA1` and `close < mdi` and `crossover(high, MA1)` and `close < MA1` → enter short one unit. A bar holding long with `close < mdi and close < MA1 and close < MA2` → close long in full; a bar holding short with `close > mdi and close > MA1 and close > MA2` → close short in full. Opposite-signal entry while holding reverses in full in one step (Pine default `pyramiding = 0` reversal netting; the source declares no pyramiding — the default governs, recorded as source-declared-by-default). Conditional closes name their own side's entry id and are no-ops when flat — pinned.
- No same-bar entry/entry ambiguity exists anywhere in this record: the long leg requires `close > MA1`, the short leg requires `close < MA1` — both cannot hold on one bar, and the `crossover`/`crossunder` pair cannot co-fire on one bar either. Exact-equality bars (`close == MA1`, `close == mdi`, `MA1 == MA2` with no strict side) fire neither leg — ties defined by the strict operators, with the sole exception that `MA1 == MA2` satisfies both regime permissions simultaneously yet still cannot produce an entry without the strict close-side conditions, disclosed. Non-signal bars are explicit no-ops.
- Risk posture (pinned): no stop-loss, no take-profit, no trailing, no time exit, no cooldown (none coded — each explicitly none, not invented). The sole position-changing paths are the triple-condition signal closes and opposite-touch reversal.
- Direction: two-sided long/short with symmetric touch logic and full-unit reversal. Futures venue required for the short leg (researcher market choice — pinned).

## Required data

- Completed `1d` bars of BTCUSDT: `high`, `low`, `close` (all three read by order-gating lines: touch crosses read `low`/`high` against `MA1`; regime and loss-closes read `close`; McGinley recurs on `close`). No `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (0 `request.*` / 0 `security(` anywhere).
- Single decision timeframe `1d` (researcher choice — the pinned rule names no timeframe; the mirror's `WIN1!` backtest header is not adopted). One evaluation per completed bar; all signal reads reference confirmed bars only (`[1]` lags inside `ema`/`mdi`/`crossover`/`crossunder`, confirmed-bar relations); no intrabar path is read.
- Warmup: `ema(close, 42)` seeding transient dominates (McGinley self-seeds at the first close and settles within a few dozen bars beside it); Pine `ema` prints seeded values from bar 0 and `crossunder(na, x)` is falsy, so no touch can fire pre-history by construction. The adopted warmup is the first 150 completed `1d` bars flat by record rule (~3× the max fixed lookback 42 for EMA convergence plus McGinley settling plus margin — predeclared researcher choice); no signal before bar 151 may trade. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the pinned rule names no market in-code; the mirror's `WIN1!` header is porter chrome, and no source-market equivalence is claimed).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution for entries, closes, and reversals, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source sets no `process_orders_on_close` (TradingView default fills entries next-bar-open); this record does not claim any source fill convention. Within one bar, exits resolve before entries: a bar that fires the holding side's triple-condition close and simultaneously prints the opposite touch closes the old unit and opens the new one in the same step — the pinned net effect of Pine reversal netting under default `pyramiding = 0`, disclosed.
- Stop/limit modeling: none — the derived spec carries zero stop/limit/trailing/time orders by record rule (the source's only such orders, the two `profit=20` tick scalps, are dropped as non-portable — see Negative evidence). No hidden Hummingbot stop-order defaults are relied upon; the exits-before-entries ordering is a record rule, disclosed.
- Sizing/capital/costs: the source ships no sizing, capital, fee, slippage, margin, or funding concept of any kind beyond `qty=1`. The explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all) apply to the derived evaluation here, with the single-unit/no-add position pin from Signal, never presented as source-native behavior.
- Concurrency: at most one position (long or short) at any time; a triple-condition close exits in full; the opposite touch reverses in full in one step; re-entry after a close needs only the next qualifying touch (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The short leg requires margin-short permission, realistic on the pinned perpetual venue.

## Evidence

### Source-reported

The pinned file ships the full construction (Pine v4 `strategy(` declaration with `overlay=true`, eleven inputs at pinned defaults, the self-seeding McGinley recursion with floored denominator, the `EMA21/EMA42` regime pair, the wick-touch `crossunder(low, MA1)` / `crossover(high, MA1)` entry pair with strict close-side conditions, the triple-condition `strategy.close` loss pair, the per-side `profit=20` tick `strategy.exit` pair, the constant-window gate with `strategy.close_all()` outside it, plus the author's adaptive-average tenet and MPL-2.0 header). The mirror description's `WIN1!` backtest note is venue chrome, never performance evidence. The page ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Scalp removal, admitted plainly: the source's only limit orders are `profit=20` ticks per side — a WIN-future tick unit with no coded percentage, ATR, or point equivalent. Ported literally to BTCUSDT perpetual pricing, 20 ticks is degenerate sub-spread dust that would exit essentially every position on the entry bar; invented re-scalings (ATR multiples, percentages) would be researcher fiction. This record therefore drops both tick scalps and exits only on triple-condition closes plus reversal — a predeclared derivation, disclosed, not source exits.
2. Fill-timing derivation, admitted plainly: with no `process_orders_on_close` in-source, TradingView fills entries next-bar-open by default — this record's same-bar-close fills are a researcher adaptation for pinned-backtester compatibility, disclosed, not source timing.
3. Window derivation, admitted plainly: the source gates entries on the 2019-05-28→2020-05-28 window with `strategy.close_all()` outside; the eight date inputs are pinned as dead in the derived spec and evaluation is every post-warmup bar — disclosed, not repaired and not adopted as a window.
4. Missing stop, admitted bluntly: no stop-loss, take-profit (after scalp removal), trailing, time exit, or cooldown exists anywhere in the derived spec — each explicitly none. A touch that immediately fails through the EMA realizes the full adverse excursion until the triple-condition close or the opposite touch fires; gap-through sequences have no bound in this record. This is the coded posture minus the non-portable scalp, disclosed as the record's principal risk.
5. `na`/seed edges, disclosed: `mdi` self-seeds at the first close (`na(mdi[1]) ? closePrice`) so the recursion is defined on every bar, but early McGinley values are seed-dominated transient — covered by the 150-bar record-rule flat, not traded. The denominator floor `max(..., 1)` clamps extreme displacement ratios — pinned, not smoothed over. Pre-history `crossover`/`crossunder` relations are falsy by construction.
6. Regime-overlap edge, disclosed: `MA1 == MA2` satisfies both `aboveAverage` and `hunderAverage` at once, but the strict `close ≷ MA1` / `close ≷ mdi` legs keep entries mutually exclusive on every bar — equality fires nothing, pinned.
7. Source basis fenced: the pinned rule names no market or timeframe (the mirror's `WIN1!` note is chrome). The BTCUSDT-`1d` choice, same-bar-close fills, exits-before-entries ordering, every-bar evaluation, 150-bar warmup, single-unit/no-add pin, scalp removal, and house sizing/costs are researcher choices, disclosed; this record is therefore never evidence that any source-market deployment passes.
8. Derivation boundary fenced: the only non-source-native behaviors in this record are same-bar-close fills, exits-before-entries ordering, every-bar evaluation with dead date inputs, the adopted 150-bar warmup with record-rule pre-warmup flat, the dropped tick scalps, the BTCUSDT-`1d` market choice, and house sizing/costs — all predeclared above; the `ema(close,21)` / `ema(close,42)` pair / `McGinley(20, 0.6)` recursion with floored denominator / wick-touch cross pair / strict `close ≷ mdi` veto / triple-condition loss-closes / both-sides stance / `qty=1` / default-`0` pyramiding / no-trailing/no-time-exit/no-cooldown posture are source-verbatim. This record is therefore never evidence that the original script itself passes.
9. The `21` / `42` / `20` / `0.6` literals, the wick-touch (not line-cross, not pattern) trigger, the strict McGinley side veto (equality fires nothing), the triple-AND loss-closes (any two of three holding fires nothing), the full-unit reversal, and the two-sided stance are pinned, not removed: retuning any literal, widening touches to closes-through, loosening loss-closes to single conditions, re-adding any TP/SL/trailing/cooldown leg, dropping the short leg, or sizing partially instead of full-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `ema(21)` / `ema(42)` / `McGinley(20, 0.6)` / wick-touch pair / strict `mdi` veto / triple-condition closes / full-unit reversal / two-sided / `1d` BTCUSDT / same-bar-close fills / exits-first ordering are frozen.

- F1 — McGinley relevance: replacing the `close ≷ mdi` side veto with the close's side of `EMA42` through the same touch triggers and exits must not improve net expectancy; fail ⇒ the adaptive recursion adds nothing over the plain slow EMA.
- F2 — Touch relevance: replacing the wick-touch triggers with plain `crossover/crossunder(MA1, MA2)` entries through the same veto and exits must not improve net expectancy; fail ⇒ the pullback-touch adds nothing over the regime cross.
- F3 — Loss-close relevance: replacing the triple-condition closes with pure opposite-touch reversal exits (no signal closes) must not improve net expectancy; fail ⇒ the triple-close adds nothing over reversal-only risk control.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision frame researcher-chosen `1d`; arithmetic over high/low/close with no venue-specific read). The construction ports across perpetual venues with full OHLCV feeds without structural change. The short leg requires margin-short permission (realistic on perpetual venues; a spot-only deployment cannot express the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere; the date inputs are dead by record rule), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Dropped scalp: the source's only take-profit legs are removed as a non-portable tick artifact; backtest economics of any re-added TP level would differ by construction — the removal is disclosed, not hidden.
- No stop anywhere: loss is bounded only by the triple-condition closes and reversal; the record carries no stop-loss/trailing/time-exit/cooldown by design — disclosed as the principal risk, not a gap to be quietly repaired later.
- Derived fill timing: same-bar-close execution is a researcher choice over logic that defaults (in TradingView) to next-bar-open; backtest economics of other timings differ by construction — the adaptation is disclosed, not hidden.
- Derived window: every-bar evaluation replaces the source's 2019→2020 window; signal timing inside versus outside that window differs by construction — disclosed, not hidden.
- Researcher market/frame: the pinned rule names no market or timeframe — BTCUSDT `1d` is a researcher choice; signal timing on other markets or frames would differ by construction.
- Position-state pin: same-side-add behavior executes nowhere in-source beyond the default; the single-unit/no-add pin under Pine-default `pyramiding = 0` reversal netting is recorded as source-declared-by-default plus researcher pin, disclosed.
- No source cost declaration: no capital, commission, fee, slippage, margin, or funding assumption ships anywhere — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Warmup cost: the first 150 bars are flat by record rule, so any textbook touch inside warmup is deliberately untraded — pinned, not recovered.
- Lineage limit: the TradingView page was not opened this run (extraction unavailable); lineage rests on the pinned file's own author/version stamps and the stable TV URL — every gate fact is from the pinned block itself.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- McGinley Dynamic Indicator [LucasZancheta, shorttitle Maguila] pinned GitHub mirror at commit `e031cab2819a7d56fb8bb9d000252f51439986e2` (sole commit touching this path, 2023-09-02; TV page published 2020-05-28): https://github.com/hasnocool/tradingview-pine-scripts/blob/e031cab2819a7d56fb8bb9d000252f51439986e2/McGinley%20Dynamic%20Indicator.pine
- McGinley Dynamic Indicator [LucasZancheta] canonical TradingView page, lineage-only (page not opened this run): https://www.tradingview.com/script/WHMsbRLs/
