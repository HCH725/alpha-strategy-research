---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: PVT-EMA crossover trend two-sided on BTCUSDT 1d bars
created: 2026-10-11
updated: 2026-10-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-11-27
sources:
  - https://www.fmz.com/strategy/473133
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/PVT-EMA%E8%B6%8B%E5%8A%BF%E4%BA%A4%E5%8F%89%E9%87%8F%E4%BB%B7%E7%AD%96%E7%95%A5-PVT-EMA-Trend-Crossover-Volume-Price-Strategy.md
  - https://www.tradingview.com/pine-script-reference/v5/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# PVT-EMA crossover trend two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (immutable public mirror file plus its recorded FMZ canonical page, fetched 2026-10-11):

- Canonical page: https://www.fmz.com/strategy/473133 (fetched live over HTTPS during this cycle with HTTP 200, 711646 bytes of landing HTML). Page title `PVT-EMA Trend Crossover Volume-Price Strategy | FMZ`; author token `Pakun` × 2; `Created` stamp `2024-11-27 15:01:02` (adopted as `source_as_of`, equal to the mirror's `> Last Modified` stamp 2024-11-27 15:01:02). The page embeds the executable `/*backtest*/` header verbatim: `start: 2019-12-23 08:00:00`, `end: 2024-11-25 08:00:00`, `period: 1d`, `basePeriod: 1d`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]` (each of `Futures_Binance`, `BTC_USDT`, `2019-12`, `2024-11-25` byte-present twice on the page). The ZH/EN prose states the rule twice: PVT accumulates daily price-change percentage times daily volume, a 20-period EMA of PVT is the reference line, PVT crossing above its EMA is the buy signal, crossing below is the sell signal — and admits plainly that the strategy itself sets no stop-loss or take-profit (`策略本身没有设置止损止盈` / `The strategy itself doesn't set stop-loss or take-profit levels`). Word-boundary counts over the whole landing HTML: `PVT` 53, `Crossover` 12, `Sharpe` 0, `Win Rate` 0, `Max Drawdown` 0, `Annualized` 0 — the page ships no performance numbers of any kind.
- Immutable mirror actually executed against (primary code source): repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (verified as the repository head via `git ls-remote` during this cycle — the same head pin as the merged KDJ, STARC, T3-Tillson, WaveTrend, Stochastic-OTT, Qstick, Aroon, SQZMOM-LB, TRIX, Schaff, KST, OBV-EMA and eleven further admissions), exact file path `PVT-EMA趋势交叉量价策略-PVT-EMA-Trend-Crossover-Volume-Price-Strategy.md` (non-ASCII filename preserved verbatim; percent-encoded blob URL in Sources). File 7455 bytes, blob SHA `3ae9eec42325f43e2076e37fda6de8b2e5dc74e0` (verified with `git hash-object` reproducing the identical SHA on re-download, and matching the GitHub contents API `sha`/`size` at the pinned commit). The mirror prints `> Author` = `ChaoZhang` (mirror porter), `> Detail` = https://www.fmz.com/strategy/473133, the `[trans]` prose matching the canonical page rule quoted above, and the code copyright `© PakunFX` inside the Pine block (cited, never redistributed beyond single-line declarations quoted for gate evidence).
- Full `//@version=5` block read in full (order-affecting lines: the `cumVol` guard, the `pvt` cum line, the `emaPVT` line, the two cross edges, two guarded entries; everything else is inputs, render-suppressed plots, or display-only shapes).
- Text census over the pinned code block: 1 `strategy(` (title/shorttitle/`overlay=false`/`calc_on_every_tick=true` plumbing only — no sizing, capital, cost, timing, or pyramiding argument ships anywhere in the declaration) / 2 `strategy.entry` (`"Buy"`/`strategy.long` inside `if (longCondition)`, `"Sell"`/`strategy.short` inside `if (shortCondition)`, no `qty=`/`limit=`/`stop=` qualifiers) / 0 `strategy.exit` / 0 `strategy.order` / 0 `strategy.close` / 0 active `stop=`/`limit=` / 1 `ta.crossover` + 1 `ta.crossunder` (the entry edge pair, nothing else) / 1 `ta.cum` + 1 `ta.change` + 1 `ta.ema` (the full indicator stack) / 2 `volume` (the `cumVol += nz(volume)` guard line and the `* volume` PVT term — no other volume read) / 1 `close` (the `src = close` line; `high`/`low`/`open` 0 — no order-gating line reads them) / 1 `input.int` (`EMA Length = 20`, the sole parameter) / 1 `plot` (the EMA line with `display=display.none`) + 2 `plotshape` (both `display=display.none`) / 0 `security(` / 0 `request.*` / 0 `timeframe(` / 1 `barstate.islast` (inside the no-volume guard only) / 1 `runtime.error` (the guard only) / 1 `var` (the `cumVol` accumulator) / 1 `nz(` (the guard's `nz(volume)`) / 0 `pyramiding` / 0 `process_orders_on_close` / 0 `initial_capital` / 0 `default_qty` / 0 `commission` / 1 `calc_on_every_tick` (quoted verbatim; see derived declaration). No portable economics of any kind ships anywhere — recorded as an absent-economics stub, never as zero-cost evidence.
- Licence and rights: the executable block ships `// This Pine Script™ code is subject to the terms of the Mozilla Public License 2.0` via the public FMZ publication (`© PakunFX`); this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly four: (1) market/frame pin `BTCUSDT 1d` (the executable `/*backtest*/` stanza itself backtests `Futures_Binance BTC_USDT` at `period: 1d`/`basePeriod: 1d` — this pin follows the stanza verbatim; only the symbol spelling is normalized, disclosed here, never presented as source-native); (2) completed-bar decisions with same-bar-close fills (the source ships no execution-timing argument — Pine default evaluates per completed bar and fills on the next bar; no `process_orders_on_close` ships anywhere, quoted verbatim in census — while the declaration's `calc_on_every_tick=true` additionally permits realtime intrabar recomputation whose prints can repaint before the close; this record pins completed-bar evaluation only and claims no realtime intrabar behavior, disclosed here); (3) an adopted 100-bar warmup with pre-warmup bars flat by record rule (covers the EMA20 seed plus the cumulative-PVT baseline transient with margin — see Required data); (4) house sizing/capital/costs replacing the absent source economics (see Execution assumptions). The `ta.cum(ta.change(src) / src[1] * volume)` construction, the `src = close` line, the `20` input, the `ta.crossover`/`ta.crossunder` edge pair, the `"Buy"`/`"Sell"` order path, the full-unit reversal, the two-sided stance, and the no-stop/no-target posture are source-native and unmodified. No tie-break had to be invented: the two edges are provably mutually exclusive on every bar (see Negative evidence), and each bar's outcome is a single deterministic event.

Pre-write dedup (2026-10-11): working-tree case-insensitive searches for `pvt`, `price.volume.trend`, and `473133` return zero hits in any strategy record — no `main` record evaluates a Price-Volume-Trend rule anywhere. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool record `obv-ema-crossover-trend-two-sided-btcusdt-1d` is a different mechanism on five axes: (i) indicator lineage — textbook-style PVT cumulating move-magnitude-weighted volume (`%change × volume`) versus an ATR3-scaled signed-volume-squared cum (`±volume × (volume/atr3)`), a volume-squared-over-ATR normalization PVT never applies; (ii) signal construction — one PVT line against its own single EMA20 versus fast-EMA6/slow-EMA24 dual smoothing of the OBV line; (iii) risk leg — explicitly no stop and no target (prose-admitted) versus a coded 3%-stop-market pair with an arming gate; (iv) position state — always-in-market full-unit reversal with no reachable flat state after the first cross versus a genuine post-stop flat state that waits for the next cross; (v) source identity — PakunFX FMZ 473133 (Nov-2024, native `1d` stanza) versus FMZ 442252 (Feb-2024, `1h` stanza ported to `1d`). The Klinger record is an EMA-difference volume×trend oscillator with trigger semantics, and the CMF record is a bounded money-flow ratio — neither cumulates a price-volume trend line nor crosses it against its own EMA. Not a trivial parameter variant.

## Economic mechanism

### Source-reported

Volume-confirmed trend capture (mirror prose plus code): each bar's percentage price move scaled by that bar's volume is the market's conviction-weighted displacement, and cumulating it into PVT turns a sequence of conviction prints into a persistent trend balance — sustained accumulation with rising prices drags PVT up, distribution drags it down, while large moves on thin volume barely register. The 20-bar EMA of PVT is the slow consensus of that balance; a cross above means fresh conviction is running hotter than its own recent consensus (uptrend ignition), a cross below means conviction has flipped to distribution. The design bets that conviction-weighted flow persists once it confirms above/below its own average, and it carries no stop and no target by the author's own admission — the opposite cross is the sole risk control.

### Research interpretation

Always-in-market conviction-reversal system, edge-triggered, single unit. Unlike the OBV-EMA record, there is no second smoothing to consult, no stop to hide behind, and no flat state to rest in: after the first cross the book is permanently either long or short, and every subsequent opposite cross flips the full unit. Unlike oscillator-cross systems (KDJ, Stochastic-OTT, KST, Schaff) the line being crossed is unbounded and venue-volume-denominated, so the EMA20 reference auto-scales to the asset's own flow regime rather than to a 0–100 rail — chop prints alternating crosses that flip the unit each way, which is the coded cost of the design, disclosed, not smoothed. The bet is on magnitude-weighted volume persistence at the ~month scale under a 20-bar consensus leg, not on any price level, band break, slope test, calendar effect, or second timeframe.

## Signal

Exact rule as pinned (`emaLength = 20` frozen, `src = close` frozen — any other value is a different, unpinned rule):

- Declarations (derived): single-unit always-in-market two-sided machine over `BTCUSDT 1d` with same-bar-close execution and house sizing/costs (see Execution assumptions). State ∈ {flat, long, short}, where flat is reachable only before the first cross fires.
- PVT line, pinned verbatim: `pvt[t] = pvt[t-1] + (close[t] − close[t-1]) / close[t-1] × volume[t]`, i.e. `ta.cum(ta.change(src) / src[1] * volume)` with `src = close`, seeded 0 before the first available bar. Zero-volume bars contribute exactly 0 to the sum by code, disclosed.
- Reference line, pinned verbatim: `emaPVT = ta.ema(pvt, 20)` (Pine `ema`, α = 2/21, SMA-seeded at 20 bars, `na` before — `na` comparisons are false so no edge can fire pre-seeding, coded behavior, disclosed).
- Entry long, pinned verbatim: `longCondition(t) = ta.crossover(pvt, emaPVT)(t)` — `pvt[t-1] ≤ emaPVT[t-1]` and `pvt[t] > emaPVT[t]` — fires `strategy.entry("Buy", strategy.long)`; from short it reverses the full unit, from flat it opens, from long (no pyramiding ships anywhere) no additive exposure can print.
- Entry short, pinned verbatim: `shortCondition(t) = ta.crossunder(pvt, emaPVT)(t)` — strict mirror — fires `strategy.entry("Sell", strategy.short)` with symmetric reversal semantics.
- Exits and risk, pinned verbatim: there are none besides the opposite cross — zero `strategy.exit` legs, zero `stop=`/`limit=` qualifiers, and the prose admits no stop-loss and no take-profit. No trailing, no time exit, no cooldown — pinned as written, explicitly none, not invented.
- Direction: two-sided with resting flat only pre-first-cross. A long-only reading would contradict the `"Sell"`/`strategy.short` leg and is explicitly not this record.

## Required data

- Completed `1d` bars of BTCUSDT: `close` (the PVT displacement source) and `volume` (the conviction weight — standard per-bar kline volume, point-in-time at the close with no leakage). No `open`, no `high`, no `low`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (derived pin following the stanza's own `period: 1d`/`basePeriod: 1d`; the body contains no `security(`/`request.*` call, so the derived rule is single-frame by construction).
- Warmup: the binding seed is the EMA20 SMA-seed (20 completed bars) behind the cumulative PVT baseline transient (additive constants pass through the line-minus-EMA comparison with decaying weight). The adopted warmup is the first 100 completed `1d` bars flat by record rule (predeclared researcher choice — 5× the slow length with margin; no traded bar reads a seeded value). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. The `calc_on_every_tick=true` realtime path is excluded by the derived declaration — historical evaluation uses completed-bar values only.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (derived pin following the executable header's own `Futures_Binance BTC_USDT` venue at `period: 1d` — venue transfer and symbol spelling are disclosed here, never presented as source-native). Both sides are explicit legs, so a spot-only deployment expresses the long half unchanged while the short half stays venue-gated (short permission unused, never silently converted) — disclosed.
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar fill (no execution-timing argument ships anywhere — quoted verbatim in census), and its `calc_on_every_tick=true` declaration additionally allows realtime intrabar prints; this record claims neither the source fill timing nor any intrabar behavior. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity, and the two edges are mutually exclusive per bar (see Negative evidence), so each bar resolves to at most one order event.
- Sizing/capital/costs: the source ships no portable economics of any kind (no `initial_capital`, no `default_qty`, no commission/slippage/funding argument ships anywhere — recorded as an absent-economics stub, never as zero-cost evidence) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: single-unit machine by default no-pyramiding construction — at most one full-unit position; each cross flips it. Reversal is immediate on the next opposite cross (no cooldown specified — explicitly none, not invented). No flat state is reachable after the first cross except by house-level intervention, which would be a separately declared experiment. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The mirror ships the full construction (the `cumVol` guard, the `ta.cum(ta.change(src)/src[1]*volume)` line, `src = close`, the `20` input, the `ta.crossover`/`ta.crossunder` edge pair, the `"Buy"`/`"Sell"` entries, the render-suppressed plots, and the 2019-12-23→2024-11-25 `1d`/`1d` Binance backtest header), the author/title stamps, and the bilingual rule prose with its explicit no-stop/no-target admission. It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden risk layer: the body contains zero `strategy.exit` legs and zero `stop=`/`limit=` qualifiers, and the prose independently admits no stop-loss and no take-profit. The no-stop/no-target posture is prescribed, explicitly none, never hidden.
2. Mutual-exclusion proof, stated plainly: `crossover` requires `pvt[t-1] ≤ emaPVT[t-1]` with `pvt[t] > emaPVT[t]`; `crossunder` requires `pvt[t-1] ≥ emaPVT[t-1]` with `pvt[t] < emaPVT[t]`. Both true would require `pvt[t-1] = emaPVT[t-1]` jointly with `pvt[t]` strictly above and strictly below the reference — impossible on every bar, including equal-print bars (an exact touch with no penetration fires neither edge). No researcher precedence was invented: the shipped long-`if`-before-short-`if` order never arbitrates a real tie.
3. Edge-not-latch fenced: both conditions are `ta.crossover`/`ta.crossunder` (fire only on the cross bar), not a `pvt > emaPVT` holding state — post-cross bars with PVT still above its EMA satisfy no entry guard, so no bar can open twice and no priority rule against any exit is needed.
4. na determinism fenced: before the EMA20 seed both edges resolve false by Pine `na` comparison semantics; the first-bar `src[1] = na` makes the first PVT addend `na`, absorbed inside the warmup flat. No seeded or `na` value ever trades — structural, disclosed, never a researcher tie-break.
5. Zero-volume and degenerate bars fenced: zero-volume bars add exactly 0 to the cum by code; a zero price change adds exactly 0. `close[t-1] = 0` (division by zero) is unencounterable on `1d` BTCUSDT outside a venue outage — disclosed, not modeled.
6. `calc_on_every_tick` fenced: the declaration permits realtime intrabar recomputation, so live prints before the close could differ from the closed-bar value. This record pins completed-bar evaluation only (predeclared adaptation) and makes no claim about realtime intrabar signals — the FMZ stanza backtest itself executes on completed `1d`/`1d` bars, so the historical semantics pinned here match the stanza's, disclosed, not hidden.
7. `cumVol`/guard/display fenced: the `var cumVol` accumulator, the `barstate.islast` no-volume `runtime.error`, the `overlay=false` plumbing, and the three render-suppressed plots/shapes feed no order condition — counted in census, excluded from the rule, disclosed.
8. No future leakage in the stack, stated plainly: at decision bar `t` the slowest input is the EMA20 seed resolving at bar `t`'s close — every input is complete at the close. No `security()`, no `request.*`, no negative index, no `barstate`-gated order path. All `plot`/`plotshape` calls are render-suppressed (`display.none`) and drive no order.
9. Always-in-market posture provably complete: after the first cross the code paths admit only long→short and short→long flips under default no-pyramiding — no flat state is reachable by code. Any flat-holding reading would contradict the shipped declaration and is explicitly not this record.
10. Derivation boundary fenced: the only non-source-native behaviors in this record are the `BTCUSDT 1d` market/frame pin, completed-bar same-bar-close fills with the realtime-intrabar exclusion, the adopted 100-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the PVT formula, `src = close`, the `20` input, the strict cross edge pair, the `"Buy"`/`"Sell"`-id order path, full-unit reversal, two-sided direction, and the risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, or timing of the source passes.
11. Network limitation disclosed: every formula line above was byte-verified in the pinned mirror file at commit `7853bb2` (7455 bytes, blob SHA recorded, `git hash-object` identical on re-download, contents-API `sha`/`size` matched); the FMZ canonical page verified live the title, the `Pakun` token, the `Created` stamp, the PVT/EMA crossover rule prose with its no-stop/no-target admission, the `Futures_Binance BTC_USDT` `1d`/`1d` backtest stanza, and the absence of any performance numbers — the division of evidence is disclosed here, not hidden.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `ta.cum(ta.change(close)/close[1]*volume)` / `src = close` / EMA 20 / strict `ta.crossover`/`ta.crossunder` edge pair / opposite-cross-only exits / no-stop-no-target posture / always-in-market two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Volume-weight relevance: replacing PVT with a plain close-EMA20 cross (same 20 length, same reversal, same risk posture) must not improve net expectancy; fail ⇒ the volume conviction-weighting adds nothing over a price-only cross.
- F2 — Consensus-length relevance: replacing the 20-bar PVT-EMA with a slow 50-bar PVT-EMA (same line, same edges, same risk posture) must not improve net expectancy; fail ⇒ the pinned fast consensus adds nothing over a slow reading of the same line.
- F3 — Reversal-vs-hold relevance: replacing the always-in-market flip with cross-to-flat holding (exit long on the short cross to flat, re-enter only on the next long cross, shorts disabled — a different, separately specified posture) must not improve net expectancy; fail ⇒ staying inverted through distribution adds nothing over holding flat between crosses.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (derived pin following the executable header's own `Futures_Binance BTC_USDT` venue at `period: 1d`/`basePeriod: 1d`). The PVT arithmetic ports across perpetual venues without structural change, but venue volume-reporting differences touch `volume[t]` and hence every PVT print, every EMA value, and every cross — disclosed above, not hand-waved. The cumulation auto-scales in the asset's own flow units, so no fixed-pip recalibration is needed across assets — cross-asset behavior differences are still real and unclaimed. Both sides are explicit legs, so a spot deployment expresses the long half unchanged while the short half stays venue-gated — disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no session gating anywhere); decision boundaries are calendar-day bars of the venue feed, disclosed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source fills next-bar with no timing argument and declares `calc_on_every_tick=true`; this record executes completed-bar same-bar-close on `1d` BTCUSDT and claims no realtime intrabar behavior. Backtest economics of the timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- Derived market and frame: the stanza backtests `Futures_Binance BTC_USDT` at `1d`/`1d`; this record pins `BTCUSDT 1d` with normalized symbol spelling. Cross-market and cross-frame behavior differences are real — the adaptation is disclosed, and this record makes no claim about any other market, frame, or base period.
- Always-in-market commitment: after the first cross the book is permanently positioned with the opposite cross as the sole control — adverse excursion has no stop beyond the next flip, and chop prints alternating full-unit flips. This is the prescribed posture (prose-admitted, zero coded exits), disclosed as the principal risk — not smoothed, not supplemented.
- No source economics: beyond the bare `strategy(...)` title plumbing the source ships no capital, sizing, commission, slippage, funding, or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Seed coverage: the EMA20 seed plus the cumulative baseline transient settle within dozens of bars; the first 100 `1d` bars are flat by record rule, so early-history signals never enter any evaluation.
- Volume-venue dependence: the rule reads per-bar kline volume directly — a venue or feed whose volume prints differ (wash filters, reporting gaps, outage zeros) changes every downstream value. Zero-volume outage bars contribute 0 by code rather than by estimation — disclosed, not interpolated.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- FMZ canonical strategy page (rule prose with no-stop/no-target admission plus `Futures_Binance BTC_USDT` 1d/1d backtest stanza verified live via HTTP-200 page record): https://www.fmz.com/strategy/473133
- Immutable mirror file at pinned commit `7853bb2bf262c4567ac238d3552d97f0e50cb801` (blob `3ae9eec42325f43e2076e37fda6de8b2e5dc74e0`, 7455 bytes): https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/PVT-EMA%E8%B6%8B%E5%8A%BF%E4%BA%A4%E5%8F%89%E9%87%8F%E4%BB%B7%E7%AD%96%E7%95%A5-PVT-EMA-Trend-Crossover-Volume-Price-Strategy.md
- Pine strategy semantics (order calls, default execution, `calc_on_every_tick`, built-in `ta.cum`/`ta.change`/`ta.ema`/`ta.crossover`/`ta.crossunder` semantics): https://www.tradingview.com/pine-script-reference/v5/
