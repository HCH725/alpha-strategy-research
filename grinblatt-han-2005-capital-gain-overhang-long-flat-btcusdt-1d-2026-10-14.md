---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Grinblatt-Han 2005 capital-gain-overhang gain-domain-hold long-flat on BTCUSDT 1d bars
created: 2026-10-14
updated: 2026-10-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2005-11-01
sources:
  - https://doi.org/10.1016/j.jfineco.2004.10.006
  - https://www.sciencedirect.com/science/article/abs/pii/S0304405X05000747
  - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=288466
  - http://depot.som.yale.edu/icf/papers/fileuploads/2533/original/00-71.pdf
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Grinblatt-Han 2005 capital-gain-overhang gain-domain-hold long-flat on BTCUSDT 1d bars

## Provenance

Primary source identity verified end to end (Crossref metadata hand-fetched plus the authors' own working-paper PDF read in full locally, 2026-10-14):

- Grinblatt, Mark and Han, Bing, `Prospect Theory, Mental Accounting, and Momentum` — Journal of Financial Economics, vol. 78, 311–339 (November 2005). DOI `10.1016/j.jfineco.2004.10.006`. Crossref record pins title `Prospect theory, mental accounting, and momentum`, container `Journal of Financial Economics`, volume `78`, pages `311-339`, print publication November 2005 (836 citing works at fetch time; SSRN `288466` is the working-paper trail).
- Actually-read text (disclosed as the full working-paper version, not the typeset journal): Yale ICF Working Paper `00-71` (first version November 2000, current version August 2004), fetched live 2026-10-14 as a 346,145-byte 38-page PDF (SHA-256 `cd727c67…1418854`), converted locally and read in full (`pypdf` extraction, 87,659 characters).
- Pinned headline spec (working-paper text, read verbatim modulo PDF ligature noise): the aggregate reference price `Rt` follows equation (1) `Rt+1 = VtPt + (1 − Vt)Rt` with the updating weight `Vt` tied to the stock's turnover ratio; the empirical reference price is the turnover-weighted cost basis `R(t−1) = (1/k) Σ(n=1..260) [V(t−1−n) Π(τ=1..n−1)(1 − V(t−1−n+τ))] P(t−1−n)` with `k` rescaling weights to sum to one; estimation is truncated at five years (260 weeks) because `distant market prices have little influence on the reference price`; the adopted regressor is the capital-gains overhang `g = (P(t−2) − R(t−1))/P(t−2)`; the paper's sample is weekly returns, turnover (weekly volume over shares outstanding), and capitalization for all ordinary common shares on NYSE and AMEX from July 1962 to December 1996.
- Pinned headline findings (working-paper text, qualitative only — no coefficient, t-statistic, or return number is adopted anywhere in this record): `the capital gains variable thus defined predicts future returns, even after controlling for the effect of past returns, but the reverse is rarely true`; `Past returns have no predictability for the cross-section of returns once this variable is controlled for`; high-overhang stocks `under-react most` to news while no-overhang stocks show no significant drift; the January/December double-sort subsamples carry a December tax-loss-selling seasonal that is fenced off, never carried (see Negative evidence 5).
- Licence and rights: the paper is a published journal article plus an openly hosted author working paper — this record cites and normalizes the rule (short phrases and the two definitional equations only) and reproduces no figures, tables, or extended prose.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the paper's turnover-weighted cost-basis reference price ported to one crypto asset as a weekly gain-domain long-or-flat hold — not a lossless reproduction of the paper's equity cross-sectional study. Researcher-declared adaptations are exactly six: (1) single-asset BTCUSDT Binance venue (every cross-sectional sort, quintile breakpoint, Fama-MacBeth coefficient, t-statistic, and momentum-profit number is fenced off, never carried — see Negative evidence 1–2); (2) calendar-week sampling on the 24/7 tape with a fixed 21M turnover denominator (the paper's shares-outstanding denominator does not exist for BTC — see Signal and Negative evidence 4); (3) the paper's one-week timing skip mirrored exactly (signal uses data through week w−1 at a week-w close decision — see Signal); (4) the zero threshold as the gain/loss-domain boundary (the paper never trades a threshold rule — see Negative evidence 3); (5) Sunday-close decision with next-bar (Monday) open fills, fixed 100%-equity 1× sizing, and a 260-week conventional warmup (the paper ships no order timing, sizing, or costs — see Execution assumptions); (6) long-flat direction mapping only (the paper's long-short decile framing carries no short leg here — no short is enabled, explicitly none). The turnover-weighted reference-price construction, the overhang definition, the gain-domain direction, and the no-stop time-hold stance are source-faithful.

Pre-write dedup (2026-10-14): working-tree case-insensitive searches for `grinblatt`, `han-2005`, `overhang`, `prospect.theor`, `reference.price`, `capital.gain`, `turnover.weight` return no strategy record (the sole `disposition` prose hit is a one-word behavioral aside inside the Gao-Han-Li-Zhou first-to-last-halfhour intraday record — a different paper, mechanism, and 30m grid; the `cost.basis` prose hits are exact-numbers-rule boilerplate `no ... cost basis`, never a cost-basis reference price). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak), #49 (Gaussian channel StochRSI breakout), #63 (SuperTrend ATR-flip), #89 (Chandelier Exit stop-flip), #92 (SSL channel reversal) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `gervais-kaniel-mingelgrin-high-volume-premium-long-flat-btcusdt-1d-2026-10-14.md` trades a volume-shock next-day premium with no reference price; `nvi-255ema-regime-long-flat-btcusdt-1d-2026-10-13.md` and `obv-ema-crossover-trend-two-sided-btcusdt-1d-2026-10-10.md` accumulate signed volume against a long moving average with no cost-basis weighting; `jegadeesh-titman-6m-6m-momentum-long-flat-btcusdt-1d-2026-10-13.md`, `liu-tsyvinski-1w-momentum-long-flat-btcusdt-1d-2026-10-13.md`, and `tsmom-12m-sign-monthly-long-btcusdt-1d-2026-10-10.md` condition on past-return sign or formation returns (the paper's headline is that overhang subsumes past returns — see Negative evidence 7); `monday-drift-weekly-calendar-hold-btcusdt-1h-2026-10-06.md` and `turn-of-month-4day-hold-long-btcusdt-1d-2026-10-10.md` are pure calendar partitions with no price, volume, or reference input. Five-axis distinction: no pool record and no open PR conditions exposure on a turnover-weighted cost-basis reference price versus the current price.

## Economic mechanism

### Source-reported

Disposition-driven underreaction, not risk compensation: prospect-theory / mental-accounting investors measure gains and losses against the aggregate cost basis (reference price); holders sell winners too soon and ride losers too long, so high-overhang (aggregate-gain) stocks face disposition selling pressure that leaves good news under-incorporated — and high-overhang stocks `under-react most` to subsequent news. (All mechanism framing fenced to the paper's equity sample, never adopted as a crypto claim here.)

### Research interpretation

Cost-basis-regime drift-capture, long-only, weekly cadence. Unlike return-conditioned momentum systems there is no formation return and no winner/loser ranking: the position exists if and only if the tape trades above its own turnover-weighted cost basis (aggregate-gain domain). Unlike volume oscillators (NVI/OBV/PVO/Klinger/CMF) volume never enters as a level, shock, or cross — it enters only as the weighting kernel of the reference price, so a volume spike with no price displacement moves the reference, never the trigger directly. Unlike calendar holds there is no date input anywhere. The bet, as derived, is purely that the documented gain-domain/underreaction partition ports to BTCUSDT weekly bars, never on a level, band, return-sign, weekday, or funding anchor — and the position sits through any within-regime slide with no guardrail.

## Signal

Exact rule as pinned (weekly sampling; Sunday-close decision; Monday-open fills; long-flat — any other week definition, denominator, window, skip, or threshold is a different, unpinned rule):

- Bar grid: completed `1d` bars of BTCUSDT only. Weeks are pinned calendar weeks Monday 00:00:00 UTC through Sunday 23:59:59 UTC (matches the venue's own weekly-bar grid, verified at write time). One evaluation per week, in week order.
- Weekly inputs (pinned): `P(w)` = close of the week's Sunday daily bar; `Vol(w)` = sum of base-asset volume over the week's seven daily bars (a partial first history week sums whatever daily bars exist — deterministic as printed).
- Turnover analog (pinned declared derivation): `V(w) = Vol(w) / 21,000,000`. The paper divides by shares outstanding, which BTC lacks; the fixed terminal-supply denominator is the declared port. Venue-checked admissibility: over the venue's full 479-week history (August 2017–October 2026, hand-fetched at write time) the maximum weekly base volume is 3,775,888.9 BTC = 0.1798 × 21M, so `0 < V(w) < 1` holds on every printed week and every `(1 − V)` weight factor stays positive — if a future week ever printed `V ≥ 1` the weights would be invalid and this pin would be void, disclosed (see Limitations).
- Reference price (pinned, paper's equation with the declared `V`): `R(w) = (1/k) Σ(n=1..260) [V(w−1−n) Π(τ=1..n−1)(1 − V(w−1−n+τ))] P(w−1−n)`, with `k` the sum of the 260 bracket weights (rescale-to-one, exactly as the paper). This is the paper's five-year/260-observation truncation, ported from 260 weeks of equity turnover to 260 weeks of the declared turnover analog.
- Overhang with the paper's one-week skip mirrored (pinned): `g(w) = (P(w−1) − R(w)) / P(w−1)` — at the week-`w` Sunday-close decision only data through week `w−1` is touched, exactly as the paper's `P(t−2)/R(t−1)` timing touches nothing newer than `t−2` relative to its week-`t` regression.
- Position target (pinned): the target for week `w+1` (Monday through Sunday) is long iff `g(w) > 0` (aggregate-gain domain), else flat; the exact-zero tie maps to flat (measure-zero tie rule, pinned). Zero is the prospect-theory gain/loss-domain boundary — the paper never trades a threshold rule, so the threshold is researcher-pinned, never implied (see Negative evidence 3).
- Orders (pinned): at most one order event per week, placed for the next week's Monday bar open (next-open fill after the Sunday decision bar — the declared causal port; the paper ships no fill convention): flat→long target buys 100% equity at Monday's open; long→flat target closes all at Monday's open; unchanged target places nothing. No intrabar evaluation, no intrabar orders, no adds, no partials. Decisions on distinct Sundays fill on distinct Mondays — no same-bar dual-fire exists to sequence.
- Risk legs (pinned absence, not invented): the paper ships no stop/target/trailing concept for the overhang partition — the sole position-closing path is the regime exit to flat at a Sunday close (filled Monday open). The derived posture is explicitly no stop, no target, no trailing, no opposite-signal exit, no calendar extension; a fully ridden within-regime slide is absorbed exactly as printed by construction.
- Direction: long-or-flat, derived-and-declared (the futures venue is still pinned as the research market under the house overlay with the short permission simply unused, and a spot-only deployment expresses the identical event set).

## Required data

- Completed `1d` bars of BTCUSDT only: `close` (weekly `P`), base-asset `volume` (weekly `Vol`), `open` as fill price (no `high`, no `low`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, supply-feed, sentiment, macro, session-template, or cross-venue state gates any order). No multi-symbol, multi-timeframe, or external-feed dependency of any kind — the 21M denominator is a record constant, not a feed.
- Single decision grid: one evaluation per week at the Sunday bar's close; fills land on the next Monday bar's open. All inputs are completed-bar values — no provisional intrabar value is ever used; the one-week skip means the freshest touched data is always a full week old.
- Warmup: flat until the Sunday close at which the first computable `g` exists (the first computable `g`, needing 260 reference weeks plus the one-week skip) — structural, not conventional: on this venue that is the Sunday close of 2022-08-21, so the first position week is 2022-08-22..28. No repainting, no negative shift, no future reference, no full-sample normalization (`M`-style rolling maxima are not used; every `V` is a same-week constant-denominator ratio).

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared port of the paper's NYSE/AMEX universe; no cross-venue equivalence claimed).
- Order timing (declared causal port; the paper ships no executable timing): Sunday-bar-close decision with next-bar (Monday) open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill is claimed. At most one order exists per week boundary, so there is no same-bar dual-fire to sequence.
- Cash leg: flat earns nothing by record rule. No T-bill, stablecoin-lending, funding-rebate, or synthetic yield is substituted; the paper's cost-free accounting accrues no cash yield to either regime.
- Sizing/capital/costs: fixed 100%-equity single position, no adds, no leverage (1×, no margin concept), no compounding concept beyond equity. The paper reports cost-free sample statistics, so derived evaluation must carry the explicit house overlay (pinned house fees plus historical funding treatment; no hypothetical zero funding claimed — long weeks carry realized funding, flat weeks carry none, and the form holds genuine flat stretches so it is never an always-in-position funding accumulator). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one long position at any time; week regimes are disjoint by calendar construction, so overlapping entries are structurally impossible (no ignore-rule needed beyond the single-position book); after any Sunday-close exit the next Sunday decision fires on schedule (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The unused short permission requires no margin-short modeling. Safety orders: explicitly none.

## Evidence

### Source-reported

The paper ships every adopted headline fact quoted in Provenance: the turnover-updated reference-price equation, the 260-observation truncation with rescale-to-one, the `(P−R)/P` overhang definition with its skipped-week timing, the weekly NYSE/AMEX July-1962–December-1996 sample, and the gain-predicts-returns / past-returns-lose-power headline. It ships zero adopted performance numbers for this record: every coefficient, t-statistic, and return spread in the paper describes its equity cross-section, never a single-asset BTCUSDT derivative — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Cross-section fenced: every quintile sort, Fama-MacBeth coefficient, t-statistic, momentum-profit spread, and independence test in the paper belongs to its 1962–1996 equity cross-section — none transfers to a single-asset crypto time-series rule, and none is adopted.
2. Number silence fenced: no coefficient, t-statistic, return spread, sample-window moment, or percentile cut from any paper table or figure is adopted anywhere — figures are omitted by rule, and any dispute over exact magnitudes is decided against this record, never patched by inference.
3. Threshold pin disclosed: the paper sorts and regresses but never trades a `g > 0` time-series rule — the zero threshold is researcher-pinned from the prospect-theory gain/loss-domain boundary, never a paper convention. Any other threshold would be a different, unpinned rule.
4. Denominator derivation disclosed: the paper's turnover divides by shares outstanding; this record divides weekly base volume by the constant 21M. The paper's own Table-4 robustness (an average-turnover reference price still carries a significant gain coefficient) is cited as comfort only — never as validation of this denominator, never as a claim the paper blesses it.
5. Seasonal subsample fenced: the paper's double sorts show December tax-loss-selling / January seasonal behavior inside high/low-overhang legs — the derived rule holds straight through Decembers and Januarys with no seasonal veto, disclosed, not recovered.
6. Fully exposed inside the regime: once in gain domain, the position rides the entire adverse excursion with no guardrail — a −20% week inside a positive-`g` hold is held to the next Sunday close by construction. This is the coded trade, disclosed, not a tunable parameter here.
7. Momentum-family overlap disclosed: the paper's headline is that overhang subsumes past returns — so this record will often agree with 6m/12m momentum signs by construction (both load on sustained drift), but the trigger (price versus turnover-weighted cost basis, unconditional on any formation return) differs materially from every return-sign rule in the pool; agreement is arithmetic, not mechanism duplication. Replacing the reference with a plain moving average would be a different, unpinned rule (see F2).
8. Derivation boundary fenced: the only non-paper behavior is the six declared adaptations (single asset, calendar weeks plus 21M denominator, mirrored one-week skip, zero threshold, next-open fills plus fixed sizing plus structural warmup plus house costs, long-flat mapping); the turnover-weighted reference construction, the overhang definition, the gain-domain direction, and the no-stop stance are source-faithful. This record is therefore never evidence that the paper's equity study passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 260-week turnover-weighted reference / 21M denominator / one-week skip / zero threshold / Sunday-close decision / Monday-open fills / single-position long-flat / `1d` BTCUSDT are frozen.

- F1 — Sign relevance: an inverted twin (long iff `g ≤ 0`, flat otherwise, same grid and fills) must not improve net expectancy; fail ⇒ the gain-domain sign points the wrong way on this tape and the disposition read inverts.
- F2 — Weighting relevance: a plain-mean twin (long iff `P(w−1)` exceeds the 260-week simple mean of Sunday closes, same skip and fills) must not improve net expectancy; fail ⇒ the turnover-weighting kernel adds nothing over an unweighted long-run mean and the paper's core construction is doing no work here.
- F3 — Skip relevance: a no-skip twin (Sunday decision using week-`w` data: `g* = (P(w) − R*(w))/P(w)` with the reference shifted one week newer, same fills) must not improve net expectancy; fail ⇒ the mirrored microstructure skip is pure lag on this tape.
- F4 — Selectivity relevance: buy-and-hold over the same sample must not improve net expectancy; fail ⇒ sitting out loss-domain weeks costs more in missed drift than it saves in avoided exposure — or the record's selectivity pin is doing unacknowledged work.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid Sunday `1d` bar closes; fills at Monday opens; no venue-specific read). The arithmetic ports across perpetual venues without structural change provided the venue's weekly volume history keeps `V < 1` on the 21M denominator (checked on Binance at write time — recheck, never assume, elsewhere). No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. Extension to other house-universe assets, week definitions, denominators, windows, or timeframes would be a different, unpinned claim.

## Limitations

- Single-asset port: the paper's evidence is an equity cross-section; BTCUSDT gain-domain behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Mechanism mismatch: whatever disposition-selling clientele sits behind the equity result has no established crypto analogue (24/7 global holder base, no certificates, different turnover rhythms) — the port bets on regime persistence, not on a verified crypto mechanism.
- Denominator rigidity: 21M understates early-tape turnover versus then-circulating supply and overstates nothing later — a fixed, disclosed approximation, not the paper's outstanding-shares normalization.
- Week-definition rigidity: drift arriving across a Sunday boundary is attributed to whole weeks; a Monday-open gap against the fresh regime is taken at the post-move open, never at the edge.
- Warmup cost: everything before the first computable-`g` Sunday close (2022-08-21) is flat by record rule, so the 2017–2022 tape is deliberately untraded — pinned, not recovered.
- Ceiling void: a future week printing `V ≥ 1` voids this pin's weight validity (see Signal) — monitored, not modeled.

## Implementation status

not-implemented. No Hummingbot controller/executor has been written for this record; the Execution assumptions section names the exact pinned engine path (package `20260920`, VERSION `dev-2.17.0`, Sunday-close decision on completed `1d` bars, Monday-open market fills, single-asset 100%-equity 1× long-or-flat) that a future implementation must target, with representative event-level Qlib/Hummingbot parity required before any mass screening.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. PASS means the declared derived strategy is causally expressible under the pinned Hummingbot model — not profitable, not Qlib-paritied, not source-equivalent, not live-tradable.

## Related Wiki records

None.

## Sources

- Grinblatt, Mark and Han, Bing (2005). Prospect Theory, Mental Accounting, and Momentum. Journal of Financial Economics 78, 311–339. https://doi.org/10.1016/j.jfineco.2004.10.006 (Crossref-verified 2026-10-14; publisher landing https://www.sciencedirect.com/science/article/abs/pii/S0304405X05000747; SSRN trail https://papers.ssrn.com/sol3/papers.cfm?abstract_id=288466; author working paper Yale ICF 00-71 http://depot.som.yale.edu/icf/papers/fileuploads/2533/original/00-71.pdf fetched live 2026-10-14, 346,145-byte 38-page PDF, SHA-256 `cd727c67…1418854`, read in full locally)
