---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Bali-Cakici-Whitelaw 2011 MAX lottery-avoidance top-quintile-gated hold long-flat on BTCUSDT 1d bars
created: 2026-10-14
updated: 2026-10-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2011-02-01
sources:
  - https://doi.org/10.1016/j.jfineco.2010.08.014
  - https://www.nber.org/papers/w14804
  - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1354512
  - https://pages.stern.nyu.edu/~rwhitela/papers/max%20jfe11.pdf
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bali-Cakici-Whitelaw 2011 MAX lottery-avoidance top-quintile-gated hold long-flat on BTCUSDT 1d bars

## Provenance

Primary source identity verified end to end (Crossref metadata hand-fetched plus the authors' NBER working paper read in full locally, 2026-10-14):

- Bali, Turan G., Cakici, Nusret, and Whitelaw, Robert F., `Maxing Out: Stocks as Lotteries and the Cross-Section of Expected Returns` — Journal of Financial Economics, vol. 99, 427–446 (February 2011). DOI `10.1016/j.jfineco.2010.08.014` (Crossref-pinned title, container, volume `99`, pages `427-446`).
- Actually-read text (disclosed as the working-paper version, not the typeset journal): NBER Working Paper `14804` (March 2009), fetched live 2026-10-14 as a 360,804-byte 50-page PDF (SHA-256 `8039f722…1826612`), converted locally and read in full (`pypdf` extraction, 107,607 characters).
- Pinned headline spec (working-paper text, read verbatim modulo PDF hyphenation noise): `MAX` is `the maximum daily return within the previous month` (Appendix eq. 2, `MAX = max(R(1)…R(D))` over the month's daily returns); `Decile portfolios are formed every month from July 1962 to December 2005 by sorting stocks based on the maximum daily return (MAX) over the past one month`; the data are daily/monthly CRSP returns for all NYSE/AMEX/NASDAQ firms (January 1926–December 2005 raw file, July 1962–December 2005 estimation sample, 522 months); sorts use the formation month's MAX and measure the following month's returns (Table I caption and Section II.B prose).
- Pinned headline findings (working-paper text, qualitative only — no return, alpha, or t-statistic number is adopted anywhere in this record): `a negative and significant relation between the maximum daily return over the past one month (MAX) and expected stock returns`; the value-weighted high-minus-low MAX decile raw and alpha gaps both `exceed 1% per month` in magnitude; the decline is not uniform — `The average returns of deciles 1 to 7 are approximately the same` while `going from decile 7 to decile 10, average returns drop significantly`, with the top deciles carrying average MAX levels near 9%, 12%, and 24%; the paper's read is lottery preference — `investors view these stocks as valuable lottery-like assets, with a small chance of a large gain` — and the effect survives controls for size, book-to-market, momentum, short-term reversals, liquidity, and skewness. (All mechanism and magnitude framing fenced to the paper's equity sample, never adopted as a crypto claim here.)
- Licence and rights: the paper is a published journal article plus openly hosted author/NBER working papers — this record cites and normalizes the rule (short phrases and the one definitional equation only) and reproduces no figures, tables, or extended prose.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the paper's prior-month-MAX sort ported to one crypto asset as a monthly top-quintile lottery-avoidance long-or-flat hold — not a lossless reproduction of the paper's equity cross-sectional study. Researcher-declared adaptations are exactly six: (1) single-asset BTCUSDT Binance venue (every cross-sectional sort, decile breakpoint, alpha, t-statistic, and return number is fenced off, never carried — see Negative evidence 1–2); (2) calendar-month formation on the 24/7 tape with close-to-close simple daily returns (the paper's CRSP daily returns include distributions; BTC has none — see Signal and Negative evidence 4); (3) the paper's monthly formation/holding cadence mirrored exactly (sort on completed month M, hold month M+1 — see Signal); (4) the top-quintile time-series rank gate as the lottery-avoidance threshold (the paper never trades a single-asset threshold rule — see Negative evidence 3); (5) month-end-close decision with next-bar open fills, fixed 100%-equity 1× sizing, and a 37-formation-month structural warmup (the paper ships no order timing, sizing, or costs — see Execution assumptions); (6) long-flat direction mapping only (the paper's long-short decile framing carries no short leg here — no short is enabled, explicitly none). The MAX definition, the avoid-extreme-MAX direction, and the no-stop time-hold stance are source-faithful.

Pre-write dedup (2026-10-14): working-tree case-insensitive filename searches for `lottery|maxing|bali|cakici|whitelaw` return only the unrelated `pmax-profit-maximizer-ma-cross-flip-two-sided-btcusdt-15m-2026-10-12.md` (a Profit-Maximizer MA-cross indicator flip, different author/source/mechanism); content searches for `maximum daily return|MAX decile|stocks as lotteries|lottery-like|bali|cakici|whitelaw` return zero strategy records. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak), #49 (Gaussian channel StochRSI breakout), #63 (SuperTrend ATR-flip), #89 (Chandelier Exit stop-flip), #92 (SSL channel reversal) — different mechanisms, indicators, and sources; the last-100 closed PR titles carry no lottery/MAX-family record. Closest pool records differ in mechanism class: `jegadeesh-titman-6m-6m-momentum-long-flat-btcusdt-1d-2026-10-13.md`, `novy-marx-12-7-intermediate-momentum-long-flat-btcusdt-1d-2026-10-13.md`, `liu-tsyvinski-1w-momentum-long-flat-btcusdt-1d-2026-10-13.md`, and `tsmom-12m-sign-monthly-long-btcusdt-1d-2026-10-10.md` condition on formation-period return levels/signs (this record conditions on the single largest daily spike inside the month versus its own history — a high-MAX month with a flat total return still forces flat here and would not trigger any return-sign rule); `gervais-kaniel-mingelgrin-high-volume-premium-long-flat-btcusdt-1d-2026-10-14.md` trades a volume-shock event with no return input; `lehmann-1990-weekly-reversal-long-flat-btcusdt-1d-2026-10-13.md` and `jegadeesh-1990-monthly-reversal-long-flat-btcusdt-1d-2026-10-13.md` trade prior-period total-return reversal (opposite direction mapping, no spike statistic); `monday-drift-weekly-calendar-hold-btcusdt-1h-2026-10-06.md`, `turn-of-month-4day-hold-long-btcusdt-1d-2026-10-10.md`, and `ariel-1987-monthly-half-effect-long-flat-btcusdt-1d-2026-10-14.md` are pure calendar partitions with no price input. Five-axis distinction: no pool record and no open PR conditions exposure on a prior-month maximum-daily-return lottery-avoidance gate.

## Economic mechanism

### Source-reported

Lottery-preference overpricing, not risk compensation: investors with a preference for upside potential `pay more for` stocks exhibiting extreme positive daily returns and accept lower expected returns on them, viewing them `as valuable lottery-like assets, with a small chance of a large gain` — so high-MAX stocks earn lower subsequent returns even after risk and characteristic controls. (All mechanism framing fenced to the paper's equity sample, never adopted as a crypto claim here.)

### Research interpretation

Single-spike-regime drift-avoidance, long-only, monthly cadence. Unlike return-conditioned momentum systems there is no formation total return and no winner/loser ranking: the position exists if and only if the just-completed month's single largest up-day is unremarkable against its own three-year history. Unlike volume-shock records volume never enters anywhere. Unlike calendar holds there is no date input anywhere — month boundaries are only the formation/holding grid, never a long/flat partition. The bet, as derived, is purely that the documented extreme-MAX underperformance partition ports to BTCUSDT monthly bars, never on a level, band, return-sign, weekday, or funding anchor — and the position sits through any within-regime slide with no guardrail.

## Signal

Exact rule as pinned (calendar-month formation; month-end-close decision; next-bar-open fills; long-flat — any other month definition, return definition, trailing window, rank cutoff, or threshold is a different, unpinned rule):

- Bar grid: completed `1d` bars of BTCUSDT only. Formation months are pinned calendar months in UTC (January 01 00:00:00 through the month's last day 23:59:59). One evaluation per month, in month order.
- Daily return (pinned): `r(t) = (C(t) − C(t−1)) / C(t−1)` on consecutive completed daily bars (`C` = close; simple, not log; close-to-close, never high/low/open-based). The first history bar carries no `r` (no predecessor — skipped, pinned). Venue-checked guard: closes are strictly positive on any traded tape, so no divide-by-zero branch can trigger; if a non-positive close ever printed, that day is excluded and the month uses its remaining days (defensive pin, disclosed, never exercised).
- Formation statistic (pinned, paper's Appendix eq. 2): `MAX(M) = max r(t)` over daily bars dated in calendar month M. A partial first history month uses whatever daily bars exist (deterministic as printed).
- Trailing pool (pinned declared derivation): `S(M) = {MAX(M−36) … MAX(M−1)}` — the 36 completed formation months strictly preceding M.
- Cutoff (pinned order statistic, no interpolation): `q80(M)` = the 29th smallest value of `S(M)` (`ceil(0.8 × 36) = 29`, top-quintile boundary of the paper's own quintile language, ported to time series — researcher-pinned, never a paper convention).
- Position target (pinned): the target for calendar month `M+1` is long iff `MAX(M) < q80(M)` (strict inequality; the exact tie maps to flat — measure-zero tie rule, pinned), else flat.
- Orders (pinned): at most one order event per month boundary, placed for the next month's first bar open (next-open fill after the month-end decision bar — the declared causal port; the paper ships no fill convention): flat→long target buys 100% equity at the first bar's open of month M+1; long→flat target closes all at the first bar's open of month M+1; unchanged target places nothing. No intrabar evaluation, no intrabar orders, no adds, no partials. Decisions on distinct month-ends fill on distinct month-opens — no same-bar dual-fire exists to sequence.
- Risk legs (pinned absence, not invented): the paper ships no stop/target/trailing concept for the MAX partition — the sole position-closing path is the regime exit to flat at a month-end close (filled next open). The derived posture is explicitly no stop, no target, no trailing, no opposite-signal exit, no calendar extension; a fully ridden within-regime slide is absorbed exactly as printed by construction.
- Direction: long-or-flat, derived-and-declared (the futures venue is still pinned as the research market under the house overlay with the short permission simply unused, and a spot-only deployment expresses the identical event set).

## Required data

- Completed `1d` bars of BTCUSDT only: `close` (daily `r` and monthly `MAX`), `open` as fill price (no `high`, no `low`, no volume, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, supply-feed, sentiment, macro, session-template, or cross-venue state gates any order). No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision grid: one evaluation per month at the last bar's close; fills land on the next month's first bar open. All inputs are completed-bar values — no provisional intrabar value is ever used.
- Warmup: flat until the month-end close at which the first computable target exists (the first computable target needs 36 trailing plus one current formation month = 37 completed formation months) — structural, not conventional: on this venue (history opening August 2017) that is the 2020-08-31 close, so the first position month is September 2020. No repainting, no negative shift, no future reference, no full-sample normalization (every `MAX` is a same-month extremum; the cutoff is a trailing order statistic).

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared port of the paper's NYSE/AMEX/NASDAQ universe; no cross-venue equivalence claimed).
- Order timing (declared causal port; the paper ships no executable timing): month-end-bar-close decision with next-bar open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill is claimed. At most one order exists per month boundary, so there is no same-bar dual-fire to sequence.
- Cash leg: flat earns nothing by record rule. No T-bill, stablecoin-lending, funding-rebate, or synthetic yield is substituted; the paper's cost-free accounting accrues no cash yield to either regime.
- Sizing/capital/costs: fixed 100%-equity single position, no adds, no leverage (1×, no margin concept), no compounding concept beyond equity. The paper reports cost-free sample statistics, so derived evaluation must carry the explicit house overlay (pinned house fees plus historical funding treatment; no hypothetical zero funding claimed — long months carry realized funding, flat months carry none, and the form holds genuine flat stretches so it is never an always-in-position funding accumulator). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one long position at any time; month regimes are disjoint by calendar construction, so overlapping entries are structurally impossible (no ignore-rule needed beyond the single-position book); after any month-end exit the next month-end decision fires on schedule (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The unused short permission requires no margin-short modeling. Safety orders: explicitly none.

## Evidence

### Source-reported

The paper ships every adopted headline fact quoted in Provenance: the within-month maximum-daily-return MAX definition, the every-month decile formation on prior-month MAX with following-month holding, the July-1962–December-2005 NYSE/AMEX/NASDAQ CRSP sample, and the negative-MAX/positive-lottery-preference headline with its top-decile concentration shape. It ships zero adopted performance numbers for this record: every return gap, alpha, and t-statistic in the paper describes its equity cross-section, never a single-asset BTCUSDT derivative — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Cross-section fenced: every decile sort, alpha, t-statistic, transition matrix, bivariate sort, and Fama-MacBeth slope in the paper belongs to its 1962–2005 equity cross-section — none transfers to a single-asset crypto time-series rule, and none is adopted.
2. Number silence fenced: no return gap, alpha, t-statistic, percentile level, or sample-window moment from any paper table or figure is adopted anywhere — figures are omitted by rule, and any dispute over exact magnitudes is decided against this record, never patched by inference.
3. Threshold pin disclosed: the paper sorts and holds deciles but never trades a single-asset `MAX < q80` time-series rule — the trailing-36-month top-quintile gate is researcher-pinned from the paper's quintile/decile-concentration language, never a paper convention. Any other window, cutoff, or level would be a different, unpinned rule.
4. Return-definition derivation disclosed: the paper's CRSP daily returns are distribution-inclusive equity returns; this record uses simple close-to-close crypto returns (BTC has no distributions to adjust for). Skipped-day calendars differ (equity weekends/holidays versus the 24/7 tape) — fenced, never adjusted.
5. Multi-day-average variant fenced: the paper's Table-II average-of-top-N robustness is cited as comfort only — this record pins the single-day MAX (N=1), never the averages, never a claim the paper blesses the choice beyond its own `for simplicity we focus on the single day measures` sentence.
6. Fully exposed inside the regime: once long for a month, the position rides the entire adverse excursion with no guardrail — a −20% month inside a below-cutoff hold is held to the next month-end close by construction. This is the coded trade, disclosed, not a tunable parameter here.
7. Momentum/reversal-family overlap disclosed: high-MAX months often coincide with high prior-month total returns, so this record will sometimes agree with short-term-reversal shorts by construction — but the trigger (single-day spike versus own history) differs materially from every total-return-sign rule in the pool, and the direction mapping (avoid spike months by going flat) is not a reversal trade; agreement is arithmetic, not mechanism duplication. Replacing MAX with the month's total return would be a different, unpinned rule (see F2/F4).
8. Derivation boundary fenced: the only non-paper behavior is the six declared adaptations (single asset, calendar months plus close-to-close returns, mirrored monthly cadence, trailing-quintile gate, next-open fills plus fixed sizing plus structural warmup plus house costs, long-flat mapping); the MAX definition, the avoid-extreme-MAX direction, and the no-stop stance are source-faithful. This record is therefore never evidence that the paper's equity study passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: calendar-month formation / close-to-close MAX / 36-month trailing pool / 29th-order-statistic cutoff / strict-inequality tie-to-flat / month-end-close decision / next-open fills / single-position long-flat / `1d` BTCUSDT are frozen.

- F1 — Sign relevance: an inverted twin (long iff `MAX(M) ≥ q80(M)`, flat otherwise, same grid and fills) must not improve net expectancy; fail ⇒ the avoidance sign points the wrong way on this tape and the lottery read inverts.
- F2 — Spike-vs-level relevance: a total-return twin (long iff the formation month's total close-to-close return sits below its own trailing-36-month 80th percentile, same grid and fills) must not improve net expectancy; fail ⇒ the single-spike statistic adds nothing over a plain return level and the paper's core construction is doing no work here.
- F3 — Formation relevance: a 3-month-MAX twin (`MAX` over the prior three calendar months' daily returns, same trailing-rank gate and fills) must not improve net expectancy; fail ⇒ the one-month formation specificity is doing no work on this tape.
- F4 — Selectivity relevance: buy-and-hold over the same sample must not improve net expectancy; fail ⇒ sitting out top-quintile spike months costs more in missed drift than it saves in avoided exposure — or the record's selectivity pin is doing unacknowledged work.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid month-end `1d` bar closes; fills at next-month first-bar opens; no venue-specific read). The arithmetic ports across perpetual venues without structural change (no volume, corporate-action, or calendar adjustment exists to recheck). No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. Extension to other house-universe assets, month definitions, return definitions, windows, cutoffs, or timeframes would be a different, unpinned claim.

## Limitations

- Single-asset port: the paper's evidence is an equity cross-section; BTCUSDT spike-month behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Mechanism mismatch: whatever retail lottery-demand clientele sits behind the equity result has no established crypto analogue (24/7 global holder base, different spike rhythms, perpetual-funding holders) — the port bets on regime persistence, not on a verified crypto mechanism.
- Rank-rigidity: the trailing-36-month pool adapts slowly — a volatility-regime break reprices the cutoff only as old formation months roll off; a permanently calmer tape goes nearly always-long, a permanently wilder tape nearly always-flat, both by construction.
- Month-definition rigidity: a spike arriving across a month boundary is attributed to whole months; a first-of-month gap against the fresh regime is taken at the post-move open, never at the edge.
- Warmup cost: everything before the first computable-target month-end close (2020-08-31) is flat by record rule, so the 2017–2020 tape is deliberately untraded — pinned, not recovered.

## Implementation status

not-implemented. No Hummingbot controller/executor has been written for this record; the Execution assumptions section names the exact pinned engine path (package `20260920`, VERSION `dev-2.17.0`, month-end-close decision on completed `1d` bars, next-month-first-open market fills, single-asset 100%-equity 1× long-or-flat) that a future implementation must target, with representative event-level Qlib/Hummingbot parity required before any mass screening.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. PASS means the declared derived strategy is causally expressible under the pinned Hummingbot model — not profitable, not Qlib-paritied, not source-equivalent, not live-tradable.

## Related Wiki records

None.

## Sources

- Bali, Turan G., Cakici, Nusret, and Whitelaw, Robert F. (2011). Maxing Out: Stocks as Lotteries and the Cross-Section of Expected Returns. Journal of Financial Economics 99, 427–446. https://doi.org/10.1016/j.jfineco.2010.08.014 (Crossref-verified 2026-10-14; NBER trail https://www.nber.org/papers/w14804; SSRN trail https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1354512; author PDF https://pages.stern.nyu.edu/~rwhitela/papers/max%20jfe11.pdf; NBER w14804 fetched live 2026-10-14, 360,804-byte 50-page PDF, SHA-256 `8039f722…1826612`, read in full locally)
