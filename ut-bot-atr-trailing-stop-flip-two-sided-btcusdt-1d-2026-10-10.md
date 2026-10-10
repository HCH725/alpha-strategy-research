---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: UT Bot ATR trailing-stop flip two-sided on BTCUSDT 1d bars
created: 2026-10-10
updated: 2026-10-10
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2019-11-15
sources:
  - https://www.tradingview.com/script/VKMgZdYr-UT-Bot-Strategy/
  - https://www.tradingview.com/pine-script-reference/v4/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# UT Bot ATR trailing-stop flip two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (canonical TradingView page, live browser read 2026-10-10):

- Canonical page: https://www.tradingview.com/script/VKMgZdYr-UT-Bot-Strategy/ (title `UT Bot Strategy`, author `QuantNomad`, `OPEN-SOURCE SCRIPT`, published Nov 15 2019 — adopted as `source_as_of` 2019-11-15; author description credits the UT Bot indicator to `Yo_adriiiiaan` with the original-code idea to `HPotter`, and states this script cleans that code, converts it to v4, turns it into a strategy, and adds the Heikin Ashi input). Page chrome (never adopted as strategy facts): chart quote BITMEX XBTUSD `6h`, social stats (8.9K likes / 86 comments / 293342 views), author bio, tag list.
- Full Pine v4 block read verbatim (43 lines, `//@version=4`, `strategy(title="UT Bot Strategy", overlay = true)` with zero additional `strategy()` arguments): 1 `strategy(` / 0 `study(` / 2 `strategy.entry` (`strategy.entry("long", true, when = buy)` / `strategy.entry("short", false, when = sell)`) / 0 `strategy.close` / 0 `strategy.exit` / 0 `strategy.order` / 3 `input(` (`a = input(1, ...)` Key Value, `c = input(10, ...)` ATR Period, `h = input(false, ...)` Heikin Ashi switch) / 1 `atr(` / 1 `ema(` / 2 `crossover` / 1 `security(` / 1 `heikinashi(` (both fenced inside the `h`-gated branch — see Signal) / 2 `plotshape` / 2 `barcolor` (display only) / 0 `volume`, `open` read nowhere by any order-gating line (`high` / `low` enter only inside `atr(c)`).
- No immutable GitHub mirror is claimed; provenance rests on the canonical open-source TradingView script read verbatim this cycle, which is an eligible public source. No performance table, figure, or number ships anywhere on the page or in the code — this record claims no source-reported performance and no reproduced performance.

Licence and rights: the canonical page is a public open-source TradingView publication (republication subject to TradingView House Rules per the page notice). This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy built directly on the source's own two `strategy.entry` calls — not a lossless reproduction. Researcher-declared adaptations are exactly six: (1) `h = false` frozen at the source default (the Heikin Ashi branch is fenced off, never evaluated for any order — see Signal); (2) same-bar-close fills on the traded market's own `1d` bars (the source ships no `process_orders_on_close` argument, so Pine default next-bar-open timing applies to the original; this record's fill timing is a predeclared derivation); (3) position-state pin — single-unit per side, repeat-signal-while-positioned as no-op, full reversal on the opposite edge (Pine `pyramiding` default `0` semantics, recorded source-declared-by-default, pinned here as an explicit record rule); (4) an adopted 11-bar warmup with pre-warmup bars flat by record rule (covers `atr(10)` RMA seeding plus the `nz`-seed transient — see Required data); (5) research market BTCUSDT Binance perpetual `1d` (the page-chart BITMEX XBTUSD `6h` quote is page chrome, never adopted; the source names no market or timeframe, so market and frame are researcher choices, predeclared); (6) house sizing/capital/costs replacing the wholly absent source economics (see Execution assumptions). The Key Value `a = 1`, ATR Period `c = 10`, the 4-branch trailing-stop recursion, the `pos` state machine, the `ema(src, 1)` crossover edges, the `buy` / `sell` predicates with mutual exclusivity, the two `strategy.entry` mappings, and the no-stop/no-target/no-close posture are source-verbatim.

Pre-write dedup (2026-10-10): working-tree case-insensitive searches for `ut-bot`, `utbot`, `UT Bot`, `xATRTrailingStop`, `nLoss`, `VKMgZdYr`, and `Key Vaule` return zero strategy-record hits anywhere on `main` (66 records) — no admitted rule uses this source, author publication, indicator, or mechanism. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #58 (reconstruction batch — file list verified, no UT record), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: the PR-#63 SuperTrend record flips on a midpoint-based 2-branch band, never a close-based 4-branch recursive ratchet; the PR-#89 Chandelier record trails Donchian highest-high/lowest-low extremes with a dual-stop structure, never an ATR-multiple ratchet off close; `alphatrend-mfi-atr-trailing-reversal-btcusdt-4h-2026-10-08.md` trails ATR bands with a coeff/volume confirmation leg; `halftrend-dual-confirmation-flip-two-sided-btcusdt-1d-2026-10-10.md` ratchets a Donchian extreme with a smoothed-average AND close dual confirmation; `gann-hilo-activator-state-flip-trend-btcusdt-daily-2026-10-05.md` flips on a displaced 3-bar high/low average cross with no ratchet; the PR-#92 SSL record follows a 10-bar high/low SMA channel with a single comparison; `drm-dynamic-rsi-momentum-btcusdt-1d-2026-10-06.md` shares the author (QuantNomad) but is a dynamic-length RSI-momentum construction on a different script — different source identity and mechanism. Five-axis distinction: mechanism differs (close-based 4-branch recursive ATR trailing stop with ratchet-only continuation branches versus midpoint bands, Donchian extremes, SMA channels, or RSI momentum), signal construction differs (`nLoss = 1 * atr(10)` with `ema(src, 1)` crossover edges versus band flips, extreme breaks, or oscillator crosses), exits differ in event set (reversal-only via the opposite cross edge with no flat state versus flat-capable exits), horizon/market is the research `1d` BTCUSDT choice, and source identity differs (TV `VKMgZdYr` QuantNomad 2019 versus other TV authors or FMZ IDs).

## Economic mechanism

### Source-reported

Adaptive ATR trailing-stop trend following: a stop trails below price in uptrends (ratcheting up only) and above price in downtrends (ratcheting down only), widening when volatility rises and tightening when it falls; when price crosses the stop, the system flips direction and prints the opposite signal. The author positions it as a cleaned v4 strategy conversion of the Yo_adriiiiaan UT Bot indicator (HPotter's original idea) with an optional Heikin Ashi source switch.

### Research interpretation

Edge-triggered two-sided reversal system with no level, band, stop, target, or confirmation leg beyond the two coded cross edges — flat before the first signal, always-in-market (long XOR short) after it, reversing direction only on the opposite edge. Unlike midpoint-band followers (SuperTrend) the stop is computed off close, so it reacts to actual traded-price crosses rather than bar-midpoint crosses; unlike Donchian-extreme trailers (Chandelier, HalfTrend) there is no running extreme memory — the stop resets to `src ∓ nLoss` on every flip and otherwise only ratchets, so the distance from price is always exactly volatility-scaled with no structural anchor. Unlike oscillators there is no level, zero-line, or signal-line cross — the only events are the two flip edges. The bet, as derived, is on BTCUSDT daily trend persistence at exactly 1×ATR(10) sensitivity, never on a level, breakout, squeeze, calendar, volume, or mean-reversion anchor.

## Signal

Exact rule as pinned (`a = 1`, `c = 10`, `h = false` frozen — any other value is a different, unpinned rule):

- Declaration (source-native): Pine v4 builtins (`atr`, `ema`, `crossover`, `nz`, `iff`, `max`, `min`) with v4 `na` semantics observed. `strategy()` ships no `pyramiding`, no `process_orders_on_close`, no commission, no capital arguments — Pine defaults apply, recorded source-declared-by-default (see position pin below). The two `plotshape` / two `barcolor` legs render only and cannot change any order.
- Trailing stop (pinned, source-verbatim): `xATR = atr(10)`, `nLoss = 1 * xATR`, `src = close` (`h = false` pinned, so the `security(heikinashi(...), timeframe.period, close, lookahead = false)` branch is never taken and no multi-timeframe or Heikin Ashi read gates any order — fenced). `xATRTrailingStop` recursion over the previous stop `nz(xATRTrailingStop[1], 0)`: both closes above → `max(prev, src - nLoss)` (ratchet up only); both below → `min(prev, src + nLoss)` (ratchet down only); cross above → `src - nLoss`; cross below → `src + nLoss`. Bar-0 seed is deterministic (`nz` → 0, and `src > 0` always, so the first bar takes the reset branch).
- State (pinned, source-verbatim): `pos` ∈ {1, −1, 0-hold} flips to 1 when `src[1]` was below the previous stop and `src` is above it, to −1 on the mirror cross, else holds `nz(pos[1], 0)`. `pos` drives bar color only (`xcolor`, `barbuy` / `barsell` are level-based); no order reads `pos`.
- Orders (source-native mapping, pinned): `ema = ema(src, 1)` (identically `src` — recorded as written, not simplified into a different rule), `above = crossover(ema, xATRTrailingStop)`, `below = crossover(xATRTrailingStop, ema)`, `buy = src > xATRTrailingStop and above`, `sell = src < xATRTrailingStop and below`, then `strategy.entry("long", true, when = buy)` / `strategy.entry("short", false, when = sell)`. While already long, a repeat `buy` is a no-op (single-unit pin); while long, `sell` closes the full long and opens the full short in the same execution step (full reversal, no residual leg), and mirror. Before the first signal the system is flat (no position by construction).
- `buy` / `sell` are mutually exclusive on every bar by code (`src` cannot be simultaneously above and below the stop), so no bar can ever fire both legs — no same-bar ordering ambiguity exists anywhere in this record.
- Risk legs (pinned absence, not invented): 0 `strategy.close` / 0 `strategy.exit` ship anywhere — the derived posture is explicitly no stop, no target, no trailing, no time exit; the sole position-changing path is the opposite edge reversing the full unit.
- Direction: two-sided long/short with symmetric reversal. Futures venue required for the short leg (researcher market choice — pinned).

## Required data

- Completed `1d` bars of BTCUSDT: `high`, `low`, `close` only (`high` / `low` enter solely inside `atr(10)`; the rule itself reads `close` only). No `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (the sole `security(` call is fenced off by the pinned `h = false`).
- Single decision timeframe `1d` (researcher choice — the source names no market or timeframe; the page-chart quote is page chrome, never adopted). One evaluation per completed bar; all reads (`close`, `close[1]`, prior stop, `atr`) reference confirmed bars only.
- Warmup: `atr(10)` RMA seeding yields `na` on the earliest bars (comparisons against `na` are false, so no edge can fire — coded behavior, disclosed), and the `nz`-seeded recursion needs its first reset bar. The adopted warmup is the first 11 completed `1d` bars flat by record rule (predeclared researcher choice — covers ATR-10 seeding plus the state transient with margin); no signal before bar 12 may trade. No repainting, no negative shift, no future reference, no full-sample normalization (`lookahead = false` is source-verbatim on the fenced branch).

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; naming normalization is the only market step, and no source-market equivalence is claimed).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source ships no `process_orders_on_close` argument (Pine default = next-bar-open fills); this record does not claim that convention and instead pins same-bar-close fills as its own disclosed rule. No maker-touch, queue, or intrabar-path-dependent fill: with mutually exclusive edge legs and no stop/target legs, there is no same-bar ordering ambiguity of any kind.
- Sizing/capital/costs: the source ships no sizing, capital, fee, slippage, margin, or funding concept of any kind. The explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all) apply to the derived evaluation here, with the single-unit/no-add/reverse-full position pin from Signal, never presented as source-native behavior.
- Concurrency: at most one position (long or short) at any time; the opposite edge reverses in full in one step; re-entry after a reversal needs only the next opposite edge (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The short leg requires margin-short permission, realistic on the pinned perpetual venue.

## Evidence

### Source-reported

The page ships the full construction (43-line Pine v4 block: `strategy()` declaration with no extra arguments, 3/3 inputs at defaults `1` / `10` / `false`, `atr(10)` with `nLoss = a * xATR`, regular-close source with the fenced HA branch, the 4-branch `iff` trailing-stop recursion with `nz` seeding, the `pos` state machine, `ema(src, 1)` with the `above` / `below` crossover pair, the `buy` / `sell` predicates, two display leg pairs, and the two `strategy.entry` calls with zero `strategy.close` / `strategy.exit`). It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.close` / 0 `strategy.exit` ship anywhere — the sole position-changing path is the opposite edge reversing the full unit. The absence of any stop is coded absence, disclosed, not a tunable parameter here.
2. Always-in-market exposure, admitted plainly: after the first edge the system is never flat — a market that crosses the ratcheted stop in alternating directions flips the full unit on every alternating edge with no confirmation beyond the coded cross pair, no cooldown, and no cost guard. Adverse excursion between flips has no guardrail of any kind. This is the coded trade, disclosed, not a tunable parameter here.
3. Whipsaw at 1×ATR(10) sensitivity, admitted plainly: the tightest widely used UT Bot setting flips on any daily close that crosses one ATR(10) beyond the ratchet — sideways markets generate repeated full-unit reversals. Widening the Key Value or lengthening the ATR period would each be a different, unpinned rule — none is admitted here.
4. Heikin Ashi path fenced: the `security(heikinashi(...))` branch exists in the source but is never taken under the pinned `h = false`; an HA-sourced deployment would smooth signals at the cost of lag and would be a different, unpinned rule — none is admitted here.
5. Warmup blindness fenced: `atr(10)` seeding suppresses every edge inside the first ~10 bars even if a textbook cross prints — the adopted 11-bar flat warmup (predeclared) converts this into a record rule rather than a silent miss; a shorter warmup would be a different, unpinned rule.
6. Source basis fenced: the source names no market or timeframe (the page-chart quote is chrome). The BTCUSDT-`1d` choice, same-bar-close fills, single-unit/no-add/reverse-full pin, 11-bar warmup, and house sizing/costs are researcher choices, disclosed; this record is therefore never evidence that any source-market deployment passes.
7. Derivation boundary fenced: the only non-source-native behaviors in this record are the `h = false` freeze, same-bar-close fills, the position-state pin, the adopted 11-bar warmup with record-rule pre-warmup flat, the BTCUSDT-`1d` market choice, and house sizing/costs — all predeclared above; `a = 1`, `c = 10`, the 4-branch recursion, the `pos` machine, the `ema(src, 1)` edges, the `buy` / `sell` predicates, mutual exclusivity, the two `strategy.entry` mappings, the two-sided stance, and the no-stop/no-target/no-cooldown posture are source-verbatim. This record is therefore never evidence that the original script's default next-open-fill deployment passes.
8. The `1` / `10` / `false` literals, the strict edge predicates (not touch, not level-hold, not single-leg), the full-unit reversal, the two-sided stance, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning any input, dropping the crossover confirmation, converting edge-flips into state-holding, adding a stop/target/filter/cooldown/gate, dropping the short leg, or sizing partially instead of full-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `a = 1` / `c = 10` / `h = false` / 4-branch ratchet / strict cross-edge pair / full-unit reversal / two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Ratchet relevance: replacing the ratcheted stop (`max`/`min` accumulation across the regime) with a memoryless `src ∓ 1 * atr(10)` band recomputed fresh each bar must not improve net expectancy; fail ⇒ the sticky ratchet adds nothing over a memoryless band.
- F2 — Edge-confirmation relevance: replacing the `ema(src, 1)`-crossover edges with raw `src`-versus-stop cross edges (dropping the `above` / `below` legs) must not improve net expectancy; fail ⇒ the crossover legs add nothing over the raw cross.
- F3 — Parameter relevance: replacing the pinned `a = 1` / `c = 10` with any adjacent Key Value or ATR period must not improve net expectancy; fail ⇒ the pinned defaults carry no advantage over neighboring settings and the record's literal choice is arbitrary.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision frame researcher-chosen `1d`; high/low/close arithmetic with no venue-specific read). The OHLC arithmetic ports across perpetual venues without structural change. The short leg requires margin-short permission (realistic on perpetual venues; a spot-only deployment cannot express the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Researcher market/frame: the source names no market or timeframe — BTCUSDT `1d` is a researcher choice; signal timing on other markets or frames would differ by construction.
- Derived fill timing: same-bar-close execution is a researcher choice over a script whose default timing is next-bar-open; backtest economics of other timings differ by construction — the adaptation is disclosed, not hidden.
- Heikin Ashi input frozen: the source offers `h = true` as a user option; this record pins the default `false` and fences the branch — HA-sourced behavior is out of scope, not approximated.
- Position-state pin: same-side-add and reversal-quantity behavior beyond Pine's `pyramiding`-default semantics is pinned by record rule, disclosed, not independently source-proven beyond the shipped defaults.
- No price stop, no time stop, never flat after the first edge: adverse excursion after entry has no guardrail beyond the opposite edge, which may arrive many bars later or after deep excursion; alternating cross edges whipsaw the full unit repeatedly. This is the coded posture, disclosed as the record's principal risk.
- No source cost declaration: no capital, commission, fee, slippage, margin, or funding assumption ships anywhere — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Warmup cost: the first 11 bars are flat by record rule, so any textbook edge inside warmup is deliberately untraded — pinned, not recovered.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- UT Bot Strategy canonical open-source script page by QuantNomad (published 2019-11-15): https://www.tradingview.com/script/VKMgZdYr-UT-Bot-Strategy/
- Pine Script v4 semantics (built-ins, `na` handling, strategy execution model): https://www.tradingview.com/pine-script-reference/v4/
