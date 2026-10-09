---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: HalfTrend dual-confirmation flip two-sided on BTCUSDT 1d bars
created: 2026-10-10
updated: 2026-10-10
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2021-02-13
sources:
  - https://www.tradingview.com/script/U1SJ8ubc-HalfTrend/
  - https://www.tradingview.com/pine-script-reference/v6/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# HalfTrend dual-confirmation flip two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (canonical TradingView page, live browser read 2026-10-10):

- Canonical page: https://www.tradingview.com/script/U1SJ8ubc-HalfTrend/ (title `HalfTrend [everget]`, author `everget` / Alex Orekhov, `OPEN-SOURCE SCRIPT`, published Jan 25 2021, updated Feb 13 2021 — adopted as `source_as_of` 2021-02-13; page copy: `A popular trend indicator based on ATR. Similar to the SuperTrend but uses a different trend's identification logic`). Licence: page states the author publishes `disclosed code without license` while the code header states `HalfTrend script may be freely distributed under the terms of the GPL-3.0 license` — cited as GPL-3.0 per the in-code header; social stats (13.2K likes / 378 comments / 420061 views) are page chrome, never performance evidence.
- Full Pine v6 block read verbatim (104 lines, `//@version=6`, `indicator('HalfTrend', overlay = true)`): 1 `indicator(` / 0 `strategy(` / 0 `strategy.entry` / 0 `strategy.close` / 0 `strategy.exit` / 0 `strategy.order` — a pure indicator with zero order calls, so every order in this file is a predeclared researcher derivation (see declaration below). 5 `input.` declarations: `amplitude = input.int(2)` and `channelDeviation = input.int(2)` (calculation group) plus `showArrows` / `showChannels` / `showLabels` display bools (visuals group — gate no signal, fenced). 1 `ta.atr` (`atr2 = ta.atr(100) / 2`), 2 `ta.sma` (`highma` / `lowma` over `amplitude`), 1 `ta.highestbars` + 1 `ta.lowestbars` (both over `amplitude`), 0 `request.*`, 0 `time(`, 0 `volume`, `open` read nowhere (the rule reads `high` / `low` / `close` only). 2 `alertcondition` calls (Buy/Sell — notify only, gate no order).
- State machine read verbatim: `var int trend = 0` / `var int nextTrend = 0` / `var float maxLowPrice = nz(low[1], low)` / `var float minHighPrice = nz(high[1], high)`; extremes `highPrice = high[math.abs(ta.highestbars(amplitude))]` / `lowPrice = low[math.abs(ta.lowestbars(amplitude))]`; averages `highma = ta.sma(high, amplitude)` / `lowma = ta.sma(low, amplitude)`; ATR channel `dev = channelDeviation * atr2` (display only — see Signal). Flip-down leg: while `nextTrend == 1`, `maxLowPrice := math.max(lowPrice, maxLowPrice)`, then `if highma < maxLowPrice and close < nz(low[1], low)` fires `trend := 1, nextTrend := 0, minHighPrice := highPrice`. Flip-up leg (else branch): `minHighPrice := math.min(highPrice, minHighPrice)`, then `if lowma > minHighPrice and close > nz(high[1], high)` fires `trend := 0, nextTrend := 1, maxLowPrice := lowPrice`. Plotted line `ht = trend == 0 ? up : down` with ratcheted `up` / `down` trackers; signals `buySignal = not na(arrowUp) and trend == 0 and trend[1] == 1` / `sellSignal = not na(arrowDown) and trend == 1 and trend[1] == 0` (arrow vars are `na` on every non-flip bar by declaration, so each signal fires exactly on its flip bar).
- No immutable GitHub mirror is claimed; provenance rests on the canonical open-source TradingView script read verbatim this cycle, which is an eligible public source. No performance table, figure, or number ships anywhere on the page or in the code — this record claims no source-reported performance and no reproduced performance.

Licence and rights: the canonical page is a public open-source TradingView publication (GPL-3.0 per the in-code header). This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly six: (1) indicator-to-order mapping — the source ships zero order calls, so long/short entries and reversals on `buySignal` / `sellSignal` are the researcher's executable mapping, predeclared; (2) same-bar-close fills on the traded market's own `1d` bars (the source declares no execution timing anywhere); (3) position-state pin — single-unit per side, repeat-signal-while-positioned as no-op, full reversal on the opposite flip, predeclared (the source has no sizing concept at all); (4) an adopted 101-bar warmup with pre-warmup bars flat by record rule (covers `ta.atr(100)` na-propagation into the arrow/boolean legs plus `amplitude` seeding plus the `(trend, nextTrend) = (0, 0)` initial transient — see Required data); (5) research market BTCUSDT Binance perpetual `1d` (the source page chart shows an equity/ETF quote as page chrome, never adopted as a strategy fact — the source names no market, so the market is a researcher choice, predeclared); (6) house sizing/capital/costs replacing the wholly absent source economics (see Execution assumptions). The flip predicates, `amplitude = 2` default, state-transition table, signal booleans, mutual exclusivity, and the no-stop/no-target posture are source-verbatim.

Pre-write dedup (2026-10-10): working-tree case-insensitive whole-word searches for `halftrend` and `half-trend` return zero hits anywhere — no admitted rule uses this source, author publication, indicator, or mechanism. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #58 (reconstruction batch — file list verified, no HalfTrend record), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `alphatrend-mfi-atr-trailing-reversal-btcusdt-4h-2026-10-08.md` trails ATR bands with a coeff/volume confirmation leg, never a Donchian-extreme ratchet; `gann-hilo-activator-state-flip-trend-btcusdt-daily-2026-10-05.md` flips on a displaced 3-bar high/low average cross with no ratcheted extreme and no second confirmation; the SSL record in PR #92 follows a contemporary 10-bar high/low SMA channel with a single comparison and no tracked extreme. Four-axis distinction: signal construction differs (dual-confirmation — smoothed average versus ratcheted Donchian extreme AND close versus prior-bar extreme — versus single-comparison channel, ATR-band, or coeff/volume constructions; no pool record ratchets a running max-of-lows/min-of-highs), trigger differs (flip-bar edge on a two-variable state machine versus level holds or band crosses), exits differ in event set (reversal-only via the opposite flip with no flat state versus flat-capable exits), and source identity differs (TV `U1SJ8ubc` everget 2021 versus other TV authors or FMZ IDs).

## Economic mechanism

### Source-reported

Dual-confirmed structural trend following: the indicator ratchets a support level (running max of recent lows) upward while in an uptrend and a resistance level (running min of recent highs) downward while in a downtrend, and flips state only when both the smoothed price (SMA of highs/lows) and the actual close agree the level has broken. The author positions it as SuperTrend-like in purpose (`Similar to the SuperTrend but uses a different trend's identification logic`) with fewer single-wick whipsaws, since one extreme print alone — without smoothed-average and close confirmation on the same bar — cannot flip the state.

### Research interpretation

Edge-triggered two-sided reversal system with no price level, band, stop, target, or confirmation leg beyond the two coded confirmations — always-in-market after the first flip, reversing direction only on the opposite flip. Unlike single-comparison followers (SSL, Gann-Hilo) that re-evaluate one average against one line every bar, this system holds a sticky ratcheted extreme inside each regime, so shallow pullbacks that never satisfy both confirmations simultaneously leave the position untouched; the cost is symmetric lateness — a true V-reversal must drag the SMA across the ratchet AND close beyond the prior extreme on the same bar, so entries and reversals arrive strictly after the turn by code. Unlike band/breakout systems there is no volatility gate on the state itself (the ATR channel renders only); unlike oscillators there is no level, zero-line, or signal-line cross — the only events are the two flip edges. The bet, as derived, is on BTCUSDT daily structural-trend persistence under dual confirmation, never on a level, breakout, squeeze, calendar, volume, or mean-reversion anchor.

## Signal

Exact rule as pinned (`amplitude = 2` frozen — any other value is a different, unpinned rule):

- Declaration (derived): Pine v6 builtins (`ta.sma`, `ta.highestbars`, `ta.lowestbars`, `ta.atr`, `math.abs`, `math.max`, `math.min`, `nz`) with v6 `na` semantics observed. The three visuals-group inputs (`showArrows`, `showChannels`, `showLabels`) gate plots only and no order. `channelDeviation = 2` scales the rendered ATR channel only and gates no boolean (see below).
- State (pinned, source-verbatim): `trend` / `nextTrend` ints, `maxLowPrice` / `minHighPrice` floats, `up` / `down` line trackers; initial state `(trend, nextTrend) = (0, 0)` with `maxLowPrice = nz(low[1], low)` and `minHighPrice = nz(high[1], high)` (both equal the first bar's own extreme — deterministic, no `na` seed). The machine starts in the else (up-flip-watch) branch; the first bar satisfying the up leg arms `(trend, nextTrend) = (0, 1)` with no order (trend unchanged, and `buySignal` additionally requires `trend[1] == 1`).
- Flip-down predicate (pinned): while `nextTrend == 1`: `maxLowPrice := max(lowPrice, maxLowPrice)` with `lowPrice = low[abs(lowestbars(2))]`, then `highma < maxLowPrice AND close < nz(low[1], low)` with `highma = sma(high, 2)` fires `trend := 1, nextTrend := 0, minHighPrice := highPrice`. Flip-up predicate (pinned, mirrored): while `nextTrend == 0`: `minHighPrice := min(highPrice, minHighPrice)` with `highPrice = high[abs(highestbars(2))]`, then `lowma > minHighPrice AND close > nz(high[1], high)` with `lowma = sma(low, 2)` fires `trend := 0, nextTrend := 1, maxLowPrice := lowPrice`. Both confirmations must hold on the same bar — a smoothed-average break without the close break (or vice versa) flips nothing.
- Orders (derived mapping, predeclared): `buySignal` (flip bar into `trend == 0`) → enter long; `sellSignal` (flip bar into `trend == 1`) → enter short. While already long, a repeat `buySignal` is impossible by construction (it requires `trend[1] == 1`), and likewise for shorts — no same-side-add rule is needed; the record additionally pins repeat-signal-while-positioned as no-op. While long, `sellSignal` closes the full long and opens the full short in the same execution step (full reversal, no residual leg), and mirror. Before the first signal the system is flat (no position by construction).
- `buySignal` / `sellSignal` are mutually exclusive on every bar by construction (they require opposite values of `trend` and `trend[1]`), so no bar can ever fire both legs — no same-bar ordering ambiguity exists anywhere in this record. ATR/`dev` affect only rendered channel levels and arrow price positions, never any boolean: `arrowUp`/`arrowDown` are non-`na` exactly on flip bars (assigned only in the flip branches), so `not na(arrowUp)` is a pure flip detector — except during `ta.atr(100)` na-propagation (`up - na = na`), which is why the adopted warmup is 101 bars (predeclared, see Required data).
- Risk legs (pinned absence, not invented): 0 `strategy.*` calls ship anywhere — the derived posture is explicitly no stop, no target, no trailing, no time exit.
- Direction: two-sided long/short with symmetric reversal. Futures venue required for the short leg (researcher market choice — pinned).
- Display isolation: `plot` / `plotshape` / `fill` / `alertcondition` legs render or notify only and cannot change any order; `showArrows` / `showChannels` / `showLabels` / `channelDeviation` gate display only.

## Required data

- Completed `1d` bars of BTCUSDT: `high`, `low`, `close` only (sole series read by the flip predicates and ratchets). No `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (0 `request.*` anywhere).
- Single decision timeframe `1d` (researcher choice — the source names no market or timeframe; the page-chart quote is page chrome, never adopted). One evaluation per completed bar; all reads (`high[abs(highestbars)]`, `low[abs(lowestbars)]`, `sma`, `close`, `low[1]`/`high[1]`) reference confirmed bars only.
- Warmup: `ta.atr(100)` na-propagates into the arrow/boolean legs for the first ~100 bars (a flip inside warmup would print `na` arrows and fire no signal — coded behavior, disclosed), `sma`/`highestbars`/`lowestbars` need `amplitude = 2` bars, and the `(0, 0)` initial state needs its first arming bar. The adopted warmup is the first 101 completed `1d` bars flat by record rule (predeclared researcher choice — covers ATR-100 seeding plus state transient with margin); no signal before bar 102 may trade. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; naming normalization is the only market step, and no source-market equivalence is claimed).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source declares no execution timing (indicator only); this record does not claim any source fill convention. No maker-touch, queue, or intrabar-path-dependent fill: with mutually exclusive flip legs and no stop/target legs, there is no same-bar ordering ambiguity of any kind.
- Sizing/capital/costs: the source ships no sizing, capital, fee, slippage, margin, or funding concept of any kind. The explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all) apply to the derived evaluation here, with the single-unit/no-add/reverse-full position pin from Signal, never presented as source-native behavior.
- Concurrency: at most one position (long or short) at any time; the opposite flip reverses in full in one step; re-entry after a reversal needs only the next opposite flip (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The short leg requires margin-short permission, realistic on the pinned perpetual venue.

## Evidence

### Source-reported

The page ships the full construction (104-line Pine v6 block: 2/2 calculation inputs at defaults, three display bools, the `(trend, nextTrend)` state pair with `nz`-seeded extremes, `highestbars`/`lowestbars` Donchian extremes over `amplitude`, `sma(high/low, amplitude)` averages, the dual-confirmation flip pair, ratcheted `up`/`down` lines, ATR-100/`channelDeviation` display channel, flip-exact `buySignal`/`sellSignal` booleans, Buy/Sell alert conditions). It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.*` calls ship anywhere — the sole position-changing path is the opposite flip reversing the full unit. The absence of any stop is coded absence, disclosed, not a tunable parameter here.
2. Always-in-market exposure, admitted plainly: after the first flip the system is never flat — a market that alternately satisfies both confirmations in opposite directions flips the full unit on every alternating flip with no confirmation beyond the coded pair, no cooldown, and no cost guard. Adverse excursion between flips has no guardrail of any kind. This is the coded trade, disclosed, not a tunable parameter here.
3. Lateness at regime births: a genuine reversal must push the 2-bar SMA across the ratcheted extreme AND close beyond the prior-bar extreme on the same single bar — gradual turns that satisfy only one leg per bar never flip, so entries and reversals arrive strictly after the turn by code. The lag is the coded dual confirmation, disclosed, not shortened.
4. Warmup blindness fenced: `ta.atr(100)` na-propagation suppresses every boolean inside the first ~100 bars even if a textbook flip prints — the adopted 101-bar flat warmup (predeclared) converts this into a record rule rather than a silent miss; a shorter warmup would be a different, unpinned rule.
5. Source basis fenced: the source names no market or timeframe (the page-chart quote is chrome). The BTCUSDT-`1d` choice, same-bar-close fills, single-unit/no-add/reverse-full pin, 101-bar warmup, and house sizing/costs are researcher choices, disclosed; this record is therefore never evidence that any source-market deployment passes.
6. Derivation boundary fenced: the only non-source-native behaviors in this record are the indicator-to-order mapping, same-bar-close fills, the position-state pin, the adopted 101-bar warmup with record-rule pre-warmup flat, the BTCUSDT-`1d` market choice, and house sizing/costs — all predeclared above; `amplitude = 2`, the Donchian-extreme construction, the dual predicates, the state-transition table, the flip-exact booleans, mutual exclusivity, and the no-stop/no-target/no-cooldown posture are source-verbatim. This record is therefore never evidence that the original indicator itself passes.
7. The `2` literal, the strict dual predicates (not touch, not single-leg, not level-hold), the full-unit reversal, the two-sided stance, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning amplitude, dropping either confirmation leg, converting edge-flips into state-holding, adding a stop/target/filter/cooldown/gate, dropping the short leg, or sizing partially instead of full-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `amplitude = 2` / Donchian-extreme ratchet / strict dual-confirmation flip pair / full-unit reversal / two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Dual-confirmation relevance: replacing the dual predicate with either single leg alone (smoothed-average break only, or close-beyond-prior-extreme only) must not improve net expectancy; fail ⇒ the second confirmation adds nothing over either leg alone.
- F2 — Ratchet relevance: replacing the ratcheted running extremes (`max`/`min` accumulation across the regime) with the contemporaneous 2-bar Donchian extreme recomputed fresh each bar must not improve net expectancy; fail ⇒ the sticky ratchet adds nothing over a memoryless extreme.
- F3 — Parameter relevance: replacing the pinned `amplitude = 2` with any adjacent amplitude must not improve net expectancy; fail ⇒ the pinned default carries no advantage over neighboring lookbacks and the record's literal choice is arbitrary.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision frame researcher-chosen `1d`; OHLC-only arithmetic with no venue-specific read). The high/low/close arithmetic ports across perpetual venues without structural change. The short leg requires margin-short permission (realistic on perpetual venues; a spot-only deployment cannot express the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Indicator-to-order gap: the source is a pure indicator with zero order calls — every entry, reversal, and sizing behavior here is a researcher mapping, disclosed, not source-verbatim.
- Researcher market/frame: the source names no market or timeframe — BTCUSDT `1d` is a researcher choice; signal timing on other markets or frames would differ by construction.
- Derived fill timing: same-bar-close execution is a researcher choice over an indicator that declares no timing; backtest economics of other timings differ by construction — the adaptation is disclosed, not hidden.
- Position-state pin: same-side-add and reversal-quantity behavior has no source concept at all; the single-unit/no-add/reverse-full pin is a researcher choice, disclosed, not source-verbatim.
- No price stop, no time stop, never flat after the first flip: adverse excursion after entry has no guardrail beyond the opposite flip, which may arrive many bars later or after deep excursion; alternating dual-confirmation flips whipsaw the full unit repeatedly. This is the coded posture, disclosed as the record's principal risk.
- No source cost declaration: no capital, commission, fee, slippage, margin, or funding assumption ships anywhere — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Warmup cost: the first 101 bars are flat by record rule, so any textbook flip inside warmup is deliberately untraded — pinned, not recovered.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- HalfTrend [everget] canonical open-source script page (published 2021-01-25, updated 2021-02-13): https://www.tradingview.com/script/U1SJ8ubc-HalfTrend/
- Pine Script v6 semantics (built-ins, `na` handling, indicator execution model): https://www.tradingview.com/pine-script-reference/v6/
