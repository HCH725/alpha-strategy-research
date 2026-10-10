---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Fair Value Gap 2-bar breakout long on BTCUSDT 1h bars
created: 2026-10-10
updated: 2026-10-10
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-02-20
sources:
  - https://www.fmz.com/strategy/442257
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Fair Value Gap 2-bar breakout long on BTCUSDT 1h bars

## Provenance

Primary source read end to end (live FMZ page fetched and verified 2026-10-10):

- Canonical page: https://www.fmz.com/strategy/442257 (title `Breakthrough Fair Value Gap Strategy`, Chinese title `突破型公平价差策略`, translator `ChaoZhang`, embedded Pine author `© Greg_007`, `Last Modified 2024-02-20 15:47:05` — adopted as `source_as_of` 2024-02-20). The backtest header names the source market and frame explicitly: `period: 1h`, `basePeriod: 15m`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`, demo window `start: 2024-01-01 00:00:00` / `end: 2024-01-31 23:59:59`.
- Full Pine v5 block verified verbatim against the live page (`//@version=5`, `strategy("Fair Value Gap Strategy", "FVG Strategy", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=100, pyramiding = 1)`): 1 `strategy(` / 0 `study(` / 1 `strategy.entry("Long", strategy.long)` / 1 `strategy.entry("Short", strategy.short)` / 1 `strategy.close_all()` / 0 `strategy.exit` / 0 `strategy.stop` / 0 `strategy.order` / 0 `strategy.cancel` / 0 `crossover` / 0 `crossunder` / 0 `ta.cross` / 0 `request.` / 0 `security(` / 0 `ta.*` of any kind / 0 `volume` / 0 `open` reads anywhere (the rule reads only `high`, `low`, `close[1]`, `high[2]`, `low[2]`) / 3 `input.bool` (`longOnly = false` gates logic; the two `REMINDERS`-grouped bools are declared but never read by any order line — inert, disclosed). The two `plotshape` legs and the `//reset the status` block are fully commented out — render-only, never order-gating. The state flags `bullFVG` / `bearFVG` / `bullTrend` / `bearTrend` / `plotBull` / `plotBear` are assigned but never read by any order line — inert, disclosed.
- No immutable GitHub mirror is claimed; provenance rests on the public FMZ page plus the byte-verified embedded Pine block, which is an eligible public source. The page ships zero performance tables or figures adopted here — the `can be very profitable in trending markets` prose has no table, figure, settings trace, or sample window and is therefore not adopted; this record claims no source-reported performance and no reproduced performance.

Licence and rights: the embedded Pine block carries an MPL-2.0 header (`© Greg_007`); the FMZ page is a public strategy publication. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy pinned to the source's own `longOnly` branch — not a lossless reproduction of the source default. Researcher-declared adaptations are exactly five: (1) direction pin `longOnly = true` (the source default is two-sided; its own `else strategy.close_all()` branch fully specifies the long-only behavior — bearish gap flattens instead of shorting — and this record adopts that branch verbatim; rationale: an always-in-position two-sided perpetual deployment carries unverifiable historical funding under reviewer precedent #20, while the long-only form has genuine flat periods — see Execution assumptions); (2) research market spelling BTCUSDT for the source-header `BTC_USDT` on `Futures_Binance` (naming normalization only; `1h` frame and venue are source-native, never chosen); (3) the author's January-2024 one-month demo window and the `basePeriod: 15m` granularity note are fenced off as demo config, never strategy logic (see Negative evidence 4); (4) an adopted 3-bar warmup with pre-warmup bars flat by record rule (covers the `[2]`-lag seeding — see Required data); (5) house fees/funding treatment replacing the source's cost silence (the declaration ships no commission/slippage concept at all; see Execution assumptions). The 2-bar lag, the strict gap predicates, the `close[1]` confirmation legs, the bear-first `else`-priority, `pyramiding = 1`, the percent-of-equity-100 sizing default, the next-bar-open fills, and the no-stop/no-target/no-trailing/no-time-exit/no-cooldown posture are source-verbatim.

Pre-write dedup (2026-10-10): working-tree case-insensitive searches for `fair` (zero hits outside this new file), `fvg`, `442257`, and `Greg_007` return no admitted rule using this source, author strategy, or mechanism. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout), #63 (SuperTrend ATR-flip), #89 (Chandelier Exit stop-flip), #92 (SSL channel reversal) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `three-down-three-up-consec-close-long-btcusdt-1h-2026-10-07.md` keys off consecutive close direction with no high/low-gap construction; `double-seven-connors-pullback-long-btcusdt-1d-2026-10-09.md` touches a 7-day lowest close under an SMA200 gate, never a 2-lag inter-bar gap; `etf-3day-reversion-ema5-mean-reversion-long-btcusdt-1d-2026-10-08.md` chains three lower highs AND lower lows under an EMA5 gate with an EMA5-recross exit, never a strict gap-plus-close-confirmation predicate; `darvas-box-breakout-long-btcusdt-1d-2026-10-09.md` breaks a formed box high, never a 2-bar high/low discontinuity. Five-axis distinction: no pool record and no open PR fires on a strict 2-bar-lag high/low gap confirmed by the prior close with an opposite-gap flat exit.

## Economic mechanism

### Source-reported

Inter-bar discontinuity momentum: when today's range fully clears the range from two bars ago (a `breakthrough gap`), the move is treated as the start of a directional leg rather than noise; the 2-bar lag (instead of 1) is the source's stated defence against false breakouts and short pullbacks, and the prior-close confirmation leg keeps one-bar spikes from qualifying. Long gaps capture upside-leg starts; short gaps mark downside-leg starts.

### Research interpretation

State-driven long-only gap-momentum system with no level-hold, no band, no stop, no target, and no short leg — flat until the first bullish 2-bar gap with prior-close confirmation, long from the next open, flat again on the first bearish 2-bar gap, with Pine `pyramiding = 1` no-op semantics suppressing repeat entries while long and `close_all`-while-flat as a no-op. Unlike channel-touch pullbacks (Double Seven, Darvas) there is no anchored price level — the trigger is a pure inter-bar discontinuity, so signal frequency is set entirely by how often the 1h BTCUSDT tape prints non-overlapping 2-lag ranges. Unlike consecutive-close patterns (Three-Down-Three-Up) a close-direction streak alone can never fire: both range-discontinuity AND prior-close-confirmation must hold on the same evaluated bar. The bet, as derived, is on BTCUSDT hourly gap-leg continuation at exactly lag 2 with `close[1]` confirmation, never on a trend, oscillator, squeeze, calendar, volume, or funding anchor.

## Signal

Exact rule as pinned (lag `2`, strict comparisons, bear-first priority — any other value is a different, unpinned rule):

- Declaration (source-native): `//@version=5` with Pine v5 `na` semantics observed. `strategy()` ships `pyramiding = 1` explicitly, `default_qty_type = strategy.percent_of_equity` / `default_qty_value = 100` explicitly, and no `process_orders_on_close`, no `calc_on_every_tick`, no capital arguments — Pine v5 defaults apply (`process_orders_on_close = false`, `calc_on_every_tick = false`), recorded source-declared-by-default. No commission/slippage concept ships anywhere (fenced, never converted — see Execution assumptions).
- Predicates (pinned, source-verbatim): bearish leg `high < low[2] and close[1] < low[2]` (strict — equality on either comparison never fires); bullish leg `low > high[2] and close[1] > high[2]` (strict — equality never fires). Both legs are mutually exclusive by construction (both true would require `high < low[2]` and `low > high[2]` with `low <= high` and `low[2] <= high[2]` — a contradiction), and the code evaluates the bearish leg first with the bullish leg inside the `else` branch, so priority is coded as well as mathematical — no tie semantics exist anywhere.
- Orders (derived long-only mapping, pinned): on a bearish-leg bar `strategy.close_all()` (the source's own `longOnly` branch, adopted verbatim); on a bullish-leg bar `strategy.entry("Long", strategy.long)`; on all other bars nothing. While already long, a repeat bullish entry is a no-op (single open order under `pyramiding = 1`); while flat, `close_all()` is a no-op. Before the first signal the system is flat (no position by construction).
- Same-bar co-occurrence (pinned, vacuous by construction): because the legs are mutually exclusive and `else`-branched, no bar can ever fire both an entry and an exit — there is no emulator-defined sequencing to fence, unlike entry-plus-exit records. One evaluated bar maps to at most one order.
- Risk legs (pinned absence, not invented): 0 `strategy.exit` / 0 `strategy.stop` / 0 `strategy.order` ship anywhere — the derived posture is explicitly no stop, no target, no trailing, no time exit; the sole position-closing path is the bearish-gap `close_all()` leg.
- Direction: long-only (derived pin). The short side is explicitly disabled by adopting the source's own `longOnly` branch — not underspecified. The futures venue is still pinned as the research market (house overlay), with the short permission simply unused.

## Required data

- Completed `1h` bars of BTCUSDT: `high`, `low`, `close` only (the rule keys off `high`, `low`, `close[1]`, `high[2]`, `low[2]`). No `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (0 `request.` / 0 `security(` ship anywhere).
- Single decision timeframe `1h` (source-header-native: `period: 1h` on `Futures_Binance BTC_USDT`). One evaluation per completed bar (`calc_on_every_tick = false` default); all reads reference confirmed bars only (`[1]` / `[2]` lags plus the just-closed bar); fills land on the next bar's open (`process_orders_on_close = false` default, pinned source-native).
- Warmup: the `[2]` references need three completed bars before every read is defined. The adopted warmup is the first 3 completed `1h` bars flat by record rule (predeclared researcher choice — exactly covers the deepest lag with no margin claimed); no signal before bar 4 may trade. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (source-header-native venue and frame; spelling normalization is the only market step, and no cross-venue equivalence is claimed).
- Order timing (source-native, not converted): completed-bar decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source ships no `process_orders_on_close` argument (Pine default = next-bar-open fills); this record keeps that convention as its pinned rule and claims no same-bar-close behavior. No maker-touch, queue, or intrabar-path-dependent fill: the only legs are bar-close-evaluated market entry/`close_all` orders, and same-bar dual-fire is impossible by construction (see Signal).
- Sizing/capital/costs: the source pins sizing explicitly (`percent_of_equity` 100, single position under `pyramiding = 1`, no adds, no compounding concept) and declares no commission, slippage, margin, or funding concept — adopted as the position pin, with costs carried by the explicit house overlay (pinned house fees plus historical funding treatment; no hypothetical zero funding claimed — the source declares no funding treatment at all, and the long-only form holds genuine flat periods between a bearish-gap flattening and the next bullish gap, so it is never an always-in-position funding accumulator). The downstream standard DCA matrix is a separately declared experiment, never source-native behavior here.
- Concurrency: at most one long position at any time; re-entry after an exit needs only the next bullish-gap bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The unused short permission requires no margin-short modeling.

## Evidence

### Source-reported

The page ships the full construction (Pine v5 block: `strategy()` declaration with `pyramiding = 1` and percent-of-equity-100 sizing, three `input.bool` legs with `longOnly = false` default, the strict bearish/bullish 2-lag gap predicates with `close[1]` confirmation, the bear-first `else` priority, the `close_all()`-versus-`Short` direction branch, one long entry, zero exits/stops/orders, fully commented-out plot legs). It ships zero adopted performance numbers: the `very profitable in trending markets` sentence has no table, figure, settings trace, or sample window and is therefore not adopted — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit` / 0 `strategy.stop` ship anywhere — the sole position-closing path is the bearish-gap `close_all()` leg. The absence of any stop is coded absence, disclosed, not a tunable parameter here.
2. Fully exposed between gaps: once long, the system rides the entire adverse excursion until a strict bearish 2-bar gap prints — in a grinding decline without clean inter-bar discontinuities the long is held indefinitely with no guardrail. This is the coded trade, disclosed, not a tunable parameter here.
3. Frequency honesty fenced: the source's own REMINDERS prose warns the pattern `can generate a lot of trades` on intraday crypto tape; 1h BTCUSDT ranges frequently fail to overlap at lag 2, so signal count is set by tape choppiness, not by any throttle in the rule — there is none. No frequency claim is made here.
4. Demo config fenced: the `start: 2024-01-01` / `end: 2024-01-31` header window and the `basePeriod: 15m` granularity note are the author's one-month demo settings, never strategy logic — dropped by predeclared adaptation, never tuned or carried. A different evaluation window would trade the identical event set per bar; it would not change a single rule.
5. Inert code fenced: the two REMINDER bools, the `bullFVG` / `bearFVG` / `bullTrend` / `bearTrend` / `plotBull` / `plotBear` flags, and both commented-out `plotshape` legs never gate any order — verified by full-block census, disclosed, never removed or repurposed here.
6. Derivation boundary fenced: the only non-source-default behavior in this record is the `longOnly = true` pin executed through the source's own coded branch (source-native is two-sided); the lag-2 predicates, the `close[1]` confirmations, the strict comparisons, the bear-first priority, `pyramiding = 1`, percent-of-equity-100 sizing, next-bar-open fills, the `1h` frame, the venue, and the no-stop/no-target/no-trailing/no-time-exit/no-cooldown posture are source-verbatim. This record is therefore never evidence that the source-default two-sided deployment passes.
7. The lag `2`, the strict predicates (not touch, not 1-lag, not unconfirmed), the bear-first priority, the single-position long-only stance, the opposite-gap flat exit, and the no-stop/no-cooldown stance are pinned, not removed: retuning the lag, dropping the `close[1]` confirmation, converting the legs into cross edges, adding a stop/target/filter/cooldown/gate, re-enabling the short leg, or sizing partially instead of percent-of-equity-100 would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: lag `2` / strict predicates / `close[1]` confirmation / bear-first priority / single-position long-only / opposite-gap flat exit / `1h` BTCUSDT / next-bar-open fills are frozen.

- F1 — Lag relevance: replacing the pinned lag `2` with lag `1` must not improve net expectancy; fail ⇒ the pinned 2-bar false-breakout defence carries no advantage over the raw 1-bar gap.
- F2 — Confirmation relevance: dropping the `close[1]` confirmation legs (range-discontinuity alone) must not improve net expectancy; fail ⇒ the prior-close confirmation adds nothing over the bare gap.
- F3 — Exit-leg relevance: replacing the bearish-gap flat exit with a fixed N-bar time exit must not improve net expectancy; fail ⇒ the opposite-gap exit adds nothing over a clock exit.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision frame `1h` with source-header support; high/low/close arithmetic with no venue-specific read). The OHLC arithmetic ports across perpetual venues without structural change. No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/sessions for the rule to read (no `time(` gating anywhere — the author's demo window is fenced off, not carried), so session-gap behavior needs no approximation; every `gap` here is a pure inter-bar discontinuity, defined on any continuously traded tape. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Researcher direction pin: the source default is two-sided — long-only is a researcher choice executed through the source's own coded branch; two-sided economics would differ by construction.
- Dropped demo window: evaluation-window choice changes which bars are scored, never any rule; window-truncated backtests would differ by construction.
- No price stop, no time stop: adverse excursion after entry has no guardrail beyond the next bearish gap, which may arrive many bars later or after deep excursion; repeated bullish gaps while long are no-ops, so averaging down is impossible by construction. This is the coded posture, disclosed as the record's principal risk.
- Unused cost silence: the source declares no commission/slippage/funding treatment; derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Position-state pin: same-side-add and flat-state `close_all` behavior beyond Pine's `pyramiding = 1` semantics is pinned by record rule, disclosed, not independently source-proven beyond the shipped defaults.
- Warmup cost: the first 3 bars are flat by record rule, so any textbook gap inside warmup is deliberately untraded — pinned, not recovered.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Breakthrough Fair Value Gap Strategy (FMZ, translator ChaoZhang, embedded Pine © Greg_007, last modified 2024-02-20, header `period: 1h` / `Futures_Binance BTC_USDT`): https://www.fmz.com/strategy/442257
- Pine Script v5 semantics (built-ins, `na` handling, strategy execution model): https://www.tradingview.com/pine-script-reference/v5/
