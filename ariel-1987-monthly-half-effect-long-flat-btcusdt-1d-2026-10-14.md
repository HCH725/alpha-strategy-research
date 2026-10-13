---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Ariel 1987 monthly half-effect first-half-hold long-flat on BTCUSDT 1d bars
created: 2026-10-14
updated: 2026-10-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 1987-03-01
sources:
  - https://doi.org/10.1016/0304-405X(87)90066-3
  - https://www.sciencedirect.com/science/article/abs/pii/0304405X87900663
  - https://ideas.repec.org/a/eee/jfinec/v18y1987i1p161-174.html
  - https://econpapers.repec.org/RePEc:eee:jfinec:v:18:y:1987:i:1:p:161-174
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Ariel 1987 monthly half-effect first-half-hold long-flat on BTCUSDT 1d bars

## Provenance

Primary source identity verified end to end (Crossref metadata hand-fetched plus publisher landing and RePEc/EconPapers records, all read 2026-10-14):

- Ariel, Robert A., `A Monthly Effect in Stock Returns` — Journal of Financial Economics, vol. 18, no. 1, 161–174 (March 1987). DOI `10.1016/0304-405X(87)90066-3`. Crossref record pins title `A monthly effect in stock returns`, container `Journal of Financial Economics`, volume `18`, issue `1`, pages `161-174`, author Ariel, print publication March 1987 (438 citing works at fetch time).
- Pinned headline spec (publisher abstract, read verbatim as rendered): `The mean return for stocks is positive only for days immediately before and during the first half of calendar months, and indistinguishable from zero for days during the last half of the month. This 'monthly effect' is independent of other known calendar anomalies such as the January effect documented by others and appears to be caused by a shift in the mean of the distribution of returns from days in the first half of the month relative to days in the last half.`
- Pinned construction (publisher-page full-text snippet, disclosed as snippet-level): each trading month is divided evenly in half with the odd middle trading day, if any, discarded, and the mean daily return of the first half significantly exceeds that of the second half. The paper's sample window, daily means, test statistics, and any table cell are fenced — never read, never carried (see Negative evidence 2).
- Bibliographic corroboration (RePEc/EconPapers, disclosed as corroboration only): IDEAS pins `Ariel, Robert A., 1987, "A monthly effect in stock returns," Journal of Financial Economics, Elsevier, vol. 18(1), pages 161-174, March`; EconPapers page fetched live 2026-10-14 (10,410 bytes, SHA-256 `b9435bc0…ee6`). No table, figure, or section number is cited anywhere in this record.
- Access boundary (disclosed, not worked around): the publisher full text sits behind a subscription/access wall and the publisher landing renders as a script shell under direct fetch; abstract-level, snippet-level, and bibliographic facts above are the entire adopted source evidence. Any construction dispute beyond the quoted phrasing is decided against this record, never patched by inference.
- Licence and rights: the paper is a published journal article — this record cites and normalizes the rule (short phrases only) and reproduces no figures, tables, or extended prose.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the paper's first-half/second-half monthly partition ported to one crypto asset as a calendar-half long-or-flat hold — not a lossless reproduction of the paper's equity study. Researcher-declared adaptations are exactly six: (1) single-asset BTCUSDT Binance venue (the equity index sample, every mean-return number, every t-statistic, and the January-effect-independence test are fenced off, never carried — see Negative evidence 1–2); (2) calendar-day halves on the 24/7 tape — hold covers the last calendar day of month M plus calendar days 1–15 of month M+1 — as the executable port of the paper's trading-day halves plus `days immediately before` (the 24/7 tape has no non-trading days, so trading-day halves map onto calendar days; the odd-middle-day discard has no calendar analogue and is dropped, disclosed — see Signal and Negative evidence 4); (3) bar-close decision with next-bar-open market fills (the paper forms no executable order timing — see Signal); (4) fixed 100%-equity single-position 1× sizing with no leverage (the paper ships no sizing rule — see Limitations); (5) a 5-bar conventional warmup flat by record rule plus house fees/funding treatment (the paper reports no costs — see Execution assumptions); (6) long-flat direction mapping only (the paper's second-half `indistinguishable from zero` finding carries no short leg — no short is enabled, explicitly none). The first-half-positive / second-half-zero partition, the unconditional calendar trigger (no return conditioning, no filter), the long-only posture (flat — never short — outside the hold), and the no-stop time-hold stance are source-faithful.

Pre-write dedup (2026-10-14): working-tree case-insensitive searches for `ariel-1987`, `monthly.effect`, `monthly.half`, `half-effect`, `first.half.hold`, `day.of.month` return no strategy record in the main tree (the only `ariel` prose hits are lineage/citation mentions: the turn-of-month record cites Ariel 1987 bibliographically inside a Lakonishok-Smidt lineage paragraph, and the pre-holiday record studies Ariel 1990, a different paper with a different ~9-session pre-closure window). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak), #49 (Gaussian channel StochRSI breakout), #63 (SuperTrend ATR-flip), #89 (Chandelier Exit stop-flip), #92 (SSL channel reversal) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `turn-of-month-4day-hold-long-btcusdt-1d-2026-10-10.md` holds only the 4-session month-turn window (last day plus first three days) twelve times per year on Lakonishok-Smidt/McConnell-Xu lineage (this record holds sixteen sessions per boundary on Ariel 1987 lineage with a different partition claim — overlap disclosed in Negative evidence 6); `santa-claus-rally-yearend-hold-long-btcusdt-1d-2026-10-12.md` holds the single annual December-to-January 7-session window; `sell-in-may-seasonal-hold-long-btcusdt-1d-2026-10-10.md` holds the six-month seasonal span; `monday-drift-weekly-calendar-hold-btcusdt-1h-2026-10-06.md` holds a weekly weekday session; `january-barometer-conditional-annual-hold-long-btcusdt-1d-2026-10-12.md` holds a full year conditioned on January sign (return-conditioned; this record is unconditional); `tsmom-12m-sign-monthly-long-btcusdt-1d-2026-10-10.md` holds a full calendar month only when the trailing 12-month return sign is positive (return-conditioned). Five-axis distinction: no pool record and no open PR holds the last-day-plus-first-fifteen-days monthly partition on an unconditional calendar trigger with no return, indicator, or seasonal-span conditioning.

## Economic mechanism

### Source-reported

Mean-shift calendar partition, not risk compensation: the mean return is positive only for `days immediately before and during the first half of calendar months` and `indistinguishable from zero` for the last half; the effect is `independent of other known calendar anomalies such as the January effect` and `appears to be caused by a shift in the mean of the distribution of returns` between halves. (All mechanism framing fenced to the paper's equity sample, never adopted as a crypto claim here.)

### Research interpretation

Pure calendar drift-capture with maximum time out of market, long-only. Unlike return-conditioned monthly systems (TSMOM, January Barometer) there is no formation leg and no losing-signal concept: the position exists if and only if the calendar says so. Unlike the 4-session turn-of-month hold the exposure is sixteen sessions per boundary (~half the tape), so the bet is on the whole first-half drift rather than the boundary pulse — and the position sits through any mid-first-half slide with no guardrail. Unlike seasonal-span holds (Sell-in-May, six months exposed) the strategy is flat through every second half including whole crises that fall outside the window — and equally unprotected against a crash landing inside the hold. The bet, as derived, is purely that the documented first-half/second-half partition ports to BTCUSDT calendar days, never on a level, band, oscillator, volume, return-sign, or funding anchor.

## Signal

Exact rule as pinned (hold = last calendar day of month M plus calendar days 1–15 of month M+1; bar-close decision; next-open fills; long-flat — any other window is a different, unpinned rule):

- Bar grid: completed `1d` bars of BTCUSDT only. Bar membership is the UTC calendar date of each daily bar — deterministic on the 24/7 tape. One evaluation per bar close, in bar-close order.
- Calendar convention (pinned): because the venue trades 24/7 with no holidays, every calendar day is a trading day, so the paper's trading-day halves map 1:1 onto calendar days with no holiday-shift rule and no session template needed — disclosed derivation, no hidden calendar table. Month lengths (28–31 days) need no lookup: the rule reads only each bar's own UTC date.
- Hold definition (pinned): for each month boundary, `D0` = last calendar day of month M (the paper's `days immediately before`, narrowed to the single disclosed session — see Negative evidence 4); `D1`..`D15` = first through fifteenth calendar days of month M+1 (the paper's `first half`, pinned to days 1–15 regardless of month length — February's second half is simply shorter, deterministic). The holding window is the sixteen sessions D0..D15.
- Position target (pinned): at the close of each completed bar `t` dated `d`, the target for the next bar is long iff the next bar's UTC date falls in a holding window (i.e. tomorrow is the last day of its month, or tomorrow's day-of-month is ≤ 15), else flat. The rule is a pure function of the bar date — no price, return, volume, or indicator input exists anywhere.
- Orders (pinned): at most one order event per bar boundary, placed for the next bar's open (next-open fill after the decision bar — the declared causal port; the paper ships no fill convention, so the sequential next-open fill is declared, never implied): flat→long target buys 100% equity at the next open; long→flat target closes all at the next open; unchanged target places nothing. No intrabar evaluation, no intrabar orders, no adds, no partials. At most two transitions exist per month boundary (entry at D0's open decided on the D0−1 close; exit at D16's open decided on the D15 close), on distinct bars — no same-bar dual-fire exists to sequence.
- Risk legs (pinned absence, not invented): the paper ships no stop/target/trailing concept for the monthly partition — the sole position-closing path is the calendar exit to flat at the D15 close (filled D16 open). The derived posture is explicitly no stop, no target, no trailing, no opposite-signal exit, no calendar extension; a fully ridden first-half slide is absorbed exactly as printed by construction.
- Direction: long-or-flat, derived-and-declared (the futures venue is still pinned as the research market under the house overlay with the short permission simply unused, and a spot-only deployment expresses the identical event set).

## Required data

- Completed `1d` bars of BTCUSDT only: bar UTC calendar date (the sole signal input) plus `open` as fill price and `close` as fill-reference (no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, or cross-venue state gates any order). No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision grid: daily bars. One evaluation per bar at its close; fills land on the next daily bar's open. All inputs are completed-bar values — no provisional intrabar value is ever used.
- Warmup: 5 completed `1d` bars flat by record rule (window predicates need only the bar's own UTC date, so the guard is conventional, not structural — mirrors the standing small-guard record-rule precedent set by the turn-of-month record). No repainting, no negative shift, no future reference, no full-sample normalization; the 24/7 tape needs no session template (month membership is the UTC calendar date of each daily bar — deterministic).

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared port of the paper's equity-index universe; no cross-venue equivalence claimed).
- Order timing (declared causal port; the paper ships no executable timing): completed-bar-close decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill is claimed. At most one order exists per bar boundary, so there is no same-bar dual-fire to sequence.
- Cash leg: flat earns nothing by record rule. No T-bill, stablecoin-lending, funding-rebate, or synthetic yield is substituted; the paper's cost-free accounting accrues no cash yield to either half.
- Sizing/capital/costs: fixed 100%-equity single position, no adds, no leverage (1×, no margin concept), no compounding concept beyond equity. The paper reports cost-free sample means, so derived evaluation must carry the explicit house overlay (pinned house fees plus historical funding treatment; no hypothetical zero funding claimed — long bars carry realized funding, flat bars carry none, and the form holds genuine flat stretches so it is never an always-in-position funding accumulator). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one long position at any time; holding windows are disjoint by calendar construction, so overlapping entries are structurally impossible (no ignore-rule needed beyond the single-position book); after any D15-close exit the next D0−1-close entry fires on schedule (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The unused short permission requires no margin-short modeling. Safety orders: explicitly none.

## Evidence

### Source-reported

The paper ships every adopted headline fact quoted in Provenance: the first-half-positive / second-half-zero partition, the `days immediately before` inclusion, the January-effect independence, and the mean-shift framing. It ships zero adopted performance numbers for this record: every mean return, test statistic, and sample-window claim in the paper describes its equity sample, never a single-asset BTCUSDT derivative — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Equity-only evidence fenced: every mean return, significance claim, and independence test in the paper belongs to its equity sample — none transfers to BTCUSDT crypto, whose month-end payroll/rebalancing microstructure differs arbitrarily, and none is adopted.
2. Number silence fenced: no daily mean, t-statistic, sample window, or partition cut from any paper table is adopted anywhere — table-level figures are omitted by access boundary, and any dispute over exact magnitudes is decided against this record, never patched by inference.
3. Cost silence fenced: the paper's sample means are cost-free statistics, not net-of-cost tradable P&L — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
4. Pre-day narrowing disclosed: the abstract's positive set reads `days immediately before` (plural); this record pins exactly one pre-session (D0, the last calendar day). Any additional pre-day drift the paper's tables may contain is discarded by declared derivation, not carried. The odd-middle-day discard likewise has no calendar analogue here and is dropped by declared derivation.
5. Fully exposed inside the hold: once entered, the position rides the entire adverse excursion with no guardrail — a −20% sixteen-session slide is held to the D15 close by construction. This is the coded trade, disclosed, not a tunable parameter here.
6. Turn-of-month overlap disclosed: sessions D0–D3 of this record's window coincide with the pool's 4-session turn-of-month hold, but the windows (16 sessions vs 4), the lineage (Ariel 1987 partition vs Lakonishok-Smidt/McConnell-Xu boundary pulse), and the claimed partition (first-half vs second-half means vs boundary-only drift) differ materially — overlap is arithmetic, not mechanism duplication. Widening, narrowing, or shifting the window would each be a different, unpinned rule.
7. No persistence claimed: this record adds no regime guard and claims no post-1987 edge of any kind — the second-half `indistinguishable from zero` reading is an equity-sample statement, never a crypto prediction.
8. Derivation boundary fenced: the only non-paper behavior is the six declared adaptations (single asset, calendar-day halves plus single D0, next-open fills, fixed sizing, warmup plus house costs, long-flat mapping); the first-half/second-half partition, the unconditional calendar trigger, the long-only posture, and the no-stop stance are source-faithful. This record is therefore never evidence that the paper's equity study passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: D0-plus-days-1–15 hold / bar-close decision / next-open fills / unconditional calendar trigger / single-position long-flat / `1d` BTCUSDT are frozen.

- F1 — Window-length relevance: a 4-session turn-of-month twin (hold D0..D3 only, same grid and fills) must not improve net expectancy; fail ⇒ the extra D4..D15 sessions add nothing over the boundary pulse and the half-month read carries no advantage over the narrower window.
- F2 — Pre-day relevance: a days-1–15-only twin (no D0 session, same grid and fills) must not improve net expectancy; fail ⇒ the single `immediately before` session adds nothing over the clean calendar-half hold.
- F3 — Selectivity relevance: buy-and-hold over the same sample must not improve net expectancy; fail ⇒ sitting out the second halves costs more in missed drift than it saves in avoided exposure — or the record's selectivity pin is doing unacknowledged work.
- F4 — Asymmetry relevance: the mirror second-half-hold twin (long D16..end plus D0 of next boundary, flat otherwise, same grid) must not outperform the pinned first-half mapping; fail ⇒ the paper's first-half-positive / second-half-zero asymmetry inverts on this tape and the partition points the wrong way.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid completed `1d` bar closes on UTC calendar dates; fills at next-bar opens; no venue-specific read). The arithmetic ports across perpetual venues without structural change. No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no holidays for the rule to skip (every calendar day is a trading day — deterministic on any continuously traded tape). Extension to other house-universe assets, windows, or timeframes would be a different, unpinned claim.

## Limitations

- Single-asset port: the paper's evidence is an equity-sample calendar partition; BTCUSDT first-half behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Microstructure mismatch: whatever month-end cash-flow or institutional mechanism sits behind the equity partition has no established crypto analogue — the port bets on calendar persistence, not on a verified crypto mechanism.
- Pre-day pin: a single D0 session is the narrow declared reading of `days immediately before`, not the sole paper convention — any wider pre-window the tables may support would differ by construction.
- Half-boundary rigidity: drift arriving on D16+ or starting D0−2 is missed by record rule; a month whose partition the tape disobeys is held anyway — disclosed, not recovered.
- Close-to-open seams: entries fill at D0's open and exits at D16's open — gap-through moves across hold edges are taken at post-move opens, never at the edge.
- Warmup cost: the first 5 daily bars are flat by record rule, so a hold window completing inside warmup is deliberately untraded — pinned, not recovered.

## Implementation status

not-implemented. No Hummingbot controller/executor has been written for this record; the Execution assumptions section names the exact pinned engine path (package `20260920`, VERSION `dev-2.17.0`, bar-close decision on completed `1d` bar UTC dates, next-open market fills, single-asset 100%-equity 1× long-or-flat) that a future implementation must target, with representative event-level Qlib/Hummingbot parity required before any mass screening.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. PASS means the declared derived strategy is causally expressible under the pinned Hummingbot model — not profitable, not Qlib-paritied, not source-equivalent, not live-tradable.

## Related Wiki records

None.

## Sources

- Ariel, Robert A. (1987). A Monthly Effect in Stock Returns. Journal of Financial Economics 18(1), 161–174. https://doi.org/10.1016/0304-405X(87)90066-3 (Crossref-verified 2026-10-14; publisher landing https://www.sciencedirect.com/science/article/abs/pii/0304405X87900663; RePEc https://ideas.repec.org/a/eee/jfinec/v18y1987i1p161-174.html; EconPapers https://econpapers.repec.org/RePEc:eee:jfinec:v:18:y:1987:i:1:p:161-174 fetched live 2026-10-14, 10,410 bytes, SHA-256 `b9435bc0…ee6`)
