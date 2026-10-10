---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Laguerre RSI cu-cd cross reversal two-sided on BTCUSDT 1d bars
created: 2026-10-10
updated: 2026-10-10
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-12-19
sources:
  - https://www.fmz.com/strategy/435868
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/拉盖尔RSI交易策略Laguerre-RSI-Trading-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Laguerre RSI cu-cd cross reversal two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (canonical FMZ page plus public GitHub mirror, fetched 2026-10-10):

- Canonical page: https://www.fmz.com/strategy/435868 (page title `Laguerre RSI Trading Strategy`, public `Common strategy`, `Created: 2023-12-19 14:04:46` — adopted as `source_as_of` 2023-12-19; publisher `ChaoZhang`). Fetched over HTTPS during this cycle (781141 bytes): the page carries the full bilingual prose (Ehlers Laguerre-filter RSI construction, `L0`–`L3` recursion, `cu`/`cd` integrals, `LaRSI = cu / (cu + cd)`, the 20/80 prose rule), the Strategy Arguments table (`v_input_1_close = 0` → Source `close`; `v_input_2 = 0.2` → Alpha; `v_input_3 = false` → Change Color; date-window inputs From 2020-01-01 To 9999-01-01), and the page-embedded `/*backtest*/` header (`start: 2022-12-12 00:00:00`, `end: 2023-12-18 00:00:00`, `period: 1d`, `basePeriod: 1h`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`). The page's code viewer is login-gated (`Login to view full source`), so the executable block below was read from the public GitHub mirror and cross-checked field by field against the canonical page's prose, argument table, and backtest header — all consistent. Word-boundary counts over the whole canonical landing HTML: `Sharpe` 0, `Net Profit` 0, `Win Rate` 0, `Max Drawdown` 0, `Profit Factor` 0, `Annual` 0 — the page ships no quantitative performance numbers of any kind (adopted as no claimed performance anywhere in this record; the prose's qualitative `perform well` language is marketing text with no table, figure, or number and is never treated as evidence).
- Executable block (verbatim from the mirror): `strategy("Laguerre RSI", shorttitle="LaRSI", overlay=false)`, `//@version=3`, `src = input(title="Source", defval=close)`, `alpha = input(title="Alpha", type=float, minval=0, maxval=1, step=0.1, defval=0.2)`, `colorchange` default false, `gamma = 1 - alpha`, the four recursion lines (`L0 := (1-gamma) * src + gamma * nz(L0[1])`, `L1 := -gamma * L0 + nz(L0[1]) + gamma * nz(L1[1])`, `L2`, `L3` likewise), `cu` / `cd` three-term sums, `temp = cu+cd==0 ? -1 : cu+cd`, `LaRSI = temp==-1 ? 0 : cu/temp`, the 20/80 `plot` pair (render-only), and the live order pair `strategy.entry("Long", true, when = window1() and crossover(cu, cd))` / `strategy.entry("Short", false, when = window1() and crossunder(cu, cd))` with `window1()` a date-window convenience gate defaulting to 2020-01-01 → 9999-01-01 (always true in any real evaluation — see derived declaration). Code headers credit `© mertriver1`, `Developer: John EHLERS`, `Author: Kivanc Ozbilgic`, under an MPL-2.0 notice; no licence grant beyond the visible publication is claimed.
- Text census over the executable block: 2 `strategy.entry` (the Long/Short pair quoted above, no `qty` argument on either) / 0 `strategy.close` / 0 `strategy.exit` / 0 `strategy.order` / 0 `request.*` (single-frame by construction) / 0 `volume` reads / 0 `time(` gates (the only time use is the builtin `time` inside the always-on `window1()` convenience gate — see derived declaration) / 10 `input(` declarations (Source, Alpha, Change Color, plus the seven date-window conveniences) / `pyramiding`, `process_orders_on_close`, `calc_on_every_tick`, commission and slippage appear nowhere (Pine v3 language defaults govern: see Signal). The `overlay=false` flag and the `100*LaRSI` / `20` / `80` plots render only and gate no order.
- GitHub mirror corroboration: `fmzquant/strategies` file `拉盖尔RSI交易策略Laguerre-RSI-Trading-Strategy.md` at commit `7853bb2bf262c4567ac238d3552d97f0e50cb801` (2025-04-30; file history latest `87a415edf7b08065fbcbfbfefb7351cd929e4dbd`, 2024-03-03), whose `Detail` field points back to `https://www.fmz.com/strategy/435868` and whose `Last Modified` reads 2023-12-19. The mirror's Pine block matches the canonical page's prose formulas, argument defaults, and backtest header exactly.
- No `©` republication beyond single-line declarations quoted for gate evidence; this record cites and normalizes the rule and reproduces no source block beyond the short declarations above.

Licence and rights: the canonical page is a public FMZ strategy publication and the mirror is a public GitHub implementation file (code under an MPL-2.0 notice). This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly five: (1) same-bar-close fills (the source sets no execution-timing argument anywhere, so source fills are next-tick by language default); (2) removal of the `window1()` date-window convenience gate as always-active (defaults From 2020-01-01 To 9999-01-01 never bind in any real evaluation — behavior-neutral, predeclared); (3) an adopted 60-bar warmup with pre-warmup bars flat by record rule (covers the four-tap recursion plus `nz` seeding transient — see Required data); (4) house sizing/capital/costs replacing the source economics (live code passes no `qty`: Pine v3 default one fixed unit; no commission, fee, slippage, margin, or funding assumption ships anywhere — see Execution assumptions); (5) venue naming normalization only (`BTC_USDT` → `BTCUSDT`). There is deliberately NO timeframe adaptation (source header `period: 1d`; derived frame `1d`), NO alpha/src/formula change (`0.2`/`close`/Laguerre four-tap frozen), and NO stop/target/filter/cooldown addition (the prose's stop-loss wishes live under future optimizations only). The Laguerre arithmetic, the `cu`/`cd` cross predicates, and the Long/Short order pair are source-verbatim.

**Code-over-prose pin (material, predeclared):** the page prose trades the plotted bands (`Go long when Laguerre RSI crosses above 20, and go short when Laguerre RSI crosses below 80`), but the executable code enters on `crossover(cu, cd)` / `crossunder(cu, cd)` — i.e. the up/down integrals crossing each other, which is exactly LaRSI crossing the 0.5 midline, not the 20/80 bands (the 20/80 plots gate no order anywhere). The derived spec follows the executable code and excludes the prose 20/80-band rule from all order logic. A genuine 20/80-band-cross variant would be a different, unpinned rule — none is admitted here.

Pre-write dedup (2026-10-10): working-tree case-insensitive word-boundary searches for `\blaguerre\b` return zero strategy hits (the sole mention anywhere is a dedup sentence inside the RWI record) — no admitted rule uses this source, author publication, indicator, or mechanism. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `tsi-signal-cross-reversal-btcusdt-1h-2026-10-06.md` smooths one RSI into a double-smoothed TSI against its own signal line; `qqe-fast-slow-cross-two-sided-btcusdt-1d-2026-10-09.md` crosses fast/slow QQE lines with an ATR-trailing threshold; `rsi-classic-level-reversal-btcusdt-1h-2026-10-05.md` trades classic-RSI level excursions; `stochastic-ott-dual-trend-btcusdt-1d-2026-10-09.md` pairs a stochastic with an OTT band — none evaluates a four-tap Laguerre filter-bank ratio with integral-pair midline crosses. Four-axis distinction: signal construction differs (Laguerre polynomial filter bank `L0`–`L3` with `gamma = 0.8` feeding the `cu/(cu+cd)` ratio versus stochastic/smoothed-RSI/QQE/OTT constructions — no pool record evaluates a Laguerre bank), trigger differs (`crossover`/`crossunder` of the `cu`/`cd` integral pair, i.e. the 0.5 midline, on single-bar pulses versus band touches or signal-line crosses), exits differ in event set (reversal-only via the opposite integral cross with no stop/target/trailing/time leg of any kind), and source identity differs (FMZ 435868 December-2023, Ehlers/Ozbilgic lineage, versus other FMZ IDs or TV authors).

## Economic mechanism

### Source-reported

Laguerre-filter RSI: John Ehlers' Laguerre transform builds four recursive filter legs (`L0`–`L3`) from price with a single damping coefficient (`alpha`, default 0.2); the up integral `cu` and down integral `cd` accumulate same-direction leg steps, and their ratio `cu/(cu+cd)` is an RSI-like 0–1 oscillator that reaches extremes faster than classic RSI (less data needed per the prose) while the recursion smooths noise. The coded bet is integral dominance: long when the up integral takes over (`crossover(cu, cd)`), short when the down integral takes over (`crossunder(cu, cd)`).

### Research interpretation

Pulse-triggered (not state-following, not level-holding) two-sided reversal system with no price stop, target, trailing, or time exit — flat until the first integral cross, then always positioned, flipping only on the opposite cross. Unlike level systems (classic RSI bands, the prose's own 20/80 language) it never buys oversold levels or sells overbought levels; the only events are the two midline integral crosses. Unlike state systems (RWI, SSL) that re-assert every bar, cross pulses fire on single bars only — a persisting dominance without a fresh cross does nothing. Unlike smoothed-oscillator-cross systems (TSI, QQE) the oscillator is a four-tap Laguerre-bank ratio at `alpha = 0.2`, reaching full-scale 0/1 far faster than an RSI-derived line — whipsaw across the midline in chop is the record's principal admitted cost.

## Signal

Exact rule as pinned (`alpha = 0.2` / `src = close` frozen — any other value or source is a different, unpinned rule):

- Declaration (derived): Pine v3 semantics (`//@version=3` ships in the block; `nz(x)` yields 0.0 on leading `na`; literal `true`/`false` are the long/short direction arguments). The `strategy(...)` header carries no `pyramiding`, `process_orders_on_close`, or `calc_on_every_tick` argument — v3 defaults govern (no same-direction adds; exactly one evaluation per completed bar). No `qty` ships on either entry — v3 default one fixed unit, replaced by the house overlay in derived evaluation (see Execution assumptions, predeclared).
- Indicator arithmetic (pinned, source-verbatim, single-TF): `gamma = 0.8`; `L0 := 0.2 * close + 0.8 * nz(L0[1])`; `L1 := -0.8 * L0 + nz(L0[1]) + 0.8 * nz(L1[1])`; `L2 := -0.8 * L1 + nz(L1[1]) + 0.8 * nz(L2[1])`; `L3 := -0.8 * L2 + nz(L2[1]) + 0.8 * nz(L3[1])`; `cu = (L0>L1 ? L0-L1 : 0) + (L1>L2 ? L1-L2 : 0) + (L2>L3 ? L2-L3 : 0)`; `cd` mirror-image; `LaRSI = (cu+cd==0) ? 0 : cu/(cu+cd)` — all on BTCUSDT `1d` bars (source header `period: 1d`; no `request.*` call anywhere).
- Entry long: `window1() and crossover(cu, cd)` → `strategy.entry("Long", true)` — fires on the single bar the up integral crosses above the down integral (equivalently, LaRSI crossing above 0.5 given nonzero denominators); same-bar-close execution under the derived declaration. Flat before the first cross by construction.
- Entry short / reversal: `window1() and crossunder(cu, cd)` → `strategy.entry("Short", false)` — fires on the single bar the down integral crosses above the up integral (LaRSI crossing below 0.5); while long it closes the full long and opens the full short in the same execution step (full reversal, no residual leg). `crossover` and `crossunder` of the same pair are mutually exclusive on every bar by construction, so no bar can ever fire both legs — no same-bar ordering ambiguity exists anywhere in this record. The measure-zero edge `cu == cd` on consecutive bars fires neither leg and the position simply holds — stated, not patched. The `cu+cd == 0` edge pins `LaRSI = 0` by coded ternary (occurs only in the `nz`-seeded leading transient, inside the adopted warmup flat) — never patched with a guard constant.
- Pyramiding irrelevance (pinned, not assumed): a second `crossover(cu, cd)` cannot occur without an intervening `crossunder(cu, cd)` (a cross requires the opposite inequality on the prior bar), and the intervening crossunder reverses any open long first — same-direction double-entry is impossible by signal construction, so the v3 no-add default never binds beyond the coded pulses. No cooldown is specified — explicitly none, not invented.
- Risk legs (pinned absence, not invented): 0 `strategy.close`, 0 `strategy.exit`, 0 `strategy.order` ship anywhere — the derived posture is explicitly no stop, no target, no trailing, no time exit; the prose's stop-loss and filter suggestions (`Add stop loss mechanisms`, `Combine other indicators`) live under future optimizations as wishes, never rules, and none is adopted here.
- Direction: two-sided long/short with symmetric pulse reversal. Futures venue required for the short leg (source venue is already `Futures_Binance BTC_USDT` — pinned).
- Display isolation: `overlay=false`, the `100*LaRSI` line, the 20/80 band plots, and the `colorchange` ternary render only and cannot change any order.

## Required data

- Completed `1d` bars of BTCUSDT: `close` only (sole series read by any order-gating line — `src` defaults to `close` and the argument table pins index 0; `high`, `low`, `open`, `volume` are read nowhere). No funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (0 `request.*` calls).
- Single decision timeframe `1d` (source chart header `period: 1d`; `basePeriod: 1h` equals native 1h execution granularity — 24 hourly bars per 1d bar on a 24/7 venue — and with pulse-only reversal entries plus zero intrabar-conditional legs, no intrabar path exists for the base to affect; pinned as irrelevant, not modeled).
- Warmup: the four-tap recursion with `nz` zero-seeding needs a seeding transient (leading bars pin `cu = cd = 0`, `LaRSI = 0` by the coded ternary). The adopted warmup is the first 60 completed `1d` bars flat by record rule (predeclared researcher choice — covers recursion settling margin several times over at `gamma = 0.8`); no cross before bar 61 may trade. No repainting (`close` read only on completed bars), no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (source venue is already `Futures_Binance BTC_USDT` on the source `1d` chart frame — naming normalization to `BTCUSDT` is the only market change; formula, alpha, source, and frame are verbatim, never presented as anything but the coded rule).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-tick (no execution-timing argument ships anywhere); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill: with mutually exclusive single-bar cross pulses and no stop/target legs, there is no same-bar ordering ambiguity of any kind. `1d` is a supported pinned-engine interval (current campaign already screens `1d`).
- Sizing/capital/costs: the source ships no live sizing argument (both entries omit `qty`; v3 default one fixed unit) and no commission, fee, slippage, margin, or funding assumption anywhere. The explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all) apply to the derived evaluation here, with the single-unit/no-add/reverse-full position pin from Signal, never presented as source-native behavior.
- Concurrency: at most one unit per side under the fixed order IDs `Long`/`Short` (same-direction re-entry impossible by cross-pulse construction; the v3 no-add default restated as record rule, predeclared); the opposite integral cross reverses in full in one step; re-entry after a reversal needs only the next opposite cross (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The short leg requires margin-short permission, realistic on the pinned perpetual venue.

## Evidence

### Source-reported

The page ships the full construction (v3 header, `Laguerre RSI` working title, `overlay=false`, Source/Alpha/Change-Color inputs, `gamma = 1 - alpha` four-tap recursion with `nz` seeding, `cu`/`cd` three-term integrals, the `temp`/`LaRSI` ternary, the 20/80 render plots, the Long/Short `crossover`/`crossunder` order pair with the always-on date-window gate, mertriver1/Ehlers/Ozbilgic credit lines with MPL-2.0 notice, the 1d/1h Dec-2022→Dec-2023 backtest header on `Futures_Binance BTC_USDT`, bilingual Laguerre-RSI prose). It ships zero quantitative performance numbers: no return, no win rate figure, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.close`, 0 `strategy.exit`, 0 `strategy.order` — the sole position-changing path is the opposite integral cross reversing the full unit. The absence of any live stop is coded absence, disclosed, not a tunable parameter here.
2. Always-positioned exposure after the first cross, admitted plainly: the system holds a side until the opposite cross — a market that trends against the entry keeps the full unit on with no guardrail beyond the next cross, which may arrive many bars later or after deep excursion. Chop that alternates `cu`/`cd` dominance across the midline flips the full unit repeatedly; the Laguerre bank reaches full-scale faster than classic RSI, so midline whipsaw is the principal admitted cost. This is the coded trade, disclosed, not a tunable parameter here.
3. Prose/code divergence fenced: the page prose's 20/80-band-cross rule (`crosses above 20` long / `crosses below 80` short) is contradicted by the executable entries (integral-pair cross ⟺ 0.5 midline). The derived spec follows the code; a genuine 20/80-band variant would be a different, unpinned rule — none is admitted here. The plotted 20/80 lines are display only.
4. Date-window gate removed as behavior-neutral, fenced: `window1()` defaults (From 2020-01-01 To 9999-01-01, confirmed in the argument table) never bind in any real evaluation; dropping the convenience gate changes no event. A genuinely window-gated variant would be a different, unpinned rule — none is admitted here.
5. Derivation boundary fenced: the only non-source-native behaviors in this record are same-bar-close fills, the always-on date-gate removal, the adopted 60-bar warmup with record-rule pre-warmup flat, venue naming normalization, and house sizing/costs — all predeclared above; the `0.2`/`close` literals, the `gamma = 0.8` four-tap recursion, the `nz` seeding, the `temp`/`LaRSI` ternary, the `crossover`/`crossunder` predicates, the Long/Short order pair, the `cu == cd` / `cu+cd == 0` hold edges, and the no-stop/no-target/no-cooldown stance are source-verbatim. This record is therefore never evidence that any 20/80-band, next-tick-fill, or window-gated reading of the source itself passes.
6. The `0.2` / `close` literals, the four-tap construction (not a shallower/deeper bank), the integral-pair midline trigger (not band touch, not level hold), the full-unit reversal, the two-sided stance, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning any literal, converting pulse-crossing into state-following or band-trading, adding a stop/target/filter/cooldown/gate, dropping the short leg, flipping to the prose's 20/80 bands, or sizing partially instead of full-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `alpha = 0.2` / `close` / four-tap Laguerre bank / `cu`-`cd` midline-cross pulses / full-unit reversal / two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Trigger relevance: replacing the pinned integral-pair cross (0.5 midline) with the prose's 20/80-band crosses under the identical bank must not improve net expectancy; fail ⇒ the coded trigger carries no advantage over its prose alternative and the code-over-prose pin is unmoored.
- F2 — Filter relevance: replacing the pinned Laguerre bank (`alpha = 0.2`) with a classic-RSI midline cross at comparable responsiveness must not improve net expectancy; fail ⇒ the Laguerre construction adds nothing over plain RSI.
- F3 — Direction relevance: replacing the coded dominance-following direction (long on up-integral takeover) with its fade (long on down-integral takeover) under the identical gate must not improve net expectancy; fail ⇒ the executable direction adds nothing over its mirror and the rule is direction-arbitrary.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision frame source-native `1d`; no signal-series adaptation of any kind — predeclared section above lists all five derivations, none touching frame or formula). The close-price recursion ports across perpetual venues without structural change. The short leg requires margin-short permission (realistic on perpetual venues; a spot-only deployment cannot express the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no session gating beyond the removed always-on date window), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source fills next-tick on a 1d-decision/1h-base backtest; this record executes same-bar-close on `1d` BTCUSDT perpetual. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden.
- Date-gate removal: the source's `window1()` convenience inputs are dropped as always-active at defaults; any evaluation window that would actually bind the 2020→9999 defaults is outside real use — disclosed, not hidden.
- Position-state pin: restates the v3 no-add default plus single-unit/reverse-full as record rule; live same-side-add quantity behavior beyond the default is unreachable-by-construction (alternating pulses) and the pin is a researcher restatement where it goes beyond the coded pulses, disclosed, not source-verbatim.
- Prose/code divergence: the 20/80-band rule exists only in prose and is excluded here — a reader trusting the prose alone would reconstruct the opposite-timing, unpinned rule.
- No price stop, no time stop, always positioned after the first cross: adverse excursion after entry has no guardrail beyond the opposite integral cross, which may arrive many bars later or after deep excursion; alternating chop across the midline flips the full unit repeatedly. This is the coded posture, disclosed as the record's principal risk.
- No source cost declaration: no live capital, commission, fee, slippage, margin, or funding assumption ships anywhere in the active code — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Venue naming only: the source venue is already `Futures_Binance BTC_USDT`; the derived venue is Binance `BTCUSDT` perpetual. Microstructure, tick size, fee, and funding differences are carried by the house overlay — no equivalence is claimed.
- One-year source backtest window (Dec-2022→Dec-2023 header) is a page setting, not a strategy rule: it bounds no derived claim and this record draws no performance inference from it.

## Implementation status

Not implemented. No Hummingbot controller/executor has been written for this record; no Qlib screening, parity run, Paper, Testnet, or live deployment is authorized or claimed. Admission PASS (upon independent review) means model-consistent research admissibility under the pinned engine assumptions above — nothing more.

## Adoption boundary

- `status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. This record is not authorization to trade, allocate capital, or deploy to any live, paper, or test venue.
- Downstream eligibility (Qlib screening after event-level parity, Hummingbot re-validation, survivor promotion) is governed solely by the repository's downstream contract and is never implied by this record alone.
- Any parameter, frame, market, direction, fill-timing, or risk change versus the pinned rule above constitutes a different, unpinned strategy requiring its own record and review.

## Related Wiki records

None. No Wiki Brain ingestion was performed for this record (Scout PR-only workflow performs no intake review or wiki writes).

## Sources

- https://www.fmz.com/strategy/435868 — canonical FMZ strategy publication (`Laguerre RSI Trading Strategy`, Created 2023-12-19 14:04:46; prose, Strategy Arguments table, and page-embedded backtest header `period: 1d`, `basePeriod: 1h`, `Futures_Binance BTC_USDT`, Dec-2022→Dec-2023 window read from the page fetched 2026-10-10; page code viewer login-gated).
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/拉盖尔RSI交易策略Laguerre-RSI-Trading-Strategy.md — public GitHub mirror carrying the verbatim Pine v3 block (`Laguerre RSI` / `LaRSI`, `alpha = 0.2`, `src = close`, `crossover(cu, cd)` Long / `crossunder(cu, cd)` Short; code © mertriver1, Developer John Ehlers, Author Kivanc Ozbilgic, MPL-2.0 notice), `Detail` link back to FMZ 435868.
- https://www.tradingview.com/pine-script-reference/v5/ — Pine builtin semantics reference (v3-era `nz`/`strategy.entry`/`crossover` behavior as observed in the source block).
