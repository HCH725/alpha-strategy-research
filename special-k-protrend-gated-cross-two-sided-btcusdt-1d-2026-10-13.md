---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Pring Special K pro-trend gated cross two-sided on BTCUSDT 1d bars
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
  - https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/prings-special-k
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Pring Special K pro-trend gated cross two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (fetched and verified live 2026-10-13):

- StockCharts ChartSchool, `Pring's Special K` — first-party documentation of Martin Pring's indicator (the page names him as creator: "Created by Martin Pring, Special K is a momentum indicator that combines short-, intermediate-, and long-term velocity into one complete series, thereby giving us truly summed cyclicality"): https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/prings-special-k — pinned 12-term formula block (verbatim in sense): "Special K = 10 Period Simple Moving Average of ROC(10) * 1 + 10 Period Simple Moving Average of ROC(15) * 2 + 10 Period Simple Moving Average of ROC(20) * 3 + 15 Period Simple Moving Average of ROC(30) * 4 + 50 Period Simple Moving Average of ROC(40) * 1 + 65 Period Simple Moving Average of ROC(65) * 2 + 75 Period Simple Moving Average of ROC(75) * 3 + 100 Period Simple Moving Average of ROC(100) * 4 + 130 Period Simple Moving Average of ROC(195) * 1 + 130 Period Simple Moving Average of ROC(265) * 2 + 130 Period Simple Moving Average of ROC(390) * 3 + 195 Period Simple Moving Average of ROC(530) * 4". Pinned data requirement: "at least 725 data points are required to accurately calculate this indicator. If less data is available, then the final line of the calculation is skipped." Pinned short-term system (prose): "One solution is to determine its position relative to its 10-day MA. Positive readings (i.e., above the MA) would indicate a primary bull market and vice versa"; "trades from the long side would be initiated when the Special K itself crosses above its 10-day MA"; short trades when "the Special K is below its long-term MA and crosses below its 10-day MA"; "No buy signals are generated during the bearish periods, only sell signals". Pinned long-term signal line ("Using with SharpCharts"): "The second line is a double-smoothed moving average of the raw Special K value, which acts as a signal line"; "The default parameter values are 100,100". Pinned scan pair (Suggested Scans, verbs as printed): bullish — "A bullish signal is triggered when Special K crosses over its 10-day moving average" with clauses `[Special K > Special K Signal(100,100)]` AND `[Special K x SMA(10,Special K)]`; bearish — "A bearish signal is triggered when Special K crosses below its 10-day moving average" with clauses `[Special K < Special K Signal(100,100)]` AND `[SMA(10,Special K) x Special K]`. Licence and rights: public indicator-reference page — this record cites and normalizes the formula and trigger (short phrases and arithmetic only) and reproduces no figures, spreadsheet, or extended prose.
- Corroborating convention (same site, cited for one definition only): StockCharts ChartSchool `Rate-of-Change (ROC)` pins `ROC = [(Close - Close n periods ago) / (Close n periods ago)] * 100`: https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/rate-of-change-roc — adopted as the meaning of each `ROC(N)` leg above (the Special K page writes `ROC(10)` … `ROC(530)` without restating the ratio).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the page's two scan clauses assembled into a mechanical two-sided daily reversal (gated 10-day-MA cross entries, opposite-signal reversal exits) — not a lossless reproduction of a source trading system, because the source is an indicator reference, not a backtest: it ships no order, no sizing, no fill convention, no venue, and no cost assumption. Pring's own caution ("rather than blindly using this approach as a mechanical system, it's better to use pro trend signals as an alert and then use other indicators as a filter in a 'weight of the evidence' approach") is fenced as discretionary advice, never a rule here. Researcher-declared adaptations are exactly six: (1) mechanical pin — every qualified scan-clause trigger trades (trendline-break, pattern-confirmation, and weight-of-evidence overlays fenced, see Negative evidence); (2) scan-to-strategy assembly — the bullish/bearish scan entry predicates become order triggers and the opposite qualified trigger becomes the sole exit (the scans pin entries only; reversal exits are the declared assembly, stated here); (3) same-bar-close fills on completed `1d` bars (the source declares no execution timing); (4) an adopted 930-bar warmup with pre-warmup bars flat by record rule (covers the source's 725-point minimum plus trigger/signal-line seeding — see Required data; the source's short-history skip-the-final-line variant is never used here); (5) house sizing/capital/costs replacing the absent source economics (see Execution assumptions); (6) venue port from the page's equity examples (SPY, $CRB, GLD, DJP) to `BTCUSDT` Binance perpetual on the source-native daily frame. The 12-term construction, all weights, all ROC/SMA lengths, the (100,100) double-smoothed signal line, the 10-day trigger MA, both gated cross triggers, and the no-stop/no-target posture are source-faithful.

Pre-write dedup (2026-10-13): working-tree case-insensitive searches for `special-k`, `specialk`, `special_k`, and `pring` return zero strategy records using this source, author, indicator, or mechanism — the lone `pring` token anywhere is the English prose "no Pring-theory paragraph" inside `kst-signal-cross-trend-two-sided-btcusdt-1h-2026-10-09.md` (an FMZ-sourced summed-ROC record, distinguished below), never this construction. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-reversal two-sided) — different mechanisms, indicators, and sources. Closed research PRs contain no Special K record (title search for `special`/`pring` over the closed queue returns zero hits; latest closed includes #163 PMO, #162 January Barometer, #161 Santa Claus Rally, #160 Slow Stochastic). Closest pool records differ in mechanism class: `kst-signal-cross-trend-two-sided-btcusdt-1h` is an FMZ-scripted 4-term ROC sum (`sma(roc,10/10/10/15)`, weights 1/2/3/4) crossed raw against its own 9-bar signal on `1h` with no regime gate of any kind; `tsi-signal-cross-reversal-btcusdt-1d` is a Blau double-smoothed change/abs-change normalization (25/13/13), never a weighted SMA-of-ROC sum; `pmo-signal-cross-reversal-two-sided-btcusdt-1d` is Swenlin's custom-smoothed ratio ROC (35/20/10), never a multi-horizon summed cyclicality aggregate. Five-axis distinction: no pool record and no open PR evaluates Pring's 12-term 1/2/3/4-weighted summed-cyclicality Special K with a (100,100) double-smoothed signal-line position gate and 10-day-MA cross triggers on any market or frame.

## Economic mechanism

### Source-reported

Summed-cyclicality thesis: the Special K "combines short-, intermediate-, and long-term velocity into one complete series, thereby giving us truly summed cyclicality", with "two functions": "Identify primary trend reversals at a relatively early stage" and "Use that information to time short-term pro-trend price moves". Cycle framing: "The formula assumes that prices are revolving around the four-year business cycle"; in a linear uptrend the indicator leads turning points, in a truncated cycle (1987 crash example) it lags — "most of the time, the price and Special K reverse simultaneously". Pro-trend discipline: "trades executed in the direction of the main trend are more likely to be successful than those generated in a counter-cyclical way", operationalized as Special K position relative to its 10-day MA (above = primary bull market, below = bear), with long entries only from cross-above and short entries only from cross-below. Long-term context: "It is normal to run a moving average through the Special K. The default is a 100-day smoothed by a 100-day SMA. Crossovers of the average typically signal a reversal in the direction of the primary trend."

### Research interpretation

Always-in-market primary-trend rotation that only spends pro-trend ammunition: after the first qualified trigger the system is long-or-short, flipping solely on the opposite qualified trigger. Unlike ungated signal-cross systems (the pool's KST record fires every cross), a cross against the long-term (100,100) signal-line position is ignored entirely — the system pays whipsaw only inside the prevailing primary trend, never for counter-trend stabs. Unlike level systems there is no overbought/oversold constant anywhere — both gates are relational (aggregate vs its own averages), so the rule ports across assets without a per-asset signature range. Unlike the source's discretionary use (nine-month trendline breaks, GLD-style pattern confirmation, multi-indicator weight-of-evidence), the derived record spends no confirmation of any kind: the bet is purely that daily Special K rotations, pre-filtered by the primary-trend gate, precede multi-week directional drift often enough to survive intra-trend chop, with the 12-term 1/2/3/4-weighted smoothing plus the double gate as the sole noise defence. The US-stock scan liquidity floors and the commodity/equity examples gate nothing here.

## Signal

Exact rule as pinned (Pring 12-term weighted SMA-of-ROC Special K with 10-day trigger MA and (100,100) double-smoothed signal-line gate; strict confirmed-bar triggers only — any other term, weight, length, gate, trigger, or fill is a different, unpinned rule):

- Price input (pinned): `close` of completed `1d` bars only. The source's worked examples and scan reference run on daily closes; no `open`, `high`, `low`, or `volume` enters any order-gating series.
- ROC legs (site-convention pinned): `ROC(N)(t) = (Close(t) - Close(t-N)) / Close(t-N) * 100` for N in {10, 15, 20, 30, 40, 65, 75, 100, 195, 265, 390, 530}. Division is safe by record rule: BTCUSDT closes are strictly positive (a zero print would be a data error, never a signal — stated, not patched).
- Special K aggregate (pinned 12-term, weights pinned 1/2/3/4 per cycle group): `SK(t) = 1*SMA(ROC10,10) + 2*SMA(ROC15,10) + 3*SMA(ROC20,10) + 4*SMA(ROC30,15) + 1*SMA(ROC40,50) + 2*SMA(ROC65,65) + 3*SMA(ROC75,75) + 4*SMA(ROC100,100) + 1*SMA(ROC195,130) + 2*SMA(ROC265,130) + 3*SMA(ROC390,130) + 4*SMA(ROC530,195)` — simple moving averages throughout, exactly as the source writes "Simple Moving Average" on every term.
- Trigger line (pinned): `TRIG(t) = SMA(SK, 10)` — the source's "10-day MA".
- Gate line (pinned): `SIGL(t) = SMA(SMA(SK, 100), 100)` — the source's "100-day smoothed by a 100-day SMA" with "default parameter values 100,100".
- Entry long (scan-pinned conjunction): on the first completed bar with a cross of Special K above its trigger (`SK(t) > TRIG(t)` and `SK(t-1) <= TRIG(t-1)`) AND long-term position (`SK(t) > SIGL(t)`), buy at that bar's close. Prior-bar confirmation means the cross resolves causally — no provisional intrabar value is ever read.
- Entry short (scan-pinned mirror): on the first completed bar with `SK(t) < TRIG(t)` and `SK(t-1) >= TRIG(t-1)` AND `SK(t) < SIGL(t)`, sell short at that bar's close.
- Gated-out crosses (pinned posture, structural): a trigger cross whose gate predicate fails on the cross bar is ignored entirely — the position holds (or stays flat if none). No bar ever fires both legs: both strict-cross predicates cannot hold on one bar, so no same-bar ordering ambiguity exists. The measure-zero edge `SK(t) == TRIG(t)` (or exact gate-line equality) fires neither leg and the position holds — stated, not patched.
- Risk legs (pinned posture): no stop, no target, no trailing, no time exit — the source ships none (its risk management is the discretionary weight-of-evidence check, fenced). The sole position-closing path on each side is the opposite qualified trigger, which reverses the position in full.
- Direction: two-sided with reversal only. Before the first post-warmup qualified trigger the system is flat (no position by construction); after it, always-in-market — there is no flat state, disclosed, not missing.

## Required data

- Completed `1d` bars of BTCUSDT only: `close` (sole series read — all twelve ROC legs, all smoothings, trigger, gate, and both predicates). No `open`, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state gates any order. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (the source's scan liquidity floors and equity examples gate nothing here).
- Single decision grid: one evaluation per completed daily bar; both legs read only confirmed closes of bars `t` and `t-1` (plus history for the warmup arithmetic below).
- Warmup: the longest leg `ROC(530)` needs 531 closes; the longest smoothing `SMA(…,195)` needs 195 aggregate values on top, so the first full raw Special K lands on the 725th completed bar — exactly the source's "at least 725 data points". The trigger `SMA(SK,10)` needs 9 more (734th bar); the double-smoothed gate needs 99 + 99 more (923rd bar). Structural minimum is therefore the 923rd completed `1d` bar. The adopted warmup is the first 930 completed `1d` bars flat by record rule (predeclared researcher choice — covers 923 plus seeding margin); no signal before bar 931 may trade. SMA seeds are a deterministic record-rule convention (first-available fill; immaterial beside the 930-bar flat). The source's short-history skip-the-final-line variant is never used — evaluation requires history of at least 930 bars (satisfied by BTCUSDT `1d` history). No repainting, no negative shift, no future reference, no full-sample normalization; the 24/7 tape needs no session template.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared port of the page's equity/commodity examples; no cross-venue equivalence claimed).
- Order timing (declared derivation — the source is an indicator reference with no execution semantics): completed-bar decision with same-bar-close execution, compatible with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). This record makes no claim about any source fill timing because the source declares none. No maker-touch, queue, or intrabar-path-dependent fill: with mutually exclusive trigger legs and no stop/limit legs, there is no same-bar ordering ambiguity of any kind.
- Sizing/capital/costs: the source ships no capital, sizing, commission, fee, slippage, or margin assumption anywhere — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all) apply to the derived evaluation here, never presented as source-native behavior. The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one position at any time; qualified opposite triggers reverse in full in one step; same-side refires while already positioned are no-ops (single position, no adds); re-entry needs only the next qualified opposite trigger (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The short leg requires margin-short permission, realistic on the pinned perpetual venue.

## Evidence

### Source-reported

The page ships the construction adopted here: Pring authorship, the summed-cyclicality thesis, the full 12-term weighted formula with all ROC and SMA lengths, the 725-point minimum, the 10-day-MA regime/trigger prose, the (100,100) double-smoothed signal line, and both Suggested-Scan trigger clauses (cross-over-10-day-MA gated by above-signal, cross-under gated by below-signal). Descriptive cycle context as printed: four-year business-cycle assumption, lead-in-trend versus late-in-truncated-cycle behavior, 2003/2009 MA-cross-plus-trendline-break bottoms — fenced as description, never rules. It ships zero adopted performance numbers for this record: no backtest, no win rate, no return table appears anywhere on the page — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Mechanical-use caution fenced: Pring warns against blind mechanical use ("rather than blindly using this approach as a mechanical system, it's better to use pro trend signals as an alert and then use other indicators as a filter in a 'weight of the evidence' approach") and exhibits a subpar Example Sell Point fired while the system lagged in bearish mode — all discretionary filtering with no codable thresholds, fenced as advice, never rules. This record trades every qualified trigger with eyes open (adaptation (1), disclosed).
2. Trendline/pattern techniques fenced: nine-month-plus Special K trendline breaks, combined trendline-plus-MA-cross confirmation, and GLD-style price-pattern confirmations are chart-reading techniques with no codable predicates in the source — none gates any order here.
3. Scan liquidity floors fenced: the US-stock universe, 20-day average-volume and 60-day average-close floors are a screening use with a different event set, never strategy behavior here.
4. Short-history variant fenced: the "final line skipped" short-data calculation is a different, unpinned construction — never used; evaluation requires the full 930-bar history.
5. Gate-ignored chop, admitted plainly: gated-out crosses are skipped even when the trigger cross is violent, and qualified alternating crosses flip the full position with no confirmation, no cooldown, and no cost guard. Adverse excursion between qualified triggers has no guardrail beyond the opposite qualified trigger, which the (100,100) gate can delay further. This is the coded trade, disclosed, not a tunable parameter here.
6. Derivation boundary fenced: the only non-source behaviors are the mechanical-trigger pin, the scan-to-strategy reversal-exit assembly, same-bar-close fills, the adopted 930-bar warmup with record-rule pre-warmup flat, house sizing/costs, and the equity→BTCUSDT-perp venue port — all predeclared above; authorship, summed-cyclicality thesis, 12-term 1/2/3/4-weighted construction, all ROC/SMA lengths, 725-point minimum, 10-day trigger, (100,100) gate, both gated triggers, exclusivity, and the no-stop/no-target/no-cooldown posture are source-faithful. This record is therefore never evidence that any source trading system passes.
7. The twelve `ROC(N)`/`SMA(·,N)` literals, the 1/2/3/4 cycle-group weights, the ChartSchool ROC ratio convention, the `100,100` double smoothing, the 10-day trigger, the strict confirmed-bar crosses (not touches, not level holds), the gate conjunction on the cross bar, the full reversal, the two-sided stance, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning any length, reweighting any term, swapping SMAs for EMAs, dropping the gate, converting a cross into a touch or a level/zero-line hold, adding a stop/target/filter/cooldown/gate, dropping a side, or exiting to flat instead of reversing would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 12-term construction / weights / ROC and SMA lengths / 10-day trigger / (100,100) gate / close-only Special K vs own-average triggers / strict confirmed crosses / full reversal / two-sided / `1d` BTCUSDT / same-bar-close fills / 930-bar warmup are frozen.

- F1 — Trigger relevance: freezing direction to the first post-warmup qualified trigger side (hold that side for the whole sample, ignoring all later triggers) must not improve net expectancy; fail ⇒ the trigger sequence adds nothing over the first regime read.
- F2 — Gate relevance: dropping the (100,100) position gate (every 10-day-MA cross trades, same reversal structure) must not improve net expectancy; fail ⇒ the primary-trend gate adds nothing over the raw trigger cross.
- F3 — Trigger-horizon relevance: replacing the 10-day-MA trigger cross with a Special K-vs-(100,100)-signal-line cross (same gate conjunction, same reversal structure) must not improve net expectancy; fail ⇒ the fast 10-day trigger adds nothing over the slow signal-line cross.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid completed `1d` bars; close-ratio arithmetic with no venue-specific read). The close-only arithmetic ports across perpetual venues without structural change. The short leg requires margin-short permission (realistic on perpetual venues; a spot-only deployment cannot express the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read, so session-gap behavior needs no approximation; "10-day" and "100-day" source phrasing maps 1:1 onto ten and one hundred `1d` bars. The four-year business-cycle framing is unfenced only as context — this record times no cycle and ports no equity level. Extension to other house-universe assets, formation inputs, or timeframes would be a different, unpinned claim.

## Limitations

- Indicator-doc sourcing: the source proves constructibility and trigger semantics, never profitability — no performance is claimed here for exactly this reason.
- Whipsaw by construction: Pring's own caution and the exhibited subpar sell point admit lagging, unprofitable rotation signals; the derived record takes every qualified one, disclosed, not recovered.
- Triple lag at V-turns: twelve smoothings up to 195 bars plus a 10-bar trigger average plus a double-100 gate average — a sharp reversal must drag the aggregate across the trigger gap while the slow gate still permits it, so entries arrive strictly after the turn by code, and the gate can strand the system through the turn it was built to catch. The lag is the coded smoother, disclosed, not shortened.
- Seed convention: pre-warmup SMA seeds are a deterministic record-rule convention, disclosed for completeness (immaterial beside the 930-bar flat warmup).
- Open-confirmation lag: none beyond the bar close — decisions and fills share the completed close bar by declared derivation; gap-through moves across closes are taken at post-move closes, never at pre-move prices.
- Warmup cost: the first 930 daily bars are flat by record rule — pinned, not recovered (roughly two and a half years of `1d` history consumed before the first admissible signal).

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- StockCharts ChartSchool, Pring's Special K (Pring authorship, summed-cyclicality thesis, 12-term 1/2/3/4-weighted SMA-of-ROC formula with ROC lengths 10/15/20/30/40/65/75/100/195/265/390/530 and SMA lengths 10/10/10/15/50/65/75/100/130/130/130/195, 725-point minimum with skip-variant, 10-day-MA regime/trigger prose, (100,100) double-smoothed signal line, both Suggested-Scan gated cross clauses, mechanical-use caution, trendline/pattern fencing, four-year-cycle context; verified live 2026-10-13): https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/prings-special-k
- StockCharts ChartSchool, Rate-of-Change (ROC) (ROC ratio convention `[(Close - Close n periods ago) / (Close n periods ago)] * 100` adopted for each Special K leg; verified live 2026-10-13): https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/rate-of-change-roc
