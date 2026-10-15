---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Bufi adaptive-threshold RSI(2) 28-bar time-exit long-flat on BTCUSDT 1d bars
created: 2026-10-15
updated: 2026-10-15
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-09-17
sources:
  - https://www.tradingview.com/script/zDP76aFT-TASC-2024-10-Adaptive-Oscillator-Threshold/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bufi adaptive-threshold RSI(2) 28-bar time-exit long-flat on BTCUSDT 1d bars

## Provenance

Primary source read end to end (verified 2026-10-15):

- Canonical page: https://www.tradingview.com/script/zDP76aFT-TASC-2024-10-Adaptive-Oscillator-Threshold/ (`TASC 2024.10 Adaptive Oscillator Threshold` by `PineCodersTASC`, `OPEN-SOURCE SCRIPT` badge, page stamp Sep 17 2024, adopted as `source_as_of`). Fetched live twice during this cycle: once over HTTPS (HTTP 200, 462660 bytes, `OPEN-SOURCE` and `PineCodersTASC` markers byte-confirmed) and once in a real browser session (HTTP 200, badge/title/author/date rendered). The page carries a `Strategy report` tab (it is a `strategy`, not a `study`) and its demo chart shows SPDR S&P 500 ETF 1D (Cboe One) — display context only, never a rule. Page prose in substance: an adaptive buy-level technique from Francesco Bufi's article `Overbought/Oversold Oscillators: Useless Or Just Misused` (TASC October 2024 Traders' Tips) applied to a simple RSI strategy so users can compare it against the traditional fixed-threshold approach. The page ships no performance table, figure, trade count, date range, or cost basis — only the qualitative observation that the adaptive threshold can help backtest performance; this record claims no source-reported performance (see Evidence).
- Full 61-line `//@version=5` block read in the page's source viewer (MPL 2.0 header; header pins `TASC Issue: October 2024`, `Article: Overbought/Oversold Oscillators: Useless Or Just Misused`, `Article By: Francesco P. Bufi`, `Provided By: PineCoders`). Verbatim source declaration with the absences it discloses load-bearing for the derived status below: `strategy(title, stitle, false, default_qty_type = strategy.percent_of_equity, default_qty_value = 10, slippage = 5)` — no `pyramiding` (default 0: single open position, repeat entries rejected), no commission, no `process_orders_on_close`, no `calc_on_every_tick`. Source fills are therefore next-bar-open evaluated once per completed bar; this record's same-bar-close execution is a separately identified researcher adaptation, never presented as source-native (see Execution assumptions). The `percent_of_equity`/`10`/`slippage = 5` settings are tester settings echoed by the page DISCLAIMER (`10% of equity`, `5 ticks`), never coded economics.
- Pinned source inputs (all seven, defaults frozen): `sys = "BAT"` (`System`, options `["Traditional", "BAT"]`), `rsiLen = 2`, `buyLevel = 14`, `adapLen = 8`, `adapK = 6`, `exitBars = 28` (`Fixed-Bar Exit`), `DSL = 1600` (`Dollar Stop-Loss`, minimum `0`). Retuning any of them would be a different, unpinned rule.
- Text census over the pinned block: 1 `strategy(` declaration / 2 `strategy.entry` calls (both id `"long"` with `strategy.long` — long-only, no short leg ships anywhere) / 2 `strategy.close` calls (`"exit"` fixed-bar leg, `"Stop-loss"` dollar leg with `immediately = true`) / 0 `strategy.exit` / 0 `strategy.order` / 0 `stop=`/`limit=`/`profit=`/`loss=` / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `crossover(`/`crossunder(`/`ta.cross` / 0 `plotshape` / 4 render calls (`plot` × 3 + `fill` × 1, display only — none gates any order).
- Licence and rights: the canonical page is an open-source PineCodersTASC Traders' Tips publication (MPL 2.0). This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly six: (1) research market/timeframe BTCUSDT `1d` on Binance futures (the demo chart shows SPY 1D — frame-faithful daily choice; venue transfer plus symbol spelling disclosed here, never presented as source-native; the short side is never used so no short permission is exercised); (2) `sys = "BAT"` pinned (the `"Traditional"` fixed-threshold branch is real source content, disclosed here and never carried into the traded trigger — see Negative evidence); (3) `DSL = 0` (the coded `DSL > 0` guard makes the dollar-stop leg fully inert; a SPY-tester-calibrated dollar stop coupled to 10%-equity sizing is unportable to house sizing and carries `immediately = true` intrabar semantics — excluded by record rule, never silently kept); (4) same-bar-close fills (the source fills next-bar-open — no execution-timing argument ships anywhere, quoted verbatim in census); (5) an adopted 100-bar warmup with pre-warmup bars flat by record rule (signal needs ~10 bars — see Required data); (6) house sizing/capital/costs replacing the tester settings (zero cost assumption — recorded as absent economics, never as zero-cost evidence; see Execution assumptions). The RSI(2)-on-close oscillator, the stdev/linreg/slope/clamp threshold construction, all pinned constants, the sub-threshold level entry, the single `"long"` order id, `pyramiding` default 0, the 28-bar time exit, long-only direction, and the no-target/no-trailing posture are source-pinned or predeclared above and unmodified elsewhere.

Pre-write dedup (2026-10-15): working-tree case-insensitive fixed-string searches for `Bufi`, `adaptive threshold`, `AdapThrs`, `zDP76aFT`, `Misused`, `buyLevel`, `adapK`, and `exitBars` return zero strategy records using this source, author, article, indicator, or construction. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: every pool RSI record trades fixed-level crosses or reversals (`rsi-classic-level-reversal`, `cumulative-rsi-dual-threshold`, `connors-rsi2-ma70-fade`, `drm-dynamic-rsi-momentum`, `laguerre-rsi-cu-cd-cross`) and none scales its level by a signed linreg-slope/stdev ratio; `drm-dynamic-rsi-momentum` adapts the RSI *length* (correlation-driven 20–50) against fixed 30/70 cross triggers two-sided, while this record fixes RSI(2) and adapts the *level* itself with a 28-bar time exit long-only; `qqe-fast-slow-cross-two-sided` crosses an ATR-smoothed RSI fast line against its own slow line two-sided with no time exit; `linreg-channel-band-touch-two-sided` trades price against regression channel bands, never an oscillator-against-adaptive-level; `stoch-rsi-kd-zone-cross` and `stochastic-ott-dual-trend` read stochastics, not RSI-vs-slope-scaled-level. No pool record computes `buyLevel x adapK x clamp(slope/stdev)` or holds a long leg for a fixed bar count. Shared `RSI` or `linreg` vocabulary is not shared signal.

## Economic mechanism

### Source-reported

Trend-gated dip acceptance with dispersion shrinkage: the buy level should sit higher during uptrends and lower during downtrends, and it should shrink as price strays far from its mean so volatile stretches emit fewer signals. Bufi's formula makes the level proportional to the trend (linear-regression slope) and inversely proportional to the typical distance of price from its mean (standard deviation), clamped to `±0.5`. The technique adapts the *interpretation* of any oscillator without touching the oscillator's own calculation. The demo applies it to RSI: buy when RSI(2) prints below the adaptive level, hold a fixed 28 bars, and cut on a dollar stop — the fixed-threshold branch exists only as the comparison baseline.

### Research interpretation

Signed-level long-flat with a fixed-horizon hold. Unlike fixed-threshold RSI systems, whose level is a constant an oscillator can always reach, this level carries the trend's sign: in an uptrend the level is positive and dips can trigger; in a downtrend the level goes negative while RSI lives on `0–100`, so no bar can trigger at all — the downtrend is never bought, by arithmetic rather than by a regime filter. Unlike always-in-market flippers, every leg ends by the clock (28 bars), so adverse rides are time-boxed and flat is a first-class resting state between legs. Unlike stop-carrying systems, the derived posture holds each leg to the clock with no mid-leg exit — the honestly priced cost is riding the full 28 bars through adverse moves plus immediate re-entry clustering when the level stays permissive after an exit (see Negative evidence). The bet is on short-horizon RSI(2) dips inside slope-confirmed uptrends with dispersion shrinkage, not on any price pattern, second series, volume read, calendar effect, or volatility breakout.

## Signal

Exact rule as pinned (all inputs frozen — any other value is a different, unpinned rule):

- Declarations (derived): single-position long-flat state machine over `BTCUSDT 1d` with same-bar-close execution and house sizing/costs (see Execution assumptions). At most one open long under the single order id `"long"`; state ∈ {flat, long}; no short state exists anywhere.
- Oscillator, pinned verbatim (`rsiLen = 2`): `osc(t) = ta.rsi(close, 2)(t)` — Wilder-RMA RSI on closes (seed convention fenced by the warmup below; no seed invented).
- Adaptive level, pinned verbatim (`buyLevel = 14`, `adapK = 6`, `adapLen = 8`): `sd(t) = ta.stdev(close, 8)(t)`; `lr(t) = ta.linreg(close, 8, 0)(t)`; `slope(t) = (lr(t) - close(t-8)) / 9`; `BAT(t) = min(0.5, max(-0.5, slope(t) / sd(t)))`; `thrs(t) = 14 x 6 x BAT(t)`, hence `thrs(t)` ∈ `[-42, 42]`. Both estimators read only completed closes; `ta.linreg` is deterministic least squares with offset `0` (no future bar, no negative shift).
- Entry long (BAT branch pinned, `sys = "BAT"` fixed): on bar `t` with `osc(t) < thrs(t)` from flat → open long. While positioned, further sub-threshold bars are rejected no-ops (`pyramiding` default 0, source-pinned). The `"Traditional"` `osc < buyLevel` branch never fires in this record (untraded benchmark — see Negative evidence).
- Exit flat (pinned): `nBar(t) = bar_index(t) - entry_bar_index(t)`, on bar `t` with `exitBars = 28 > 0` and `nBar(t) >= 28` → close `"long"` in full (`"exit"` leg). The `"Stop-loss"` leg is inert by record rule (`DSL = 0`, coded `DSL > 0` guard — see Provenance). No stop, no target, no trailing — explicitly none by record rule, not invented.
- Re-entry: allowed on the very next qualifying bar after any flat (no cooldown specified — explicitly none, not invented).
- Direction: long-only long-flat. No short leg ships anywhere in the block; the short side is disabled by source construction, never by researcher choice. A venue without shorting expresses this rule unchanged.
- Determinism notes: an `na` print (`osc`/`thrs` pre-warmup or degenerate) falsifies the `<` comparison, so no order can fire without full numeric inputs; exact-touch `osc == thrs` is not `<`, so the book carries the prior state (measure-zero on continuous prints — disclosed); a zero-variance 8-bar window (`sd == 0`) yields `na`, which likewise cannot fire (fenced as out-of-scope on BTCUSDT `1d` — see Negative evidence). Entry (flat-only) and exit (positioned-only) are mutually exclusive by machine state on every bar — no same-bar entry/exit conflict exists under any evaluation order.

## Required data

- Completed `1d` bars of BTCUSDT: `close` only — RSI(2), `ta.stdev(close, 8)`, and `ta.linreg(close, 8, 0)` read nothing else. No `open`, no `high`, no `low`, no volume, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line. The `entry_bar_index` counter reads the record's own entry event plus the bar count — a deterministic holding-period clock, not market data.
- Single decision timeframe `1d` (frame-faithful to the SPY-1D demo context; the rule references no other frame, no multi-timeframe input, no `security`-style call of any kind — single-frame by construction).
- Warmup: the binding estimators need 8 completed closes plus the `close(t-8)` reach and the RSI seed; the first fully-formed signal needs roughly 10 bars. The adopted warmup is the first 100 completed `1d` bars flat by record rule (predeclared researcher choice — wide margin over the structural minimum; no seed branch exists to fence beyond this). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. Each bar's close enters the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (researcher-declared per the derived declaration; venue/symbol spelling is naming only, never presented as source-native semantics). The rule is long-only and never shorts, so no short permission is exercised; a spot-only deployment expresses it unchanged.
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar-open (no execution-timing argument ships anywhere — quoted verbatim in Provenance); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill: with the dollar-stop leg inert and no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity, and the entry/exit predicates are mutually exclusive by machine state every bar (see Signal), so each bar's outcome is a single deterministic event (hold, open, or close).
- Engine path for `1d` (gate 5, stated plainly): `1d` is a Binance-documented USDT-M kline interval; the derived rule needs only completed `1d` closes on a single frame — no second timeframe, no unfinished-bar read, no intrabar path, no volume/funding/OI/mark-price leg. The close-only completed-bar same-close primitive is the same verified path as the admitted `1d` records (including the same-bar-close RSI-family and qstick passages); the fixed-bar holding clock is a deterministic bars-since-entry counter, not an engine-state fill dependency. That is the same single-frame completed-bar path as the admitted `1d` records; the RSI/stdev/linreg recursions advance deterministically from known closes, so no hidden lookahead is ever modeled. Anything beyond that single-frame completed-bar path would be a different, unverified claim — none is admitted here.
- Sizing/capital/costs: the code ships tester settings only (`percent_of_equity`/`10`/`slippage = 5` plus the DISCLAIMER's `10% of equity` / `5 ticks` prose — recorded as absent economics, never as zero-cost evidence), so evaluation carries the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions here, never presented as source-native behavior. No safety-order triggers are defined anywhere in this record, so the Safety tranches never add — no DCA events exist in the admitted version. Historical funding is flagged per the house baseline: the pinned V2 simulator's historical-funding path is unproven (`docs/hb-backtest-baseline-v1.0.md` funding section), so funding is modeled, never reported as realized or canonical funding, and never silently zeroed. Each leg holds at most 28 days with flat gaps between legs, bounding funding exposure by construction.
- Concurrency: `pyramiding` default 0 is source-pinned — at most one open long under the fixed order id `"long"`; repeat sub-threshold bars while positioned are rejected no-ops; the time leg closes all; re-entry is allowed on the very next qualifying bar after any flat (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The page ships the full construction (seven pinned inputs with defaults, the `BAT` stdev/linreg/slope/clamp function, `ta.rsi(close, 2)`, the `"Traditional"` vs `"BAT"` entry branches, the single `"long"` order id, the 28-bar `"exit"` close leg, the `DSL`-guarded `"Stop-loss"` close leg, default single-position semantics, and the Bufi/article lineage note with the SPY-1D demo context) — quoted in Provenance. It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — the only performance language is the qualitative observation that adaptivity can help backtests. This record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No performance to carry, admitted plainly: unlike paper-sourced records with backtest tables, the TASC page ships construction, inputs, and trigger semantics only — there is no expectancy number anywhere to fence, and this record claims none.
2. Untraded source content fenced, admitted plainly: the `sys = "Traditional"` branch (`osc < buyLevel` with `buyLevel = 14`) is real source content deliberately not carried into the traded trigger — it is the article's fixed-threshold comparison baseline. The pinned `BAT` level branch is therefore signal-complete by record rule, and carrying the fixed-14 meaning onto it would be fabrication.
3. Dollar-stop exclusion fenced, admitted plainly: the `"Stop-loss"` leg (`profit(0) <= -DSL` with `immediately = true`, default `1600`) is real source content deliberately set inert (`DSL = 0` through the coded `DSL > 0` guard). The default couples SPY-tester dollars to 10%-equity sizing, reads engine-state unrealized profit, and demands immediate intrabar fills — none of which this record models. The derived posture is time-exit-only by record rule (see Limitations for the principal risk this accepts).
4. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=`/`profit=`/`loss=` — with the dollar leg inert, the sole position-closing path is the coded 28-bar `"exit"` leg. The absence is coded and disclosed for the reviewer rather than upgraded into a source claim.
5. Re-entry clustering, admitted plainly: after a time exit, the very next bar with `osc < thrs` re-enters at once — there is no cooldown, no fresh-cross requirement, no re-confirmation delay. A market pinned beneath the adaptive level can compound consecutive 28-bar legs with no flat rest. This is the coded trade, disclosed, not a tunable parameter here.
6. Boundary ties hold their side: exact-touch `osc == thrs` satisfies neither entry nor exit, so no order fires and the book carries the prior state; an `na` print (pre-warmup or degenerate early bars) falsifies every comparison, so no order can fire without full numeric inputs; a zero-variance 8-bar `close` window would zero the stdev denominator, which cannot occur on BTCUSDT `1d` and is fenced as out-of-scope rather than modeled; warmup bars are flat by record rule.
7. State exclusion holds on every bar: entry fires only from flat while the time exit fires only while positioned — no single bar can satisfy both legs under any evaluation order, so no priority rule is needed or invented. (The two `strategy.entry` calls share one order id and opposite `sys` branches, so at most one can fire per bar in this record anyway.)
8. No future leakage in the stack, stated plainly: at decision bar `t`, the estimators read completed closes `t-8..t` (`linreg` offset `0`, `price[length]` reaches back only), the RSI reads closes, and the entry compares prints at `t` — every input is complete at bar `t`'s close. No multi-frame read, no negative index, no full-sample normalization, no repainting path, no calendar read at all. The Wilder-RMA RSI seed is absorbed by the 100-bar warmup, not modeled.
9. RSI/linreg-family overlap fence, admitted plainly: the pool's fixed-threshold RSI records cross constant levels or reverse at extremes with no threshold arithmetic; `drm-dynamic-rsi-momentum` adapts the RSI *length* (correlation-driven 20–50) against fixed 30/70 crosses two-sided with reversal exits; `qqe-fast-slow-cross-two-sided` crosses a smoothed RSI fast line against its own ratcheted slow line two-sided; `linreg-channel-band-touch-two-sided` trades price location against regression bands, never an oscillator against a slope-scaled level. This record fixes RSI(2), scales the *level* by a signed slope/dispersion ratio, exits by the clock, and never shorts. Shared `RSI`/`linreg` vocabulary or shared close inputs are not shared signal.
10. Long-flat posture provably complete: one `"long"` order id with the time-exit close and no short leg anywhere — no third direction exists, and a two-sided reading would contradict the coded order set.
11. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT `1d` futures market pin, the `sys = "BAT"` scope pin, the `DSL = 0` inert stop, same-bar-close fills, the adopted 100-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the RSI(2) oscillator, the BAT construction, all constants, the level entry, the 28-bar exit, the single-position guards, and the long-only stance are source-pinned or predeclared. This record is therefore never evidence that any other market, frame, branch, threshold set, or timing of the source passes.
12. Network limitation disclosed: the rule, inputs, declaration, and lineage lines above were verified in the browser-rendered page (HTTP 200 with badge/title/author/date) and cross-checked against the independently fetched page HTML (HTTP 200, 462660 bytes with `OPEN-SOURCE`/`PineCodersTASC` markers); the linked October-2024 Traders' Tips article page itself was not separately fetched and contributes no rule beyond the lineage already printed in the Pine header. The division of evidence is disclosed here, not hidden.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: RSI(2) on close / BAT(8) with `buyLevel = 14`, `adapK = 6` / signed `±0.5` clamp / sub-threshold level entry / 28-bar time exit / DSL inert / long-only / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Adaptivity relevance: replacing the adaptive `thrs` with the fixed `buyLevel = 14` threshold (same RSI(2), same 28-bar exit, same state machine — the fenced Traditional baseline) must not improve net expectancy; fail ⇒ the slope/dispersion adaptivity adds nothing over the fixed level.
- F2 — Horizon relevance: shortening the time exit to `exitBars = 14` (same level, same entries, same state machine) must not improve net expectancy; fail ⇒ the 28-bar hold adds nothing over a faster clock.
- F3 — Oscillator-length relevance: lengthening the oscillator to RSI(7) (same adaptive level, same 28-bar exit, same state machine) must not improve net expectancy; fail ⇒ the 2-bar dip read adds nothing over a slower oscillator.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (researcher-declared venue family). The rule reads only completed daily closes, so no high/low definition differences and no volume-series differences can touch any order-gating line — but spot-vs-perp close prints can still differ structurally (funding-driven drift, venue aggregation, anomalous prints), so the futures-venue pin is load-bearing and disclosed. The level math is unit-free (a ratio times constants), so no fixed-pip recalibration is needed across assets — cross-asset behavior differences are still real and unclaimed. The rule is long-only with no stop leg, so a spot-only deployment expresses it unchanged. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read beyond each calendar-day bar's own close (no session gating anywhere); decision boundaries are calendar-day bars of the venue feed, disclosed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived market/frame: the source demonstrates on SPY 1D with no venue pin; BTCUSDT `1d` futures is a researcher choice. Results on any other market or frame are a different, unpinned claim.
- Derived fill timing: the source fills next-bar-open evaluated once per completed bar; this record executes same-bar-close on `1d` BTCUSDT. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- Branch scope: the `"Traditional"` fixed-threshold system is performance-unclaimed context; only the `sys = "BAT"` system is admitted here.
- Stop removal: the derived posture holds every leg the full 28 bars with no mid-leg exit — the inert dollar stop is the record's principal risk. Adverse excursion after entry has no guardrail beyond the clock; consecutive 28-bar legs can compound while the level stays permissive.
- Uptrend-only gating: when the BAT level prints negative (downtrend slope), RSI on `0–100` can never print below it, so the system sits flat through downtrends and through high-dispersion stretches that shrink the level — by arithmetic, disclosed, not smoothed.
- Dispersion-definition sensitivity: venue close prints (rolls, aggregation, anomalous prints) flow straight into the slope and stdev legs; a venue that cannot supply trustworthy per-bar closes cannot trade the pinned rule.
- Warmup cost: the adopted 100-bar warmup means the system is blind for the first 100 bars of any `1d` evaluation window (structural minimum roughly 10).
- Performance evidence is absent: neither the page prose (qualitative observation only, no numbers) nor the open-source block reports any number; nothing here is calibrated, fitted, or tuned to any window.
- Licence: the canonical page is an open-source PineCodersTASC Traders' Tips publication (MPL 2.0) — downstream implementation must honor its House-Rules terms; this record copies no code block.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- TradingView PineCodersTASC canonical strategy page, TASC 2024.10 Adaptive Oscillator Threshold — full 61-line open-source block, seven pinned inputs, BAT construction, long-only order set, fixed-bar and dollar-stop close legs, declaration absences, MPL 2.0 lineage header (verified live in browser session and fetched HTML during this cycle; zero crypto claims): https://www.tradingview.com/script/zDP76aFT-TASC-2024-10-Adaptive-Oscillator-Threshold/
- TASC October 2024 Traders' Tips article lineage (`Overbought/Oversold Oscillators: Useless Or Just Misused` by Francesco P. Bufi — attribution printed in the source header; article page itself not separately fetched and contributes no rule here).
