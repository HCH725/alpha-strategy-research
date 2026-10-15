---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: PPO 12-26-9 signal-line cross reversal two-sided on BTCUSDT 1d bars
created: 2026-10-15
updated: 2026-10-15
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-15
sources:
  - https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/percentage-price-oscillator-ppo
  - https://www.wealthcharts.com/kb/category/charts/indicator-formulas/Percentage-Price-Oscillator-PPO-Indicator-Formula
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# PPO 12-26-9 signal-line cross reversal two-sided on BTCUSDT 1d bars

## Provenance

Primary sources read end to end (both fetched live over HTTPS during this cycle, 2026-10-15):

- StockCharts ChartSchool, `Percentage Price Oscillator (PPO)` documentation page, fetched live (HTTP 200, 797436 bytes). Ships the full construction: `Percentage Price Oscillator (PPO): {(12-day EMA - 26-day EMA)/26-day EMA} x 100`; `Signal Line: 9-day EMA of PPO`; `PPO Histogram: PPO - Signal Line`. Pins the display triple (signal line, histogram, centerline) and the signal taxonomy (`Trading signals are generated with signal line crossovers, centerline crossovers, and divergences`, shared with MACD). Pins the normalization thesis (`PPO readings are not subject to the price level of the security`; readings of different securities can be compared despite large price differences) and the close basis (`Closing prices are used to calculate the moving averages and, therefore, PPO signals should be measured against closing prices`; a `9-day EMA of PPO is plotted as a signal line to identify upturns and downturns in the indicator`). Page-wide census: `Sharpe` 0, `Net Profit` 0, `Profit Factor` 0, `Win Rate` 0, `Annualized` 0, `Max Drawdown` 0, `backtest` 0 — every `return`/`performance` hit is site chrome or an unrelated-indicator nav entry, never a PPO expectancy number. Both pages are living documentation (no version stamp ships anywhere — adopted as `source_as_of: 2026-10-15`, the verified-live fetch date).
- WealthCharts knowledgebase, `Percentage Price Oscillator (PPO) - Indicator Formula` page, fetched live (HTTP 200, 167786 bytes). Independently pins the identical construction (`two exponential moving averages; the 12-day EMA and the 26-day EMA`; `The signal line is an EMA of the PPO line, so it will be slower than the PPO line`; `oscillates around a zero line`) and the identical formula (`PPO = [(12-day EMA - 26-day EMA) / 26-day EMA] * 100`; `Signal Line = 9-day EMA of PPO`; `PPO Histogram = PPO - Signal Line`). Independently pins the explicit two-sided trigger pair (`Trade Signal: When the PPO line crosses above the signal line it is a buy signal. When the PPO line crosses below the signal line it is a sell signal`) plus the zero-line trend context (`When the PPO is above the zero-line that is a sign that the trend is up. When the PPO is below the zero-line that is a sign that the trend is down`). Ships zero performance numbers of any kind. The two constructions are arithmetically identical term for term; no other value in this record comes from any other source.

Licence and rights: both pages are public technical documentation. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any source trading system. Researcher-declared adaptations are exactly six: (1) market pin `BTCUSDT` on Binance futures with the source-native daily frame kept (venue transfer plus symbol spelling, futures short permission disclosed here, never presented as source-native); (2) entry-timing pin — the documented cross pair is evaluated once per completed bar as strict prior-bar-confirmed crosses with same-bar-close fills (the sources ship the cross triggers and the close basis, not a fill convention); (3) exit pin — the sources ship the cross pair and no stop, target, trailing, time exit, or flat state, so the opposite cross closes and atomically reverses the leg (predeclared here; explicitly none of the above, never hidden); (4) an adopted 60-bar warmup with pre-warmup bars flat by record rule (covers the 26-bar slow EMA plus the 9-bar signal smoothing plus seeding margin); (5) the EMA recursion pin `EMA(t) = k*x(t) + (1-k)*EMA(t-1)` with `k = 2/(N+1)`, seeded with the first available close (the standard Pine-convention seed; neither source pins a seed, so the seed is a predeclared record rule, and the warmup absorbs its transient); (6) house sizing/capital/costs replacing the absent source economics (recorded as absent, never as zero-cost evidence; see Execution assumptions). The 12/26/9 lengths, the `100 x (fast-slow)/slow` ratio, the 9-EMA signal, the close-only basis, the cross-above-buy / cross-below-sell pair, the discarded histogram, and the no-stop/no-target posture are source-pinned and unmodified elsewhere. **No Safety Order, no DCA event, no pyramiding, and no second leg is admitted in this record's version** — the admitted machine holds exactly one leg; the house BO/SO/SO DCA matrix is a separately declared downstream experiment only (see Adoption boundary). The reviewer is never asked to choose between versions: there is exactly one.

Pre-write dedup (2026-10-15): working-tree case-insensitive fixed-string searches for `Percentage Price Oscillator` and word-boundary `PPO` return zero strategy records using this indicator or construction — the only `PPO` hits anywhere are a prose cousin-list inside `pvo-signal-cross-volume-momentum-two-sided-btcusdt-1d-2026-10-12.md` (which names PPO among price-only signal-line crosses as distinct from its own volume-input machine, never a PPO rule) and incidental `support`/`opportunity` substrings elsewhere. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closed October-15 Scout PRs #222 (Blau DTI band-latch), #223 (DPO zero-sign latch), #224 (Bufi adaptive RSI), #225 (RMI band-latch) are different oscillators with different arithmetic. Closest pool records are different mechanism classes: `macd-signal-cross-reversal-btcusdt-1d-2026-10-09.md` crosses the absolute difference `12-EMA minus 26-EMA` against its signal (no division — its cross timing shifts with the price level, exactly the level-dependence StockCharts attributes to MACD and denies to PPO); `pvo-signal-cross-volume-momentum-two-sided-btcusdt-1d-2026-10-12.md` crosses two volume-derived lines (reads no close at all); `kst-signal-cross-trend-two-sided-btcusdt-1h-2026-10-09.md` crosses a 4-ROC composite against its signal (no EMA-difference ratio anywhere); `trix-dual-band-trend-btcusdt-1d-2026-10-09.md` bands a triple-smoothed single line (no second line to cross); `tsi-signal-cross-reversal-btcusdt-1d-2026-10-10.md` crosses a double-smoothed momentum fraction (different numerator, different smoothing stack); `pmo-signal-cross-reversal-two-sided-btcusdt-1d-2026-10-13.md` crosses a custom-smoothed Price Momentum Oscillator (different construction, different lengths); `coppock-curve-zero-state-long-flat-btcusdt-1d-2026-10-09.md` holds a ROC-sum state long/flat (no signal line, no cross, single side). No pool record computes `100 x (EMA12 - EMA26) / EMA26` with a 9-EMA signal cross. Shared `signal-line cross` wording or shared EMA machinery is not shared signal.

## Economic mechanism

### Source-reported

Percentage-normalized momentum rotation with a slower confirmation line: the PPO expresses the 12/26 EMA gap as a percentage of the slow leg, so the print is scale-free across price levels; the 9-EMA signal trails it as the slower upturn/downturn judge. When the PPO line crosses above its signal line it is a buy signal; when it crosses below it is a sell signal. Above the zero line the trend reads up, below it down — context, never a trigger here (see Negative evidence). The design bets that signal-line rotations of the normalized gap on the daily frame precede multi-day directional drift, and that staying aligned with the last rotation harvests more drift than it surrenders to whipsaw.

### Research interpretation

Naked-oscillator rotation system with no price-level, band, cloud, or confirmation state — two-sided, always-in-position after the first signal. Unlike the absolute MACD cross (whose gap is denominated in price units and whose cross timing stretches with the price level), this machine divides by the slow EMA first, so identical momentum shapes print identical crosses at any price level — on a venue where the underlying trends across orders of magnitude, level-dependence is not cosmetic. Unlike raw price-EMA crosses (EMA-20-50, golden-cross) that compare smoothed price against smoothed price, entries fire on second-order rotation of a derived series — strictly later and smoother than first-order crosses, at the cost of deeper lag into V-turns. Unlike flat-capable systems, there is no neutral state after the first signal: a long exists until the cross down reverses it to short and vice versa, so ranging markets grind through repeated full reversals with no stop to truncate them. The price of scale-freedom is that tiny slow-EMA denominators (flat, low-price chop) still print well-formed crosses that trade identically to trend-birth rotations. The bet is on daily-frame normalized-momentum persistence, never on a level, breakout, squeeze, calendar, or mean-reversion anchor.

## Signal

Exact rule as pinned (all inputs frozen — any other value is a different, unpinned rule):

- Declarations (derived): single-position state machine over `BTCUSDT 1d` with same-bar-close execution and house sizing/costs (see Execution assumptions). At most one open leg; state ∈ {flat, long, short}; flat exists only before the first signal and under the warmup rule. No Safety Order, no DCA event, no pyramiding — explicitly none admitted here, not invented.
- EMA recursion (record pin for the source-silent seed): `EMA_N(t) = k_N * C(t) + (1 - k_N) * EMA_N(t-1)` with `k_N = 2/(N+1)`, seeded with the first available close; `C(t)` is the completed bar's close.
- Indicator, pinned verbatim at defaults (`12/26` fast/slow, `9` signal): `FAST(t) = EMA_12(C)(t)`; `SLOW(t) = EMA_26(C)(t)`; `PPO(t) = 100 * (FAST(t) - SLOW(t)) / SLOW(t)`; `SIG(t) = EMA_9(PPO)(t)`. The histogram `PPO(t) - SIG(t)` is display-only: computed by neither order line, pinned as discarded (same isolation as the admitted MACD record's discarded third output).
- Entry long: on bar `t` with `PPO(t) > SIG(t)` strictly and `PPO(t-1) < SIG(t-1)` strictly (the documented cross-above buy, as a prior-bar-confirmed strict cross on confirmed closes; from flat: open long; from short: atomic reversal — close short plus open long as a single reversal event). Same-side reprints while long are no-ops (no adds — explicitly none admitted).
- Entry short: mirror on `PPO(t) < SIG(t)` strictly and `PPO(t-1) > SIG(t-1)` strictly (the documented cross-below sell).
- Exact-touch determinism, pinned by the strict source comparatives (`above` / `below`): any bar where either comparison is an equality satisfies neither leg and changes nothing — disclosed, not oversold as tolerance.
- Exits: the opposite cross only (predeclared derived completion — the sources ship the cross pair with no stop, no target, no trailing, no time exit, no flat state anywhere). No histogram-zero exit, no zero-line exit, no neutral-return flat — explicitly none by record rule, not invented, forming a complete always-in machine after the first signal. A positioned leg whose opposite cross never prints is held indefinitely.
- Direction: two-sided with an explicit pre-first-signal flat state (plus the 60-bar warmup flat by record rule). The documented Trade Signal prescribes both the buy and the sell leg; a single-sided reading would contradict it.

## Required data

- Completed `1d` bars of BTCUSDT: `close` only (sole series read — both EMAs, the ratio, and the signal derive from closes; the discarded histogram reads no new series). No `open`, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (the documented 12/26/9-day construction is frame-faithful on daily bars; the rule references no other frame, no multi-timeframe input — single-frame by construction).
- Warmup: the binding costs are the 26-bar slow EMA (first fully-formed value needs 26 completed closes), the 9-bar signal smoothing of PPO output on top, and the pinned seed transient. The adopted warmup is the first 60 completed `1d` bars flat by record rule (predeclared researcher choice — covers 26 + 9 plus wide seeding margin; no signal before bar 61 may trade). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. Every input is complete at bar `t`'s close — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (frame-faithful `1d`; venue choice, symbol spelling, and short permission disclosed in Provenance, never presented as source claims).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) — the same verified execution primitive as the admitted `qstick-zero-cross-trend-two-sided-btcusdt-1h`, `imi-50-midline-cross-flip-two-sided-btcusdt-1d`, and `macd-signal-cross-reversal-btcusdt-1d` PASS records (single-frame completed-bar decision, same-bar-close market fill, single-position machine, no stop/limit legs anywhere, hence no same-bar TP/SL ordering ambiguity; each trigger reads only completed bars with prior-bar confirmation, so each bar's outcome is a single deterministic event: hold, open, or atomic reversal). No maker-touch, queue, multi-asset sync, lower/multi-timeframe alignment, non-OHLCV input, or intrabar-path-dependent fill is required by any line of this record.
- Sizing/capital/costs: the sources ship no portable economics (no commission/quantity assumption — recorded as absent economics, never as zero-cost evidence) — derived evaluation carries the fixed, reproducible house research cost model (Base 6% + Safety 6% + Safety 6% notional framing, Isolated, 3x/5x; pinned house cost assumptions for fees plus modeled funding — no hypothetical zero funding claimed, never presented as source-native behavior). Funding is modeled, never reported as realized or canonical funding; no historical-funding settlement path is required or claimed for this version. No Safety-Order/DCA event participates in the admitted trigger machine regardless of downstream campaign settings.
- Concurrency: single-position machine — at most one open leg; same-state bars while positioned are no-ops; the opposite cross reverses in full (one atomic event); re-entry is allowed on the next fresh opposite cross after any close (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The sources ship the full construction (`100 x (12-EMA - 26-EMA) / 26-EMA`, `9-day EMA of PPO` signal, `PPO - Signal` histogram), the signal taxonomy (signal-line crossovers alongside centerline crossovers and divergences), the explicit two-sided cross trigger pair (cross above = buy, cross below = sell), the zero-line trend context, and the close basis — quoted in Provenance. Neither source ships a backtest table or figure for this construction (page-wide census above: zero Sharpe/profit/drawdown hits; all `return`/`performance` hits are site chrome or unrelated-indicator nav), so this record carries zero source-reported performance numbers and claims no performance of any kind.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No performance to carry, admitted plainly: unlike paper-sourced records with backtest tables, both rule sources ship construction, triggers, and formula context only — there is no expectancy number anywhere to fence, and this record claims none.
2. Untraded source content fenced, admitted plainly: centerline crossovers and divergences are real documented signal types deliberately not carried here (this record trades the signal-line cross pair only by record rule); the above/below-zero trend read is context, never a trigger or gate. Carrying any of them would be a different, unpinned rule.
3. No hidden exits or risk layer: the traded machine names no stop, no target, no trailing, no time exit, no histogram-zero exit, no zero-line exit, no neutral-return flat anywhere — the no-stop/no-target posture is the record rule, explicitly none, never hidden. Every adverse excursion is held to the opposite cross.
4. Trigger exclusivity proved: the long leg requires `PPO(t) > SIG(t)` with `PPO(t-1) < SIG(t-1)` while the short leg requires the exact mirror — no bar satisfies both, so no bar fires both transitions and no priority rule is needed or invented.
5. Exact-touch determinism fenced: any equality in either comparison changes nothing by the pinned strict comparatives (measure-zero on continuous prints — disclosed, not oversold as tolerance).
6. Seed determinism fenced: the only source-silent computation choice (the EMA seed) is pinned by record rule to the first-close Pine-convention seed, and the adopted 60-bar warmup (26 slow + 9 signal + wide margin) absorbs its transient before any tradable bar — no traded signal depends on an unpinned seeding choice.
7. No future leakage in the stack, stated plainly: at decision bar `t`, every input is a completed-bar close or a recursion over completed closes with prior-bar-confirmed comparisons — every input is complete at bar `t`'s close. No multi-frame read, no negative index, no full-sample normalization, no repainting path, no calendar read at all.
8. Oscillator-family overlap fence, admitted plainly: the pool's MACD record crosses an absolute price-denominated gap (level-dependent by the source's own thesis); the PVO record reads volume lines (no close input); the KST record crosses a 4-ROC composite (no EMA-difference ratio); the TRIX record bands a triple-smoothed single line (no second line to cross); the TSI record crosses a double-smoothed momentum fraction (different numerator and stack); the PMO record crosses a custom-smoothed momentum oscillator (different construction and lengths); the Coppock record holds a ROC-sum zero state long/flat (no signal line, single side); Qstick/IMI/VZO/REI/Forecast/CMO read body/range/volume legs with band or midline triggers (never a 12/26 percentage ratio with a 9-EMA signal cross). This record's `100 x (EMA12 - EMA26)/EMA26` with a 9-EMA signal-line cross pair exists nowhere else in the pool. Shared `signal-line cross` wording or shared EMA machinery is not shared signal.
9. Two-sided posture provably complete: symmetric cross-above buy / cross-below sell legs with symmetric atomic-reversal exits under the documented Trade Signal — no third direction exists, and a single-sided reading would contradict the printed opposite leg.
10. Derivation boundary fenced: the only non-source-native behaviors in this record are the `BTCUSDT` futures market pin with the source-native daily frame kept, the per-completed-bar strict-confirmed-cross evaluation with same-bar-close fills, the opposite-cross reversal exit, the first-close EMA seed with the adopted 60-bar warmup and record-rule pre-warmup flat, and house sizing/costs with no admitted Safety-Order/DCA event — all predeclared above; the 12/26/9 lengths, the ratio, the signal, the close basis, the cross pair, the discarded histogram, the single-position guards, and the risk posture are source-pinned or predeclared. This record is therefore never evidence that any other market, frame, length triple, trigger set, or timing of the source passes.
11. Division of evidence disclosed: the formula, lengths, signal, histogram, taxonomy, close basis, and normalization thesis above were byte-verified in the fetched StockCharts page (797436 bytes, HTTP 200); the explicit buy/sell cross pair, the zero-line context, and the second formula pin were byte-verified in the fetched WealthCharts page (167786 bytes, HTTP 200). The division of evidence is disclosed here, not hidden.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `12/26/9` / close-only PPO ratio / 9-EMA signal / strict confirmed crosses / cross-to-cross atomic reversal / no-stop-no-target posture / two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Cross-timing relevance: replacing the strict-cross trigger with the always-live PPO position state (long whenever `PPO > SIG`, short whenever `PPO < SIG`, evaluated every bar) must not improve net expectancy; fail ⇒ the cross timing adds nothing over holding the oscillator state.
- F2 — Short-side relevance: dropping the short leg (long on cross up, flat — not short — on cross down) must not improve net expectancy; fail ⇒ the two-sided reversal is dominated by a long/flat posture on this market.
- F3 — Normalization relevance: replacing the percentage ratio with the absolute MACD gap (same 12/26/9 lengths, same cross machine, same reversal handling) must not improve net expectancy; fail ⇒ the slow-EMA normalization adds nothing over the level-dependent gap.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (frame-faithful `1d`; venue transfer disclosed). The rule reads only completed daily closes, so no volume-series, high/low-print, or open-print differences can touch any order-gating line — but spot-vs-perp close prints can still differ structurally (funding-driven drift, venue aggregation), so the futures-venue pin is load-bearing and disclosed. The ratio is unit-free and the lengths are fixed constants, so no fixed-pip recalibration is needed across assets — cross-asset behavior differences are still real and unclaimed. The rule is two-sided with no stop leg, so a spot-only deployment expresses the long state and reversal mechanics only to the extent the venue permits shorting — full two-sided expression assumes a futures venue, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read beyond each calendar-day bar's own close (no session gating anywhere); decision boundaries are calendar-day bars of the venue feed, disclosed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived market pin: the sources describe daily stock bars; this record pins `BTCUSDT` futures `1d`. Cross-market and spot-vs-perp close behavior differences are real — the venue transfer is disclosed, and this record makes no claim about any other market or the sources' native venue.
- Untested trigger scope: the only source-documented scheme carried here is the signal-line cross pair; centerline crosses, divergences, and the zero-line trend read are performance-unclaimed context, and the pinned pair itself carries no expectancy claim until downstream research measures it.
- No source economics: the sources ship no commission, sizing, funding, or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- No price stop, no time stop: adverse excursion after entry has no guardrail beyond the opposite cross, which may arrive many bars later or after deep excursion; a leg whose opposite cross never prints is held indefinitely. This is the record-rule posture, disclosed as a principal risk.
- Alternating-cross whipsaw: consecutive opposite crosses print repeated reversal pairs with no flat state to rest in, by the prescribed always-in design. The naked-cross construction is the documented trigger, disclosed, not smoothed.
- Slow-EMA denominator sensitivity: prolonged flat chop keeps printing well-formed crosses around a near-zero denominator; a venue that cannot supply trustworthy per-bar closes cannot trade the pinned rule.
- Seed convention cost: the first-close EMA seed is a predeclared record rule, not a source fact; the adopted 60-bar warmup absorbs its transient structurally, and the first 60 bars are flat by record rule.
- Lag at V-turns: the signal smooths an already twice-EMA-derived series (12/26 then 9) — a sharp reversal must drag the PPO line across the full signal gap before any trigger prints, so entries arrive strictly after the turn by construction.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior and never part of this admission — no Safety-Order/DCA event is admitted in this record's version. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- StockCharts ChartSchool technical documentation, Percentage Price Oscillator (PPO) — 12/26/9 construction, signal/histogram/centerline, signal-line-cross taxonomy, close basis, normalization thesis (verified live in the fetched page during this cycle; zero PPO performance claims): https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/percentage-price-oscillator-ppo
- WealthCharts knowledgebase indicator formula, Percentage Price Oscillator (PPO) — independent pin of the same 12/26/9 construction plus the explicit cross-above-buy / cross-below-sell Trade Signal and zero-line trend context (verified live in the fetched page during this cycle): https://www.wealthcharts.com/kb/category/charts/indicator-formulas/Percentage-Price-Oscillator-PPO-Indicator-Formula
