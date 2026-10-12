---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Ease of Movement 14 zero-cross trend two-sided on BTCUSDT 1d bars
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
  - https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/ease-of-movement-emv
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Ease of Movement 14 zero-cross trend two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (StockCharts ChartSchool page fetched in full during this cycle, 2026-10-12; the page advertises a Markdown edition for agent consumption at the same path plus `.md`, and the publisher `.md` twin was retrieved — the publisher's own machine-readable form, not a scrape artifact):

- StockCharts ChartSchool, `Ease of Movement (EMV)` — canonical URL: https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/ease-of-movement-emv (Markdown twin at the same path plus `.md`). Lineage stated on-page: developed by Richard Arms to quantify the price/volume relationship of his EquiVolume charts as an oscillator that fluctuates above and below the zero line.
- Pinned computation (§Calculating the EMV, verbatim in sense): `Distance Moved = ((H + L)/2 − (Prior H + Prior L)/2)`; `Box Ratio = ((V/100,000,000)/(H − L))`; `1-Period EMV = Distance Moved / Box Ratio`; `14-Period Ease of Movement = 14-period simple moving average of 1-period EMV`. The two-part doctrine is pinned: Distance Moved is the signed driver (positive when the current midpoint is above the prior midpoint), Box Ratio is the volume-and-range denominator (low volume with wide range shrinks the denominator and magnifies EMV; high volume with narrow range grows it and damps EMV). The 14-period SMA smoothing is the page default (SharpCharts default setting of 14 periods) and the standard form used through every worked example.
- Pinned zero semantics (§Interpreting the EMV, verbatim in sense): "when EMV is above the zero line, prices are advancing with ease, and when EMV is below the zero line, prices are declining with ease. The further from the zero line, the easier the move." The smoothing section pins the 14-period form as the trend picture ("the standard 14-period smoothed EMV gives a better picture of trends in ease of movement") against the choppy, whipsaw-prone 1-period form.
- Cross-event pin (§Suggested Scans): the publisher's own scans fire on the zero crossing in both directions — `Daily EMV(14) crosses 0` (negative-to-positive) and `0 crosses Daily EMV(14)` (positive-to-negative) — confirming entries turn on the cross event, with the regime persisting between crosses. The volume-data note is carried: "daily volume data is incomplete during the trading day. When running scans with volume-based indicators like EMV, base the scan on the 'Last Market Close'" — this record therefore evaluates completed bars only.
- Fenced on purpose: the confirmation-use doctrine (EMV confirming price breakouts/breakdowns or RSI signals — a discretionary second-leg overlay with no standalone rule attached), the 1-period EMV illustration form (page-fenced as choppy and whipsaw-prone), the 10-day-SMA-overlay / 28-day-EMV charting variants (display options, never signal rules), and the scan liquidity pre-filters (`SMA(20, Volume) > 100000`, `SMA(60, Close) > 20` — equity-universe hygiene, not signal logic). None is adopted; the record is the 14-period zero-cross leg only.
- Licence and rights: this record cites and normalizes the rule (short phrases and formulas only) and reproduces no chart, table, figure, spreadsheet, or extended prose.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — Arms/ChartSchool's 14-period EMV zero-cross gauge ported to one crypto asset as a two-sided daily system — not a lossless reproduction of Arms' discretionary equity-chart practice. Researcher-declared adaptations are exactly six: (1) single-asset BTCUSDT Binance tape (the page is equity-charted; crypto portability is a researcher carry, disclosed — the page's own scan universe is US stocks, never crypto); (2) state-hold evaluation each completed close with orders only on target change (event-identical to the publisher's `crosses 0` scan semantics in both directions — a cross plus a hold between crosses prints the same order tape as the sign-state rule below, pinned to remove any cross-vs-hold ambiguity); (3) next-open market fills on the `1d` grid (the source is cadence-silent beyond "Last Market Close"; daily closes are the declared port); (4) fixed 100%-equity single position at 1× with no leverage (the source ships no sizing); (5) no stop, no target, no trailing, no time exit (the source ships no risk leg for the zero-cross use anywhere — exits are regime-driven only, source-faithful absence); (6) a declared degenerate-bar/warmup convention (the publisher pins the formula but no zero-volume or zero-range arithmetic, so the arithmetic for undefined prints is disclosed researcher specification, never presented as a source fact). The Distance-Moved/Box-Ratio formula, the SMA-only 14-period smoothing, the above-zero/below-zero ease semantics, and both cross directions are source-faithful.

Pre-write dedup (2026-10-12): working-tree case-insensitive searches for `ease.of.movement` and `EMV(` return zero strategy records computing this indicator — this is the pool's first Arms EMV record. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state-reversal two-sided) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `force-index-100-zero-state-two-sided-btcusdt-1d-2026-10-12.md` smooths close-change-times-volume with a 100-period EMA (no range term, no volume denominator — volume multiplies commitment there, while here volume divides ease); `obv-ema-crossover-trend-two-sided-btcusdt-1d-2026-10-10.md` cumulates signed volume with no price-extent or range factor; `pvt-ema-crossover-trend-two-sided-btcusdt-1d-2026-10-11.md` cumulates volume-scaled returns with division by price, never by range; `cmf-velocity-zero-cross-ema200-bracket-two-sided-btcusdt-1d-2026-10-10.md` and `chaikin-oscillator-ad-zero-cross-momentum-divergence-two-sided-btcusdt-4h-2026-10-12.md` read intrabar close-location placement, never midpoint drift; `klinger-volume-oscillator-trigger-flip-two-sided-btcusdt-1d-2026-10-11.md` differences two volume-force EMAs with a signal-line trigger, never a midpoint-distance-over-box-ratio zero cross. Five-axis distinction: no pool record and no open PR trades the sign-state of an SMA of midpoint-distance divided by a volume-and-range box ratio.

## Economic mechanism

### Source-reported

Ease-of-movement: Arms' two-part print asks how far the midpoint travelled per unit of volume-box. A wide range on thin volume means prices moved easily (large EMV); a narrow range on heavy volume means the move was laborious (small EMV). The sign follows the midpoint drift, so sustained positive prints mean accumulation proceeds with ease and sustained negative prints mean distribution proceeds with ease. The page's doctrine is symmetric: above zero advancing with ease, below zero declining with ease — there is no long-only fence anywhere in the interpretation or scan sections.

### Research interpretation

Range-normalized ease regime port: the 14-bar SMA of distance-over-box prints can only flip on sustained, easy drift — a single high-volume-but-narrow bar damps itself out of the average by construction (big denominator), while weeks of wide-range thin-volume drift accumulate into a flip. Unlike Force Index (volume multiplies commitment — big volume amplifies), EMV inverts the volume role (big volume damps — the same price path on heavy volume prints smaller EMV), so the two records disagree precisely on high-volume trends and agree only on thin-volume ones. Unlike OBV/PVT (unbounded every-bar cumulations with no decay), the 14-period SMA forgets in three trading weeks, so the derived system is a short-horizon ease regime, not a lifetime ledger. The bet, as derived, is purely on the persistence of easy directional drift at the ~fortnight scale, never on a level, band, oscillator zone, calendar date, or funding print.

## Signal

Exact rule as pinned (Box-Ratio product form / SMA-only smoothing / length 14 / zero-cross state hold — any other value is a different, unpinned rule):

- Series (pinned): let `M_t = (H_t + L_t)/2` be the midpoint, `R_t = H_t − L_t` the range, and `V_t` the venue-native base-asset printed volume of completed `1d` bar `t` (`t = 1` is the first available bar). `DM_t = M_t − M_{t-1}` for `t ≥ 2`. The 1-period print is the publisher formula in algebraically identical product form: `E_t = DM_t × R_t × 100,000,000 / V_t`, exactly equal to `Distance Moved / Box Ratio` wherever the publisher formula is defined (the `1e8` volume divisor is kept verbatim; being a positive constant it never affects the zero-cross). Degenerate-bar convention (declared, disclosed — the publisher is silent on undefined arithmetic): a bar with `V_t ≤ 0` prints `E_t = 0` (neutral, holds state); a zero-range bar with `V_t > 0` resolves through the product form to `E_t = 0` with no division path taken. Crypto closes, highs, and lows are strictly positive regardless.
- Regime line (length pinned, arithmetic exact): `EMV_t` is the 14-period simple moving average of `E_{t-13} … E_t`, defined from the first bar where fourteen 1-period prints exist. `EMV_t` is undefined before that bar; no decision may reference it there.
- Position target (pinned, strict): evaluated at the close of each completed `1d` bar once `EMV_t` is defined: `EMV_t > 0` → long; `EMV_t < 0` → short; `EMV_t == 0` → flat (measure-zero on live tape, pinned for determinism — no tie semantics beyond this). Both directions are source-faithful; no leg is disabled. Orders fire only on target change, which is event-identical to the publisher's `crosses 0` scans in both directions.
- Orders (pinned): at most one order event per bar, placed for the next `1d` open after the decision bar: target long buys/holds 100% equity long; target short sells/holds 100% equity short; target flat closes all. A target change closes the old side and opens the new side at the same next open. Unchanged target places nothing. No intrabar evaluation, no intrabar orders, no adds, no partials, no second decision inside the fill bar for any reason including large adverse excursion. Entry and exit can never co-fire beyond the single atomic flip: the target is one state per bar.
- Risk legs (pinned absence, not invented): the source ships no stop/target/trailing/time-exit concept for the zero-cross use anywhere — the sole position-changing path is the next regime bar mapping to a different target. The derived posture is explicitly no stop, no target, no trailing, no time exit; a fortnight-scale adverse drift is ridden in full by construction.
- Direction: two-sided long/short with a measure-zero flat tie-state (derived pin matching the page's symmetric above-zero/below-zero ease doctrine and both cross scans). The research market is the Binance perpetual under the house overlay with both permissions genuinely used.

## Required data

- Completed `1d` high, low, and venue-native base-asset printed bar volumes of BTCUSDT only: three scalars per bar (`H_t`, `L_t`, `V_t`; close is used only as fill price). No funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, breadth, or cross-venue state gates any order. No multi-symbol, multi-timeframe, or external-feed dependency of any kind. The RSI-confirmation legs, the 1-period illustration form, and the scan liquidity pre-filters are fenced — none is computed.
- Single decision grid: completed daily bar. One evaluation per close; fills land on the next daily bar's open. All inputs are completed-bar prints — no provisional range or unfinished volume is ever used, per the page's own "Last Market Close" volume note. Bar range and volume are final at bar close on the venue tape.
- Warmup: 15 completed `1d` bars before the first decision (the first 1-period print needs bar 2, and fourteen prints `E_2 … E_15` must exist to form the first SMA). Bars 1–15 are flat by record rule; the first decidable close is bar 15 and its fill lands on bar 16's open. No signal before the seed window completes may trade. No repainting, no negative shift, no future reference, no full-sample normalization; the 24/7 tape needs no session template (bar membership is the venue's own daily grid — deterministic).

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared single-asset port; no cross-venue equivalence claimed). The venue's daily base-volume print replaces the page's share-volume concept one for one — both are completed-bar venue totals, never modelled intraday. The `1e8` divisor is carried verbatim as a positive scale constant with no signal effect.
- Order timing (declared port; the source is cadence-silent beyond completed-bar evaluation): completed-bar decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill: the only legs are regime-change market entries/flips/close-all orders, and at most one order exists per bar — there is no same-bar dual-fire to sequence.
- Sizing/capital/costs: fixed 100%-equity single position, no adds, no leverage (1×, no margin concept beyond the venue's own short permission), no compounding concept beyond equity — declared derivative (the source ships no sizing). Derived evaluation must carry the explicit house overlay (pinned house fees plus historical funding treatment; no hypothetical zero funding claimed — the short leg accrues genuine funding economics and neither leg is modelled funding-free). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one position (long or short) at any time; a flip needs only the next opposite-regime close (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The page ships the full construction adopted here: the Distance-Moved/Box-Ratio formula, the 1-period quotient form, the 14-period SMA standard with 14 as the SharpCharts default, the above-zero/below-zero ease partition, both zero-cross scans (`EMV(14) crosses 0` and `0 crosses EMV(14)`), and the completed-bar volume note. It ships zero adopted performance numbers for this record: the QQQ/ABT/PM/CL charts are illustration, never a return claim — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Equity-charted gauge, fenced: every worked example is a US equity or ETF (QQQ, ABT, PM, CL) and the scans filter `[type = stock] AND [country = US]`. The single-asset crypto port is a researcher carry justified only by arithmetic portability (ranges and volumes print on any tape), never by source evidence — this record is never evidence that EMV times BTCUSDT well.
2. Whipsaw admission, carried: the page concedes the 1-period form is "choppy and prone to whipsaws" and the smoothed form still dips across zero inside consolidations (the July ABT episode, the hug-the-zero-line consolidation passages). The derived system converts those episodes into flip churn, disclosed, not filtered.
3. Standalone-use caveat, carried: "Ease of Movement is best used to confirm other indicators or chart analysis. In other words, it is not a standalone indicator." This record is a standalone specification for admission purposes, never a recommendation.
4. No hidden risk layer: the source ships no stop/target/trailing concept for the zero-cross use — the sole position-changing path is the next regime bar. The absence of any stop is source-faithful absence, disclosed, not a tunable parameter here.
5. Fully exposed inside the regime: once positioned, the system rides the entire adverse excursion with no guardrail — a −50% move inside a still-positive EMV(14) is held to the last bar by construction. This is the coded trade, disclosed, not a tunable parameter here.
6. Degenerate-arithmetic boundary, fenced: the publisher pins the quotient formula but no zero-volume or zero-range arithmetic — the `V ≤ 0 → E = 0` print is declared researcher specification, and the product form is algebraically identical to the publisher quotient wherever defined. An always-trade-through-NaN implementation or a skip-the-bar implementation would each be a different, unpinned rule. No BTCUSDT daily bar is expected to trigger the convention (continuous positive-volume tape), so it changes no live-tape event.
7. Length boundary fenced: the 1-period illustration form, the 10-day-SMA-overlay display, and the 28-day charting variant are all real page content and each would be a different, unpinned rule — none is admitted here. Only the standard 14-period form is specified.
8. Derivation boundary fenced: the only non-source behavior is the six declared adaptations (single asset, state-hold evaluation, daily next-open grid, fixed sizing, degenerate-bar/warmup convention, house costs); quotient formula, SMA-only smoothing, length 14, and above/below-zero ease semantics with both cross directions are source-faithful. This record is therefore never evidence that Arms' discretionary equity practice passes anything.
9. The Box-Ratio product / SMA-14 / zero-cross / single-position two-sided / signal-only-exit stance is pinned, not removed: adding the RSI-confirmation legs, the breakout-confirmation overlay, a stop/target/filter/cooldown, trading intrabar, disabling the short leg, or sizing partially instead of 100% equity would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: Box-Ratio product / SMA-14 / zero-cross hold / next-open fills / single-position two-sided / signal-only exit / `1d` BTCUSDT are frozen.

- F1 — Length relevance: replacing the pinned SMA-14 with a 50-period SMA (a slower ease regime) must not improve net expectancy; fail ⇒ the fortnight-scale partition carries no advantage over a slower form and the record is noise-trading in disguise.
- F2 — Box-Ratio relevance: replacing the distance-over-box print with a pure midpoint-change SMA-14 (the volume-and-range denominator deleted) must not improve net expectancy; fail ⇒ Arms' ease normalization does no work and the record is a smoothed momentum follower in disguise.
- F3 — Symmetry relevance: disabling the short leg (bear-regime flat instead of short, cost-loaded comparison) must not improve risk-adjusted expectancy; fail ⇒ the two-sided pin carries dead weight — or the short leg's funding load dominates.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid completed `1d` closes; high-low-range-plus-base-volume arithmetic with no venue-specific read). The arithmetic ports across perpetual venues without structural change provided the same base-volume denomination is pinned. Funding accrues genuinely on the short leg under the house overlay (no zero-funding claim); no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market prints volume on every daily bar (bar membership is the venue's own daily grid — deterministic on any continuously traded tape). Extension to other house-universe assets, other smoothing lengths, the RSI/breakout confirmation overlays, or the scan liquidity pre-filters would each be a different, unpinned claim.

## Limitations

- Single-asset port: the source's evidence is equity-charted illustration; single-asset BTCUSDT behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- No price stop, no intra-regime exit: adverse excursion inside the regime has no guardrail; the next decision is one bar away but the regime itself can persist for weeks. This is the source-faithful posture, disclosed as the record's principal risk.
- SMA lag: a 14-period average turns after price turns by construction — entries and flips print late by design.
- Zero-region churn: a flat market oscillating around EMV = 0 produces repeated flips with no trend to capture; disclosed, not filtered.
- Standalone-use caveat: the publisher advises confirmation use with other analysis; this record is standalone for admission purposes, never a recommendation.
- Unused cost silence: the source reports no cost accounting; derived evaluation must carry the full house cost load including short-leg funding, and this record reports no net performance of any kind.
- Warmup cost: the first 15 bars are flat by record rule, so any textbook regime completing inside the seed window is deliberately untraded — pinned, not recovered.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- StockCharts ChartSchool, Ease of Movement (EMV) (Arms lineage, Distance-Moved/Box-Ratio formula, 14-period SMA standard, above-zero/below-zero ease partition, both zero-cross scans, completed-bar volume note; fetched full publisher `.md` twin 2026-10-12): https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/ease-of-movement-emv
