---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Ultimate Oscillator oversold-breakout long on BTCUSDT 1d bars
created: 2026-10-10
updated: 2026-10-10
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-10-18
sources:
  - https://www.tradingview.com/script/z985j4Yo/
  - https://www.tradingview.com/pine-script-reference/v5/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Ultimate Oscillator oversold-breakout long on BTCUSDT 1d bars

## Provenance

Primary source read end to end (canonical TradingView page, live browser read 2026-10-10):

- Canonical page: https://www.tradingview.com/script/z985j4Yo/ (title `Ultimate Oscillator Trading Strategy`, author `EdgeTools`, `OPEN-SOURCE SCRIPT`, published Oct 18 2024 — adopted as `source_as_of` 2024-10-18; release notes Oct 24 2024 add only alert conditions and alert-setup prose, no rule change). The page prose attributes the oscillator to Larry Williams (1976) with periods 6/14/20 and weights 4/2/1, an oversold entry at 30, and an exit on close above the previous high. Page chrome (never adopted as strategy facts): chart quote E-mini Dow Jones futures `1D`, social stats (7 likes / 2,339 views), author bio, tag list.
- Full Pine v5 block read verbatim (56 lines, `//@version=5`, `strategy("Ultimate Oscillator Trading Strategy", overlay=false, commission_type=strategy.commission.cash_per_contract, commission_value=0.05, slippage=1)`): 1 `strategy(` / 0 `study(` / 1 `strategy.entry` (`strategy.entry("Long", strategy.long)`) / 1 `strategy.close` (`strategy.close("Long")`) / 0 `strategy.exit` / 0 `strategy.stop` / 0 `strategy.order` / 0 `strategy.cancel` / 3 `input.int` (`period1 = 6`, `period2 = 14`, `period3 = 20`) / 6 `ta.sma` / 0 `crossover` / 0 `crossunder` / 0 `ta.cross` / 0 `request.` / 0 `security(` / 0 `volume` / 0 `open` reads anywhere (`high` / `low` enter only inside buying-pressure/true-range arithmetic and the `high[1]` exit leg; `close` and `close[1]` gate the orders). The two `alertcondition` legs notify only and the `plot` / two `hline` legs render only — none can change any order.
- No immutable GitHub mirror is claimed; provenance rests on the canonical open-source TradingView script read verbatim this cycle, which is an eligible public source. The page ships zero performance tables or figures adopted here — the `profit factor exceeding 2.5` prose claim has no accompanying table, figure, or settings trace and is therefore not adopted as source-reported evidence; this record claims no source-reported performance and no reproduced performance.

Licence and rights: the canonical page is a public open-source TradingView publication under MPL-2.0 (page header `© EdgeTools`; republication subject to TradingView House Rules per the page notice). This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy built directly on the source's own `strategy.entry` / `strategy.close` calls — not a lossless reproduction. Researcher-declared adaptations are exactly five: (1) research market BTCUSDT Binance perpetual `1d` (the page-chart futures quote is page chrome, never adopted; the source names no market, and its frame evidence is the `1D` chart usage plus the `previous day's high` prose — see Signal); (2) Pine v5 default fill timing kept source-native — the declaration ships no `process_orders_on_close`, so market orders fill on the next bar's open, recorded here as the pinned rule rather than converted to same-bar-close; (3) position-state pin — single-unit long, repeat-entry-while-long as no-op, `strategy.close`-when-flat as no-op (Pine `pyramiding` default `0` semantics, recorded source-declared-by-default, pinned here as an explicit record rule); (4) an adopted 22-bar warmup with pre-warmup bars flat by record rule (covers the 20-bar SMA seeding plus the `[1]`-reference transient — see Required data); (5) house sizing/capital/costs replacing the source's contract-point cost stub (see Execution assumptions). The 6/14/20 periods, the 4/2/1 weights, the buying-pressure/true-range definitions, the six `ta.sma` legs, the `UO < 30` entry predicate, the `close > high[1]` exit predicate, the code order (entry block before close block), the long-only stance, and the no-stop/no-target/no-trailing/no-time-exit posture are source-verbatim.

Pre-write dedup (2026-10-10): working-tree case-insensitive searches for `ultimate`, `buyingPressure`, `EdgeTools`, and `z985j4Yo` return zero admitted rules using this source, author strategy, indicator, or mechanism — the sole `ultimate` hit anywhere is incidental prose inside `double-seven-connors-pullback-long-btcusdt-1d-2026-10-09.md`, and the sole `EdgeTools` hits are the MPL-2.0 code-credit lines in that same FMZ-derived record (different source identity FMZ 473246, different 7-day-close-channel mechanism). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long — same cited inventor lineage, different mechanism: 3-EMA channel streak, never a buying-pressure oscillator), #49 (Gaussian channel StochRSI-gated breakout long), #58 (reconstruction batch — file list verified, no oscillator-breakout record), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `etf-3day-reversion-ema5-mean-reversion-long-btcusdt-1d-2026-10-08.md` chains three lower highs AND lower lows under an EMA5 gate with an EMA5-recross exit, never an oscillator threshold; `catching-the-bottom-rsi-dip-reversal-long-ethusdt-1h-2026-10-08.md` and `oversold-rsi-tight-sl-long-btcusdt-1h-2026-10-07.md` are single-window RSI constructions with tight-stop exits, never a triple-window weighted buying-pressure ratio; `double-seven-connors-pullback-long-btcusdt-1d-2026-10-09.md` touches a 7-day lowest close under an SMA200 gate with a channel-high exit, never an oscillator level; `williams-r-level-cross-mean-reversion-long-btcusdt-1d-2026-10-09.md` crosses a single-window %R level, never a 4/2/1 triple-window blend. Five-axis distinction: mechanism differs (weighted triple-window buying-pressure/true-range mean-reversion with a prior-high-break exit versus single-window oscillators, close-channel touches, or high/low chains), signal construction differs (`100 * ((4*avgBP1/avgTR1) + (2*avgBP2/avgTR2) + (avgBP3/avgTR3)) / 7` over 6/14/20-bar SMAs versus any single-lookback formula), exits differ (`close > high[1]` breakout leg versus level recrosses, channel highs, or tight stops), horizon is `1d` BTCUSDT, source identity differs (TV z985j4Yo, EdgeTools).

## Economic mechanism

### Source-reported

Triple-window buying-pressure mean reversion: the Ultimate Oscillator blends short/medium/long buying-pressure-to-true-range ratios with 4/2/1 weights so that short-term pressure dominates; a print below 30 marks the asset as temporarily oversold after selling pressure, and the long is held until the close recovers above the previous bar's high — the page prose frames this as buying a temporary deviation and exiting on demonstrated recovery strength.

### Research interpretation

State-driven long-only dip-recovery system with no level-hold, no band, no stop, no target, and no short leg — flat until the first oversold print, long from the first bar with `UO < 30`, flat again on the first close above the prior high, with Pine-default no-op semantics suppressing repeat entries while long. Unlike single-window oscillators (RSI, %R, CCI) the signal cannot fire on one window's spike alone: all three SMA windows blend every bar, so a one-bar tail moves the 20-bar leg only marginally and the entry requires genuinely broad pressure weakness. Unlike channel-touch pullbacks (Double Seven, Low-High dip) there is no price-level anchor — the entry is a pure pressure-ratio level and the exit is a one-bar recovery breakout, so holding time is set entirely by how fast price retakes the prior high. The bet, as derived, is on BTCUSDT daily oversold-pressure recovery at exactly 6/14/20 blending with 4/2/1 weights, never on a trend, breakout, squeeze, calendar, volume, or funding anchor.

## Signal

Exact rule as pinned (periods `6` / `14` / `20`, weights `4` / `2` / `1`, threshold `30` — any other value is a different, unpinned rule):

- Declaration (source-native): Pine v5 builtins (`ta.sma`, `math.min`, `math.max`, `math.abs`) with v5 `na` semantics observed. `strategy()` ships no `pyramiding`, no `process_orders_on_close`, no `calc_on_every_tick`, no capital arguments — Pine v5 defaults apply (`pyramiding = 0`, `process_orders_on_close = false`, `calc_on_every_tick = false`), recorded source-declared-by-default (see position pin below). Commission `0.05` cash-per-contract plus `slippage = 1` ship in the declaration as contract-point stubs with no crypto-portable unit — fenced off, never carried into the derived economics (see Execution assumptions). The two `alertcondition` / one `plot` / two `hline` legs cannot change any order.
- Oscillator (pinned, source-verbatim): `buyingPressure = close - math.min(low, close[1])` (always ≥ 0 since `close ≥ low` and `close ≥ min(low, close[1])` are both tautologies), `trueRange = math.max(high - low, math.max(math.abs(high - close[1]), math.abs(low - close[1])))`, `avgBP1/avgTR1 = ta.sma(buyingPressure/trueRange, 6)`, `avgBP2/avgTR2 = ta.sma(..., 14)`, `avgBP3/avgTR3 = ta.sma(..., 20)`, `UO = 100 * ((4 * avgBP1 / avgTR1) + (2 * avgBP2 / avgTR2) + (avgBP3 / avgTR3)) / (4 + 2 + 1)`. All six smoothers are `ta.sma` — no EMA/RMA/WMA/VWMA/RSI/MFI leg ships anywhere, so no seeding-convention ambiguity beyond ordinary SMA warmup exists.
- Orders (source-native mapping, pinned): `buyThreshold = 30` (hardcoded literal, not an input), `buyCondition = UO < buyThreshold` (strict — equality never fires), `sellCondition = close > high[1]` (strict — equality never fires), then `if (buyCondition) strategy.entry("Long", strategy.long)` followed in code order by `if (sellCondition) strategy.close("Long")`. While already long, a repeat entry is a no-op (single-unit pin under `pyramiding = 0`); while flat, `strategy.close` is a no-op. Before the first signal the system is flat (no position by construction).
- Same-bar co-occurrence (pinned, disclosed): a bar with both predicates true fires both legs in code order (entry block first). Under the pinned next-bar-open fills both are market orders for the next open; the Pine broker-emulator same-bar entry-plus-exit sequencing is adopted as-coded and fenced as a limitation (Negative evidence 3) — it is not reordered, netted, or otherwise redesigned here. While long, no ordering question exists (entry is a no-op, only the close can act); while flat with only `buyCondition` true, only the entry acts.
- Risk legs (pinned absence, not invented): 0 `strategy.exit` / 0 `strategy.stop` / 0 `strategy.order` ship anywhere — the derived posture is explicitly no stop, no target, no trailing, no time exit; the sole position-closing path is the `close > high[1]` leg.
- Direction: long-only. The short side is absent by construction (no short `strategy.entry` ships anywhere) — explicitly disabled, not underspecified. Futures venue still pinned as the research market (house overlay), with the short permission simply unused.

## Required data

- Completed `1d` bars of BTCUSDT: `high`, `low`, `close` only (`high` / `low` enter inside buying-pressure/true-range arithmetic and the `high[1]` exit leg; the rule itself keys off `close`, `close[1]`, `low`, `high`, `high[1]`). No `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (0 `request.` / 0 `security(` ship anywhere).
- Single decision timeframe `1d` (source frame evidence: page chart used on `1D` plus the `previous day's high` exit prose; research market choice predeclared). One evaluation per completed bar (`calc_on_every_tick = false` default); all reads reference confirmed bars only; fills land on the next bar's open (`process_orders_on_close = false` default, pinned source-native).
- Warmup: the 20-bar SMA legs yield `na` until 20 values exist (comparisons against `na` are false, so no leg can fire — coded behavior, disclosed), and the `[1]` references need one further bar. The adopted warmup is the first 22 completed `1d` bars flat by record rule (predeclared researcher choice — covers SMA-20 seeding plus the one-bar reference transient with margin); no signal before bar 23 may trade. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; naming normalization is the only market step, and no source-market equivalence is claimed).
- Order timing (source-native, not converted): completed-bar decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source ships no `process_orders_on_close` argument (Pine default = next-bar-open fills); this record keeps that convention as its pinned rule and claims no same-bar-close behavior. No maker-touch, queue, or intrabar-path-dependent fill: the only legs are bar-close-evaluated market entry/close orders, and the flat-state co-occurrence case is fenced as-coded (see Signal, Negative evidence 3).
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its `commission_value = 0.05` / `slippage = 1` declaration is a contract-point stub with no crypto-portable unit and is fenced off, never converted. The explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all) apply to the derived evaluation here, with the single-unit/no-add/noop-on-repeat position pin from Signal, never presented as source-native behavior.
- Concurrency: at most one long position at any time; re-entry after an exit needs only the next `UO < 30` bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The unused short permission requires no margin-short modeling.

## Evidence

### Source-reported

The page ships the full construction (56-line Pine v5 block: `strategy()` declaration with commission/slippage stubs, 3/3 `input.int` at defaults `6` / `14` / `20`, `buyingPressure` / `trueRange` definitions, six `ta.sma` legs, the 4/2/1-weighted `UO` formula, the hardcoded `30` threshold, the strict `UO < 30` / `close > high[1]` predicates, code-ordered entry-then-close blocks, two alert legs, one plot plus two hlines). It ships zero adopted performance numbers: the `profit factor exceeding 2.5` sentence has no table, figure, settings trace, or sample window and is therefore not adopted — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit` / 0 `strategy.stop` ship anywhere — the sole position-closing path is the `close > high[1]` leg. The absence of any stop is coded absence, disclosed, not a tunable parameter here.
2. Flat-until-oversold, then fully exposed: before the first `UO < 30` print the system never trades, and once long it rides the full adverse excursion until a close retakes the prior high — no guardrail of any kind exists between entry and that breakout. A grinding decline that never prints a one-bar recovery holds the full unit indefinitely. This is the coded trade, disclosed, not a tunable parameter here.
3. Same-bar entry-plus-exit fenced: a flat-state bar with `UO < 30` AND `close > high[1]` fires both legs in code order (entry block first) as next-open market orders; the Pine broker-emulator same-bar sequencing is adopted as-coded, never reordered or netted by this record. Such V-reversal bars are rare (deep-pressure weakness and prior-high retake on the same daily bar), but the handling is emulator-defined, not record-defined — fenced, not repaired.
4. Division legs fenced: `avgBP1/avgTR1`, `avgBP2/avgTR2`, `avgBP3/avgTR3` divide by SMA-of-true-range legs that reach zero only if an entire 6/14/20-bar window prints zero range — impossible on continuously traded BTCUSDT `1d` bars (every daily bar in venue history spans a non-zero range). No explicit zero-guard ships in the source; the venue property is disclosed as the standing guard, and a flat-window deployment would be a different, unpinned rule.
5. Warmup blindness fenced: SMA-20 seeding suppresses every leg inside the first ~20 bars even if a textbook oversold print occurs — the adopted 22-bar flat warmup (predeclared) converts this into a record rule rather than a silent miss; a shorter warmup would be a different, unpinned rule.
6. Source basis fenced: the source names no market (the page-chart futures quote is chrome) and its frame evidence is usage-plus-prose (`1D` chart, `previous day's high`). The BTCUSDT-`1d` choice, next-bar-open fills, single-unit/no-add/noop pin, 22-bar warmup, and house sizing/costs are researcher choices, disclosed; this record is therefore never evidence that any source-market deployment passes.
7. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT-`1d` market choice, the position-state pin, the adopted 22-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the 6/14/20 periods, the 4/2/1 weights, the buying-pressure/true-range definitions, the six `ta.sma` legs, the `30` literal, the strict predicates, the code order, the long-only stance, the next-bar-open fills, and the no-stop/no-target/no-trailing/no-time-exit/no-cooldown posture are source-verbatim.
8. The `6` / `14` / `20` literals, the `4` / `2` / `1` weights, the strict predicates (not touch, not level-hold, not single-window), the single-unit long-only stance, the prior-high-break exit, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning any period/weight/threshold, dropping a window, converting the state legs into cross edges, adding a stop/target/filter/cooldown/gate, adding a short leg, or sizing partially instead of single-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `6` / `14` / `20` / `4` / `2` / `1` / `30` / strict predicates / code order / single-unit long-only / `close > high[1]` exit / `1d` BTCUSDT / next-bar-open fills are frozen.

- F1 — Threshold relevance: replacing the pinned `30` entry level with any adjacent oversold level must not improve net expectancy; fail ⇒ the pinned literal carries no advantage over neighboring levels and the record's threshold choice is arbitrary.
- F2 — Exit-leg relevance: replacing the `close > high[1]` recovery-break exit with a fixed N-bar time exit must not improve net expectancy; fail ⇒ the prior-high retake adds nothing over a clock exit.
- F3 — Triple-window relevance: replacing the pinned 4/2/1 triple-window blend with any single-window buying-pressure ratio at the same `30`-style level must not improve net expectancy; fail ⇒ the multi-window blending adds nothing over a single lookback.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision frame `1d` with usage-plus-prose source support; high/low/close arithmetic with no venue-specific read). The OHLC arithmetic ports across perpetual venues without structural change. No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Researcher market: the source names no market — BTCUSDT is a researcher choice; signal timing on other markets would differ by construction.
- Frame evidence is usage-plus-prose: the source's `1d` support is the `1D` chart usage plus the `previous day's high` exit prose, never a declared `timeframe` parameter — other frames would differ by construction.
- Same-bar entry-plus-exit sequencing is emulator-defined (Negative evidence 3) — backtest economics of a reordered or netted handling would differ by construction; the as-coded order is disclosed, not repaired.
- Division-by-range legs carry no explicit zero-guard (Negative evidence 4) — a deployment on flat-window data would be a different, unpinned claim.
- Unused cost stub: the source's `0.05` / `1` commission/slippage declaration is fenced off as non-portable; derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Position-state pin: same-side-add and flat-state close behavior beyond Pine's `pyramiding`-default semantics is pinned by record rule, disclosed, not independently source-proven beyond the shipped defaults.
- No price stop, no time stop: adverse excursion after entry has no guardrail beyond the prior-high retake, which may arrive many bars later or after deep excursion; repeated oversold prints while long are no-ops, so averaging down is impossible by construction. This is the coded posture, disclosed as the record's principal risk.
- Warmup cost: the first 22 bars are flat by record rule, so any textbook oversold print inside warmup is deliberately untraded — pinned, not recovered.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Ultimate Oscillator Trading Strategy canonical open-source script page by EdgeTools (published 2024-10-18): https://www.tradingview.com/script/z985j4Yo/
- Pine Script v5 semantics (built-ins, `na` handling, strategy execution model): https://www.tradingview.com/pine-script-reference/v5/
