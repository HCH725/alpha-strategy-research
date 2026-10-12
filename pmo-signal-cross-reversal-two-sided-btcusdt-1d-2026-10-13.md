---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: DecisionPoint PMO 35-20-10 signal-cross reversal two-sided on BTCUSDT 1d bars
created: 2026-10-13
updated: 2026-10-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-13
sources:
  - https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/decisionpoint-price-momentum-oscillator-pmo
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# DecisionPoint PMO 35-20-10 signal-cross reversal two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (fetched and verified live 2026-10-13):

- StockCharts ChartSchool, `DecisionPoint Price Momentum Oscillator (PMO)` — first-party documentation of Carl Swenlin's indicator (the page names him as developer: "Developed by Carl Swenlin, the DecisionPoint Price Momentum Oscillator (PMO) is an oscillator based on a Rate of Change (ROC) calculation that is smoothed twice with exponential moving averages that use a custom smoothing process"): https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/decisionpoint-price-momentum-oscillator-pmo — pinned formula block (verbatim in sense): "Smoothing Multiplier = (2 / Time period)"; "Custom Smoothing Function = {Close - Smoothing Function(previous day)} * Smoothing Multiplier + Smoothing Function(previous day)"; "PMO Line = 20-period Custom Smoothing of (10 * 35-period Custom Smoothing of (((Today's Price/Yesterday's Price) * 100) - 100))"; "PMO Signal Line = 10-period EMA of the PMO Line". Pinned trigger (verbatim in sense, Signal Generator section): "The PMO generates a crossover signal when it crosses through its 10-period EMA." Pinned defaults ("Using with SharpCharts"): "The default settings use a 35-period and 20-period EMA with a 10-period EMA signal line". Pinned scan identity `PMO Line(35,20,10)` / `PMO Signal(35,20,10)` corroborates the (35, 20, 10) default triple. Licence and rights: public indicator-reference page — this record cites and normalizes the formula and trigger (short phrases and arithmetic only) and reproduces no figures, spreadsheet, scan blocks beyond identification, or extended prose.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the ChartSchool PMO-vs-signal crossover pinned as a mechanical two-sided daily reversal — not a lossless reproduction of a source trading system, because the source is an indicator reference, not a backtest: it ships no order, no sizing, no fill convention, no venue, and no cost assumption. The page's own caution ("They should be used to alert you to possible trading opportunities, rather than as a mechanical trading model. Always check the chart to verify the price pattern") is fenced as discretionary advice, never a rule here. Researcher-declared adaptations are exactly five: (1) mechanical pin — every confirmed PMO-through-signal cross trades (the source's chart-check/extremes/kiss confirmations are fenced discretion, see Negative evidence); (2) same-bar-close fills on completed `1d` bars (the source declares no execution timing); (3) an adopted 80-bar warmup with pre-warmup bars flat by record rule (covers 35 + 20 + 10 plus seeding margin — see Required data); (4) house sizing/capital/costs replacing the absent source economics (see Execution assumptions); (5) venue port from the page's equity examples (S&P 500, MSFT, GLD) to `BTCUSDT` Binance perpetual on the source-native daily frame (the page warns "a monthly PMO looks completely different from a daily PMO" — frame is pinned `1d`, never monthly). The (35, 20, 10) triple, the custom-smoothing recurrence, the 10× scaling, the true-EMA signal line, both cross triggers, and the no-stop/no-target posture are source-faithful.

Pre-write dedup (2026-10-13): working-tree case-insensitive searches for `swenlin`, `decisionpoint`, `price-momentum-oscillator`, `price.momentum` return zero strategy records — a new family in this pool. The lone `pmo` substring hit is the English prose "custom close-inclusive" inside `chop-zone-dmi-psar-reversal-two-sided-btcusdt-1d-2026-10-11.md`, not this indicator. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak), #49 (Gaussian channel StochRSI breakout), #63 (SuperTrend ATR-flip), #89 (Chandelier Exit stop-flip), #92 (SSL channel reversal) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `macd-signal-cross-reversal-btcusdt-1d-2026-10-09.md` crosses an EMA-difference line (12/26/9, Appel) against its signal — an absolute-difference construction, while this record double-custom-smooths a ratio ROC with 10× scaling (the source itself draws this line: "The main difference between the PMO and MACD is the absolute value of each indicator ... whereas the PMO ... is an internal ratio"); `kst-signal-cross-trend-two-sided-btcusdt-1h-2026-10-09.md` crosses a summed ROC against its signal without double smoothing or ratio normalization; `tsi-signal-cross-reversal-btcusdt-1d-2026-10-10.md` double-smooths but as Blau normalization (`100 * ema(ema(change)) / ema(ema(abs(change)))`, 25/13/13) — a different recurrence, different scaling, different author and source. Five-axis distinction: no pool record and no open PR evaluates Swenlin's 35/20/10 custom-smoothed ratio-ROC PMO against its own 10-period EMA on any market or frame.

## Economic mechanism

### Source-reported

Ratio-normalized momentum thesis: because the PMO is built from an internal price-ratio ROC rather than an external price-minus-average difference, it is normalized — "it returns a result that is normalized and can be compared to the PMO result of any other security or index", so "chartists can rank a list of securities or indexes in relative strength order simply by using their PMO values", across stocks, indexes, and mutual funds in one list. Direction and velocity reading: "the PMO direction indicates if strength is increasing or decreasing, while the steepness of the trend angle demonstrates the power behind the move"; "PMO bottoms and tops suggest that price momentum has shifted direction, so they can provide early flags to price tops and bottoms. They are usually more reliable when the PMO is in overbought or oversold territory." Overbought/oversold colour only: the S&P 500 five-year example shows a normal range of about +2.5 (overbought) to −2.5 (oversold), MSFT about +5.0 to −5.0, with the warning that "each price index will have its own 'signature' range" — adopted as the reason no level gate is pinned here (no BTCUSDT signature range exists anywhere in the source). The page's MACD comparison ("similar shapes on shorter-term charts" but the ratio construction wins on longer-term charts "because the PMO is fairly constant, unlike the MACD") is adopted as construction context, never as performance.

### Research interpretation

Always-in-market double-smoothed ratio-momentum rotation, long-or-short, flipping only on the opposite signal-line cross. Unlike zero-level holders the position keys off the oscillator's own moving average, so a persistently positive-but-falling PMO still reverses short once it sinks through its signal — the system trades the second derivative (momentum of momentum), not the level. Unlike band/breakout systems there is no volatility, range, volume, or calendar gate — a cross on a dead bar flips the full position exactly as a high-conviction cross does. Unlike the source's discretionary use (extremes, kiss formations, trend-bias overlays), the derived record spends no confirmation of any kind: the bet is purely that daily PMO/signal rotations on BTCUSDT precede multi-day directional drift often enough to survive whipsaw, with the double custom-smoothing (35 then 20) plus the 10-bar signal EMA as the sole noise defence. The ranking use of the normalized PMO is fenced — this single-asset record ranks nothing.

## Signal

Exact rule as pinned (Swenlin 35/20/10 custom-smoothed ratio-ROC PMO against its own 10-period true-EMA signal; strict confirmed-bar crosses only — any other length, smoothing, scaling, trigger, or fill is a different, unpinned rule):

- Price input (pinned): `close` of completed `1d` bars only. The source's "Today's Price/Yesterday's Price" is the bar close ratio (the page's worked spreadsheet and scan reference both run on daily closes); no `open`, `high`, `low`, or `volume` enters any order-gating series.
- One-bar ROC (pinned): `ROC1(t) = (Close(t) / Close(t-1)) * 100 - 100`. Division is safe by record rule: BTCUSDT closes are strictly positive (a zero print would be a data error, never a signal — stated, not patched).
- Custom smoothing recurrence (pinned, NOT a true EMA): `CS(X, N)(t) = (X(t) - CS(t-1)) * (2 / N) + CS(t-1)` — the source's stated deviation ("instead of adding one to the time period setting to create the smoothing multiplier (as in a true EMA), the smoothing functions just use the period by itself"). Seeded with the first available value by record rule (deterministic; pre-warmup output never trades — see Required data).
- PMO line (pinned): `PMO(t) = CS(10 * CS(ROC1, 35), 20)` — 35-period custom smoothing of the ROC, scaled by exactly 10, then 20-period custom smoothing. The 10× factor is source arithmetic, never a tuned gain.
- Signal line (pinned): `SIG(t) = EMA(PMO, 10)` — a true 10-period EMA (multiplier `2 / (10 + 1)`), exactly as the source writes "10-period EMA of the PMO Line" (true EMA here, custom smoothing only inside the PMO leg — pinned asymmetry, not harmonized).
- Entry long (pinned trigger): on the first completed bar with `PMO(t) > SIG(t)` and `PMO(t-1) <= SIG(t-1)` (strict cross up on confirmed closes), buy at that bar's close. Prior-bar confirmation means the cross resolves causally — no provisional intrabar value is ever read.
- Entry short (pinned mirror): on the first completed bar with `PMO(t) < SIG(t)` and `PMO(t-1) >= SIG(t-1)`, sell short at that bar's close.
- Exclusivity (pinned, structural): both strict-cross predicates cannot hold on one bar, so no bar ever fires both legs — no same-bar ordering ambiguity exists. The measure-zero edge `PMO(t) == SIG(t)` fires neither leg and the position holds — stated, not patched.
- Risk legs (pinned posture): no stop, no target, no trailing, no time exit — the source ships none (its risk management is the discretionary chart/extremes check, fenced). The sole position-closing path on each side is the opposite cross, which reverses the position in full.
- Direction: two-sided with reversal only. Before the first post-warmup cross the system is flat (no position by construction); after it, always-in-market — there is no flat state, disclosed, not missing.

## Required data

- Completed `1d` bars of BTCUSDT only: `close` (sole series read — ROC ratio, both smoothings, both cross predicates). No `open`, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state gates any order. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (the source's ranking use and equity examples gate nothing here).
- Single decision grid: one evaluation per completed daily bar; both legs read only confirmed closes of bars `t` and `t-1`.
- Warmup: the 35-period custom smoothing needs 35 bars of ROC, the 20-period smoothing needs 20 bars of scaled output on top, and the signal EMA needs 10 bars of PMO output above that (35 + 20 + 10 = 65 minimum). The adopted warmup is the first 80 completed `1d` bars flat by record rule (predeclared researcher choice — covers 65 plus seeding margin); no signal before bar 81 may trade. No repainting, no negative shift, no future reference, no full-sample normalization; the 24/7 tape needs no session template.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared port of the page's equity examples; no cross-venue equivalence claimed).
- Order timing (declared derivation — the source is an indicator reference with no execution semantics): completed-bar decision with same-bar-close execution, compatible with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). This record makes no claim about any source fill timing because the source declares none. No maker-touch, queue, or intrabar-path-dependent fill: with mutually exclusive cross legs and no stop/limit legs, there is no same-bar ordering ambiguity of any kind.
- Sizing/capital/costs: the source ships no capital, sizing, commission, fee, slippage, or margin assumption anywhere — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all) apply to the derived evaluation here, never presented as source-native behavior. The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one position at any time; opposite-side crosses reverse in full in one step; same-side refires while already positioned are no-ops (single position, no adds); re-entry needs only the next opposite cross (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The short leg requires margin-short permission, realistic on the pinned perpetual venue.

## Evidence

### Source-reported

The page ships the construction adopted here: Swenlin authorship, the ratio-ROC thesis, the full custom-smoothing formula with the (35, 20, 10) default triple, the 10-period true-EMA signal line, and the crossover trigger ("generates a crossover signal when it crosses through its 10-period EMA"). Descriptive ranges as printed: S&P 500 normal range about +2.5/−2.5, MSFT about +5.0/−5.0, each index with its own signature range — fenced as description, never rules (no BTCUSDT range exists in the source). It ships zero adopted performance numbers for this record: no backtest, no win rate, no return table appears anywhere on the page — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Mechanical-use caution fenced: the page warns crossovers "can whipsaw quite a bit", "tend to be short-term in duration", should alert rather than trade mechanically, and are "best when price appears extended, is near support or resistance, and the PMO is very overbought or oversold" — all discretionary chart-reading with no codable thresholds, fenced as advice, never rules. This record trades every confirmed cross with eyes open (adaptation (1), disclosed).
2. Level gates fenced: the +2.5/−2.5 and +5.0/−5.0 ranges are other assets' signature ranges; the page insists each index has its own. Pinning any BTCUSDT overbought/oversold level would be invention — no level conditions this record.
3. Kiss/divergence/trend-bias overlays fenced: bear kiss, bull kiss, sideways-wiggle handling, price/PMO divergences, and DecisionPoint Trend Analysis 20/50/200-EMA bias are pattern-recognition overlays with no codable predicates in the source — none gates any order here.
4. Scan clauses fenced: the "rising but not yet crossed" scans add a US-stock universe, volume/price liquidity floors, three-bar rising streaks, and 20/50/200-EMA stacks — a screening use with a different event set, never strategy behavior here.
5. Monthly-frame warning fenced: "a monthly PMO looks completely different from a daily PMO" — this record is daily only; any other frame is a different, unpinned rule.
6. Always-in-market exposure, admitted plainly: after the first cross the system is never flat — chop across the signal line flips the full position on every alternating cross with no confirmation, no cooldown, and no cost guard (the page's own "Sideways Wiggle" section exhibits exactly this whipsaw). Adverse excursion between crosses has no guardrail beyond the opposite cross. This is the coded trade, disclosed, not a tunable parameter here.
7. Derivation boundary fenced: the only non-source behaviors are the mechanical-cross pin, same-bar-close fills, the adopted 80-bar warmup with record-rule pre-warmup flat, house sizing/costs, and the equity→BTCUSDT-perp venue port — all predeclared above; authorship, ratio-ROC thesis, custom-smoothing recurrence, 10× scaling, (35, 20, 10) triple, true-EMA signal, both strict triggers, exclusivity, and the no-stop/no-target/no-cooldown posture are source-faithful. This record is therefore never evidence that any source trading system passes.
8. The `35` / `20` / `10` / `10-EMA` literals, the `2/N` custom-smoothing multiplier (not `2/(N+1)`), the 10× scaling, the close-only ratio input, the strict confirmed-bar crosses (not touches, not level holds), the full reversal, the two-sided stance, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning any length, swapping custom smoothing for true EMAs, dropping the scaling, converting a cross into a touch or a level/zero-line hold, adding a stop/target/filter/cooldown/gate, dropping a side, or exiting to flat instead of reversing would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `35/20/10` / custom-smoothing recurrence / 10× scaling / close-only ratio PMO vs own 10-EMA signal / strict confirmed crosses / full reversal / two-sided / `1d` BTCUSDT / same-bar-close fills / 80-bar warmup are frozen.

- F1 — Crossover relevance: freezing direction to the first post-warmup cross side (hold that side for the whole sample, ignoring all later crosses) must not improve net expectancy; fail ⇒ the crossings add nothing over the first regime read.
- F2 — Smoothing relevance: replacing the pinned PMO with the raw 1-bar ROC sign (long when `ROC1 > 0`, short when `ROC1 < 0`, same reversal structure) must not improve net expectancy; fail ⇒ the double custom-smoothing adds nothing over raw ROC.
- F3 — Signal-line relevance: replacing the pinned PMO-vs-signal cross with a PMO-vs-zero cross (same reversal structure) must not improve net expectancy; fail ⇒ the signal line adds nothing over the zero level.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid completed `1d` bars; close-ratio arithmetic with no venue-specific read). The close-only arithmetic ports across perpetual venues without structural change. The short leg requires margin-short permission (realistic on perpetual venues; a spot-only deployment cannot express the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read, so session-gap behavior needs no approximation. The normalization property (cross-asset ranking) is unfenced only as context — this record ranks nothing and ports no equity level. Extension to other house-universe assets, formation inputs, or timeframes would be a different, unpinned claim.

## Limitations

- Indicator-doc sourcing: the source proves constructibility and trigger semantics, never profitability — no performance is claimed here for exactly this reason.
- Whipsaw by construction: the source's own caution and Sideways Wiggle section admit frequent unprofitable rotation signals around the signal line; the derived record takes every one, disclosed, not recovered.
- Lag at V-turns: the PMO smooths twice (35 then 20) before the 10-bar signal EMA smooths a third time — a sharp reversal must drag the PMO across the full signal gap before any trigger prints, so entries arrive strictly after the turn by code. The lag is the coded smoother, disclosed, not shortened.
- Seed convention: pre-warmup custom-smoothing/EMA seeds are a deterministic record-rule convention, disclosed for completeness (immaterial beside the 80-bar flat warmup).
- Open-confirmation lag: none beyond the bar close — decisions and fills share the completed close bar by declared derivation; gap-through moves across closes are taken at post-move closes, never at pre-move prices.
- Warmup cost: the first 80 daily bars are flat by record rule — pinned, not recovered.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- StockCharts ChartSchool, DecisionPoint Price Momentum Oscillator (PMO) (Swenlin authorship, ratio-ROC thesis, 1-period ROC `((Today's Price/Yesterday's Price) * 100) - 100`, custom-smoothing recurrence with `2 / Time period` multiplier, PMO line `20-period Custom Smoothing of (10 * 35-period Custom Smoothing ...)`, signal line `10-period EMA of the PMO Line`, crossover trigger "when it crosses through its 10-period EMA", (35, 20, 10) defaults, whipsaw/chart-check caution, per-index signature ranges, MACD comparison, kiss/divergence/scan fencing; verified live 2026-10-13): https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/decisionpoint-price-momentum-oscillator-pmo
