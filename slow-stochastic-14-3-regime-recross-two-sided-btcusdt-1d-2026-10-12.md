---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Slow Stochastic 14-3 20/80 regime recross two-sided on BTCUSDT 1d bars
created: 2026-10-12
updated: 2026-10-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-12
sources:
  - https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/stochastic-oscillator-fast-slow-and-full
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Slow Stochastic 14-3 20/80 regime recross two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (StockCharts ChartSchool page fetched in full during this cycle, 2026-10-12):

- StockCharts ChartSchool, `Stochastic Oscillator (Fast, Slow, and Full)` — canonical URL: https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/stochastic-oscillator-fast-slow-and-full. Lineage stated on-page: the Fast form is George Lane's original %K/%D construction; the Slow form was introduced because Fast %K prints choppy and %D carries the signal emphasis.
- Pinned computation (verbatim in sense): `Fast %K = 100 × (Close − Lowest Low over look-back) / (Highest High over look-back − Lowest Low over look-back)`; `Fast %D = 3-period SMA of Fast %K`; `Slow %K = Fast %K smoothed with 3-period SMA` (so Slow %K equals Fast %D tick for tick); `Slow %D = 3-period SMA of Slow %K`; Full Stochastic `(14,3,3)` is the customizable form of the same chain. Pinned defaults (§Using with SharpCharts): Fast `(14,3)`, Slow `(14,3)`, Full `(14,3,3)` — the 14-bar look-back feeds the basic %K and the `3` sets the %D average, with Slow %K carrying the extra 3-bar smoothing stage.
- Pinned thresholds (§Overbought/Oversold, verbatim in sense): traditional settings use `80` as the overbought threshold and `20` as the oversold threshold on the always-0-to-100 oscillator; above-80 prints are overbought-and-strong, below-20 prints are oversold-and-weak. The reversal doctrine is pinned as recross events: "a subsequent move below 80 is needed to signal a reversal or failure at resistance" and "a move above 20 is needed to show an upturn and successful support test".
- Pinned two-sided scans (§Suggested Scans, publisher's own concrete rules, quoted in structure): `Stochastic Oscillator Oversold Upturn` = `[Close > SMA(200, Close)] AND [Yesterday's Slow %K(14,3) < 20] AND [Today's Slow %K(14,3) > 20]`; `Stochastic Oscillator Overbought Downturn` = `[Close < SMA(200, Close)] AND [Yesterday's Slow %K(14,3) > 80] AND [Today's Slow %K(14,3) < 80]` — both directions ship as first-party rules with the 200-day trend gate built in.
- Pinned trend doctrine (§Overbought/Oversold and chart 4/5 passages, verbatim in sense): "it is important to identify the bigger trend and trade in the direction of this trend"; oversold upturns are taken with the bigger uptrend while overbought prints are ignored, and symmetrically in downtrends — the SMA200 gate in both scans is this doctrine in executable form.
- Fenced on purpose: the bull/bear divergence and bull/bear set-up passages (multi-step discretionary chart-reading with confirmation ladders — signal-cross, 50-midline, then price breakout — never a standalone rule); the %K/%D signal-line cross as entry ("earliest entry possible" is real page content but the publisher's own scans trigger on the 20/80 level recross, so the line-cross is fenced to keep one pinned trigger); the Full `(20,5,5)` / `(10,3,3)` chart-illustration parameters (display variants, never signal rules); the scan liquidity pre-filters (`SMA(20, Volume)`, `SMA(60, Close)` minima — equity-universe hygiene, not signal logic); the volume/support-resistance/breakout confirmation advice (discretionary overlay, no rule attached). None is adopted.
- Licence and rights: this record cites and normalizes the rule (short phrases and formulas only) and reproduces no chart, table, figure, spreadsheet, or extended prose.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — ChartSchool's Slow Stochastic (14,3) 20/80 scan pair ported to one crypto asset as a two-sided daily state machine — not a lossless reproduction of the publisher's discretionary equity-chart practice. Researcher-declared adaptations are exactly six: (1) single-asset BTCUSDT Binance tape (the page is equity-charted; the scans filter US stocks — crypto portability is a researcher carry, disclosed); (2) a two-sided hold state machine whose exits are the mirror recross events — exit-long on the downturn recross, exit-short on the upturn recross — evaluated without re-checking the SMA200 gate (the scans pin entries only; the gate-at-exit treatment is disclosed researcher specification, justified by the page's own "move below 80 signals a reversal" doctrine); (3) next-open market fills on the `1d` grid (the source is cadence-silent beyond completed-bar evaluation; daily closes are the declared port); (4) fixed 100%-equity single position at 1× with no leverage (the source ships no sizing); (5) no stop, no target, no trailing, no time exit (the source ships no risk leg for the scan use anywhere — exits are signal-driven only, source-faithful absence); (6) a declared degenerate-window/warmup convention (the publisher pins the formula but no zero-range arithmetic, so the undefined-print rule below is disclosed researcher specification, never presented as a source fact). The Slow (14,3) chain, the 80/20 thresholds, the recross trigger structure, both scan directions, and the SMA200 entry gate are source-faithful.

Pre-write dedup (2026-10-12): working-tree case-insensitive searches for `slow.?stoch`, `stoch\(14`, and `%K\(14` return zero strategy records computing a Slow Stochastic rule — the only touch is a falsification-plan mention inside `williams-r-level-cross-mean-reversion-long-btcusdt-1d-2026-10-09.md` (a Williams %R record, different indicator and mechanism). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state-reversal two-sided) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `kdj-golden-cross-long-flat-btcusdt-1d-2026-10-11.md` trades a 9-bar Wilder-`bcwsma` KDJ J-line × D-line golden cross, long-only with a J > 100 rail exit (line-cross edge on an accelerated J line, no level recross, no regime gate); `stoch-rsi-kd-zone-cross-two-sided-btcusdt-1h-2026-10-12.md` smooths RSI, not price rank; `dss-bressert-double-smoothed-stochastic-trigger-latch-two-sided-btcusdt-2h-2026-10-12.md` double-smooths with a trigger latch on a 2-hour grid; `stochastic-ott-dual-trend-btcusdt-1d-2026-10-06.md` chains %K/%D to a dual OTT trailing-stop system. Five-axis distinction: no pool record and no open PR trades Slow-Stochastic(14,3) %K 20/80 level-recross events with an SMA200 regime entry gate, two-sided.

## Economic mechanism

### Source-reported

Range-position mean-swing: the Slow Stochastic ranks each close inside its own trailing 14-bar high-low range, so the print is always a 0–100 sentiment gauge independent of price level. Sub-20 prints mean the close hugs the range floor (exhausted sellers / successful support test once it recrosses up); above-80 prints mean the close hugs the range ceiling (exhausted buyers / resistance failure once it recrosses down). The double smoothing (3-bar on %K, 3-bar on %D) exists to strip single-bar spikes while keeping the turn, and the bigger-trend gate exists because oscillators whipsaw against the prevailing drift — hence upturns are taken above the SMA200 and downturns below it.

### Research interpretation

Exhaustion-recross regime port: the derived system never holds through the overbought/oversold zone — it enters exactly on the zone exit and holds until the opposite zone exit, so every position begins the moment range-position pressure releases and ends the moment opposite pressure releases. Unlike the KDJ record (which fires on an internal J × D line cross anywhere in the 0–100 span and can ignite mid-range), this system can only fire at the 20/80 rails, so its trade count is bounded by rail-touch frequency, not by internal line wiggle. Unlike RSI-threshold records (close-to-close change gauges), the trigger here is pure range position — a grinding one-way drift that never revisits a rail prints no signal at all. The SMA200 gate makes the long leg a pullback-continuation bet and the short leg a rally-failure bet, never a counter-trend catch. The bet, as derived, is purely on post-exhaustion swing persistence at the fortnight scale, never on a level, band, calendar date, or funding print.

## Signal

Exact rule as pinned (Slow chain / 14-bar window / 3-bar smoothing / 20-80 rails / scan-verbatim cross structure — any other value is a different, unpinned rule):

- Series (pinned): for completed `1d` bar `t` (`t = 1` is the first available bar) with high `H_t`, low `L_t`, close `C_t`: `HH14_t = max(H_{t-13} … H_t)`, `LL14_t = min(L_{t-13} … L_t)`, defined from bar 14. `FastK_t = 100 × (C_t − LL14_t) / (HH14_t − LL14_t)`. `SlowK_t = (FastK_{t-2} + FastK_{t-1} + FastK_t) / 3`, defined from bar 16. `SlowD` is not computed (fenced — see Provenance). Degenerate-window convention (declared, disclosed — the publisher is silent on undefined arithmetic): a window with `HH14_t == LL14_t` prints `FastK_t = 50` (range-neutral mid-print, inside neither trigger zone, holds state); crypto highs/lows are strictly positive regardless, so the quotient is otherwise always defined.
- Regime gate (pinned): `SMA200_t = mean(C_{t-199} … C_t)`, defined from bar 200.
- Events (scan-verbatim structure, evaluated at each completed close once all inputs are defined): upturn event ⟺ `SlowK_{t-1} < 20 AND SlowK_t > 20`; downturn event ⟺ `SlowK_{t-1} > 80 AND SlowK_t < 80`. An exact `20.0`/`80.0` print on either side is a no-event (holds state) — deterministic, matching the scans' strict inequalities. The two events are mutually exclusive by construction (they require contradictory `SlowK_{t-1}` zones), so no priority rule can ever fire.
- Position target (derived state machine, disclosed): flat before the first entry event. Long-entry ⟺ upturn event AND `C_t > SMA200_t` → target long. Short-entry ⟺ downturn event AND `C_t < SMA200_t` → target short. Exit-long ⟺ downturn event (no SMA200 re-check, disclosed pin). Exit-short ⟺ upturn event (no SMA200 re-check, disclosed pin). A bar whose event matches the current side places nothing (no adds, no re-entry edge while positioned).
- Orders (pinned): at most one order event per bar, placed for the next `1d` open after the decision bar: target long buys/holds 100% equity long; target short sells/holds 100% equity short; exit events close to flat when no opposite entry co-fires (they cannot co-fire — see exclusivity). A target change closes the old side and opens the new side at the same next open. Unchanged target places nothing. No intrabar evaluation, no intrabar orders, no partials, no second decision inside the fill bar for any reason including large adverse excursion. Entry and exit can never co-fire beyond the single atomic flip: the target is one state per bar.
- Risk legs (pinned absence, not invented): the source ships no stop/target/trailing/time-exit concept for the scan use anywhere — the sole position-changing path is the next recross event. The derived posture is explicitly no stop, no target, no trailing, no time exit; an adverse drift that never prints the opposite recross is ridden in full by construction.
- Direction: two-sided long/short with a flat state between an exit and the next gated entry (derived pin matching the page's symmetric upturn/downturn scan pair). The research market is the Binance perpetual under the house overlay with both permissions genuinely used.

## Required data

- Completed `1d` high, low, and close of BTCUSDT only: three scalars per bar (`H_t`, `L_t`, `C_t`; open is used only as fill price). No volume, funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, breadth, or cross-venue state gates any order. No multi-symbol, multi-timeframe, or external-feed dependency of any kind. The %K/%D line-cross leg, the divergence/set-up legs, the Full-illustration parameters, and the scan liquidity pre-filters are fenced — none is computed.
- Single decision grid: completed daily bar. One evaluation per close; fills land on the next daily bar's open. All inputs are completed-bar prints — no provisional range is ever used. Bar extremes and closes are final at bar close on the venue tape.
- Warmup: 200 completed `1d` bars before the first decision (the SMA200 gate is the binding seed; the Slow %K chain is ready at bar 16). Bars 1–200 are flat by record rule; the first decidable close is bar 200 and its fill lands on bar 201's open. No signal before the seed window completes may trade. No repainting, no negative shift, no future reference, no full-sample normalization; the 24/7 tape needs no session template (bar membership is the venue's own daily grid — deterministic).

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared single-asset port; no cross-venue equivalence claimed). The venue's daily bars replace the page's equity bars one for one — both are completed-bar OHLC prints, never modelled intraday.
- Order timing (declared port; the source is cadence-silent beyond completed-bar evaluation): completed-bar decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill: the only legs are gated entries, recross exits, and atomic flips, and at most one order exists per bar — there is no same-bar dual-fire to sequence.
- Sizing/capital/costs: fixed 100%-equity single position, no adds, no leverage (1×, no margin concept beyond the venue's own short permission), no compounding concept beyond equity — declared derivative (the source ships no sizing). Derived evaluation must carry the explicit house overlay (pinned house fees plus historical funding treatment; no hypothetical zero funding claimed — the short leg accrues genuine funding economics and neither leg is modelled funding-free). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one position (long or short) at any time; a flip needs only the next opposite recross close (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The page ships the full construction adopted here: the Fast %K quotient formula, the 3-bar Fast-%D and Slow-chain smoothing stages with Slow %K tick-identical to Fast %D, the `(14,3)` / `(14,3)` / `(14,3,3)` defaults, the always-0–100 bound, the traditional 80/20 thresholds, the below-80/above-20 recross reversal doctrine, the trade-with-the-bigger-trend doctrine with its uptrend/downtrend chart passages, and both gated scans (Slow %K(14,3) oversold upturn above SMA200, overbought downturn below SMA200). It ships zero adopted performance numbers for this record: the IGT/KSS/CCI/AZO/MOT charts are illustration, never a return claim — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Equity-charted gauge, fenced: every worked example is a US equity and the scans filter `[type = stock] AND [country = US]`. The single-asset crypto port is a researcher carry justified only by arithmetic portability (ranges and closes print on any tape), never by source evidence — this record is never evidence that Slow Stochastic times BTCUSDT well.
2. Whipsaw admission, carried: the page concedes signal-line crosses and 20/80 moves "are frequent and prone to whipsaw" (the KSS passage, where early signals failed and the oscillator rebounded above 50 before the decline resumed). The derived system converts those episodes into flip churn, disclosed, not filtered.
3. Standalone-use caveat, carried: "it is important to use the Stochastic Oscillator in conjunction with other technical analysis tools" (volume, support/resistance, breakouts offered as confirmation). This record is a standalone specification for admission purposes, never a recommendation.
4. No hidden risk layer: the source ships no stop/target/trailing concept for the scan use — the sole position-changing path is the next recross event. The absence of any stop is source-faithful absence, disclosed, not a tunable parameter here.
5. Fully exposed inside the swing: once positioned, the system rides the entire adverse excursion with no guardrail — a −50% drift that never prints the opposite recross is held to the last bar by construction. This is the coded trade, disclosed, not a tunable parameter here.
6. Degenerate-arithmetic boundary, fenced: the publisher pins the quotient formula but no zero-range arithmetic — the `HH == LL → FastK = 50` print is declared researcher specification. A NaN-propagating or bar-skipping implementation would each be a different, unpinned rule. No BTCUSDT daily 14-bar window is expected to trigger the convention (continuous two-sided tape), so it changes no live-tape event.
7. Length and leg boundaries fenced: the Fast-only form, the %K/%D line-cross entry, the divergence/set-up legs, and the Full `(20,5,5)` / `(10,3,3)` illustration parameters are all real page content and each would be a different, unpinned rule — none is admitted here. Only Slow (14,3) with 20/80 recross events is specified.
8. Derivation boundary fenced: the only non-source behavior is the six declared adaptations (single asset, two-sided state machine with gate-at-exit treatment, daily next-open grid, fixed sizing, degenerate-bar/warmup convention, house costs); Slow chain, length 14, smoothing 3, rails 80/20, recross structure, both scan directions, and the SMA200 entry gate are source-faithful. This record is therefore never evidence that Lane's discretionary equity practice passes anything.
9. The Slow-14-3 / 20-80-recross / SMA200-gated-entry / single-position two-sided / signal-only-exit stance is pinned, not removed: adding the %K/%D line cross, the divergence legs, a stop/target/filter/cooldown, trading intrabar, disabling the short leg, or sizing partially instead of 100% equity would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: Slow (14,3) / 20-80 recross / SMA200 entry gate / next-open fills / single-position two-sided / signal-only exit / `1d` BTCUSDT are frozen.

- F1 — Window relevance: replacing the pinned 14-bar rank window with a 30-bar window (a slower range-position gauge) must not improve net expectancy; fail ⇒ the fortnight-scale rank carries no advantage over a slower form and the record is noise-trading in disguise.
- F2 — Smoothing relevance: replacing Slow %K (3-bar smoothed) with raw Fast %K(14) on the same rails and gate must not improve net expectancy; fail ⇒ the publisher's Slow-smoothing stage does no work and the record is a choppy-signal follower in disguise.
- F3 — Gate relevance: removing the SMA200 entry gate (recross events traded bare, both sides) must not improve risk-adjusted expectancy; fail ⇒ the bigger-trend doctrine carries dead weight and the gate is decoration.
- F4 — Symmetry relevance: disabling the short leg (downturn-regime flat instead of short, cost-loaded comparison) must not improve risk-adjusted expectancy; fail ⇒ the two-sided pin carries dead weight — or the short leg's funding load dominates.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid completed `1d` closes; high-low-close rank arithmetic with no venue-specific read). The arithmetic ports across perpetual venues without structural change provided the same OHLC denomination is pinned. Funding accrues genuinely on the short leg under the house overlay (no zero-funding claim); no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market prints a full high-low-close on every daily bar (bar membership is the venue's own daily grid — deterministic on any continuously traded tape). Extension to other house-universe assets, other windows, the %K/%D line-cross leg, the divergence legs, or the scan liquidity pre-filters would each be a different, unpinned claim.

## Limitations

- Single-asset port: the source's evidence is equity-charted illustration; single-asset BTCUSDT behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- No price stop, no intra-swing exit: adverse excursion inside the swing has no guardrail; the next decision is one bar away but the opposite recross itself can take weeks to print. This is the source-faithful posture, disclosed as the record's principal risk.
- Double-smoothing lag: two 3-bar averaging stages turn after price turns by construction — entries and flips print late by design.
- Rail-region churn: a market oscillating around the 20 or 80 rail produces repeated events with no swing to capture; disclosed, not filtered.
- Gate stranding: a recross event on the wrong side of the SMA200 is deliberately untraded, and an exit never re-checks the gate — a position can therefore be held counter to a freshly flipped SMA200 until the opposite recross prints. Disclosed researcher pin, not a source rule.
- Standalone-use caveat: the publisher advises confirmation use with other analysis; this record is standalone for admission purposes, never a recommendation.
- Unused cost silence: the source reports no cost accounting; derived evaluation must carry the full house cost load including short-leg funding, and this record reports no net performance of any kind.
- Warmup cost: the first 200 bars are flat by record rule, so any textbook swing completing inside the seed window is deliberately untraded — pinned, not recovered.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- StockCharts ChartSchool, Stochastic Oscillator (Fast, Slow, and Full) (Lane lineage, Slow (14,3) chain with Slow %K = 3-SMA of Fast %K, (14,3)/(14,3)/(14,3,3) defaults, 80/20 thresholds, below-80/above-20 recross reversal doctrine, trade-with-the-bigger-trend doctrine, both SMA200-gated scans; fetched in full 2026-10-12): https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/stochastic-oscillator-fast-slow-and-full
