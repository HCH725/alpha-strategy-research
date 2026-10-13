---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Gatev-Goetzmann-Rouwenhorst 2006 distance-method pairs mean-reversion two-sided on BTCUSDT+ETHUSDT 1d bars
created: 2026-10-14
updated: 2026-10-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2006-02
sources:
  - https://repec.som.yale.edu/icfpub/publications/2573.pdf
  - https://doi.org/10.1093/rfs/hhj020
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Gatev-Goetzmann-Rouwenhorst 2006 distance-method pairs mean-reversion two-sided on BTCUSDT+ETHUSDT 1d bars

## Provenance

Primary source read end to end (Yale ICF author-hosted working-paper version, fetched over HTTPS during this cycle):

- Canonical file: https://repec.som.yale.edu/icfpub/publications/2573.pdf (Yale ICF Working Paper, first draft June 1998, this version February 2006; 379,971 bytes, SHA-256 `ab3cdc1a…`, extracted text 476 lines, all read). Published as Gatev–Goetzmann–Rouwenhorst, "Pairs Trading: Performance of a Relative-Value Arbitrage Rule," Review of Financial Studies 19(3), 797–827 (2006); bibliographic identity verified against Crossref this cycle (DOI `10.1093/rfs/hhj020`, journal-article, vol 19, issue 3, pages 797–827).
- Rule literals verified verbatim in §2.1–§2.3: twelve-month formation period; screen out stocks with any no-trade day; cumulative total-return (dividends reinvested) normalized price index per stock; partner chosen by minimum sum of squared deviations between the two normalized price series; trade the top 5 and top 20 smallest-distance pairs (plus pairs 101–120 as contrast); trading begins the day after the formation period ends over the next six-month trading period; open a $1-short-higher-priced / $1-long-lower-priced position when normalized prices diverge by more than two historical standard deviations estimated in formation; unwind at the next crossing of the prices; mark at the last trading day if no crossing; close at the delisting return (or last available price) on delisting; re-opening after convergence allowed (2.02/1.96 round-trips per pair per period, Table 2 Panel A); new pairs initiated every month with six overlapping cohorts averaged à la Jegadeesh–Titman 1993 (§2.3).
- Timing literal: §3.1 Panel A opens/closes at the end of the divergence/convergence day; Panel B delays both legs one day (the conservative bid-ask-bounce-robust implementation). This record pins the Panel-B analog only (next-open fills).
- Performance numbers below are source-reported with table provenance; none is claimed for crypto and none is reproduced here.

Licence and rights: the author-hosted working paper is a public research publication. This record cites and normalizes the rule and reproduces no source block beyond single-line rule literals quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly seven: (1) fixed single pair BTCUSDT+ETHUSDT perpetuals (the paper matches top-20 pairs by exhaustive cross-sectional minimum-distance search — no pair search exists here; the pair is fixed by economic construction as close crypto substitutes, mirroring the paper's §3.9 large-liquid robustness screen of trade-every-day stocks); (2) 365 completed `1d` closes per 12 calendar months and 182-bar trading windows (crypto trades 24/7 — the paper's ~252 trading-day formation maps to 365 calendar bars; frozen per-epoch σ); (3) sequential non-overlapping single-sleeve epochs instead of monthly-reformed six-overlapping-cohort portfolios (§2.3 averaging not claimed); (4) Panel-B-analog next-open fills on completed-bar decisions; (5) fixed research notional 50/50 legs at 1× isolated with house costs, and no house DCA overlay (safety-order adds would break the paper's dollar-neutral $1/$1 shape — explicitly excluded); (6) normalized indices from closes only (no dividends exist in crypto; the funding analog is NOT folded into the index — flagged, never zero-claimed); (7) delisting analog closes both legs at the last available price. Trigger `2σ`, cross-exit, window-end unwind, both-leg direction, re-entry permission, and every no-stop/no-target/no-trailing exclusion are source-native and unmodified.

Pre-write dedup (2026-10-14): working-tree case-insensitive searches for `pairs.trading`, `Gatev`, `Goetzmann`, `Rouwenhorst`, `cointegrat`, `distance-method`, `relative-value`, and `statistical arbitrage` return zero strategy records using any cross-asset spread construction — the sole `cointegrated-pairs` hit is a wiki cross-link line inside an unrelated ATR-momentum record, not a strategy. Open `research/*` PRs are only #48 (Larry Williams 3-EMA streak long), #49 (Gaussian StochRSI breakout long), #63 (SuperTrend flip long), #89 (Chandelier dual-stop long), #92 (SSL reversal two-sided) — all single-asset indicators. Five-axis distinction: mechanism differs (two-asset relative-value spread convergence — no pool record trades any cross-asset spread; the pool's Lehmann/Jegadeesh records are single-asset prior-return contrarians, JT/TSMOM/Novy-Marx/Cooper-state/George-Hwang/LS-lifecycle/FIP records are single-asset momentum sorts, BLL/Donchian/Bollinger records are single-asset level bands), signal construction differs (formation-σ-normalized cross-asset divergence `|D|>2σ` versus own-price level, band, or momentum sign), exits differ (convergence cross plus window-end time unwind versus signal flips or reversal-only books), source identity differs (GGR 2006 RFS 19(3):797–827 versus all other families), and direction handling differs (dollar-neutral long-short pair book where either leg may be the short versus long-flat or single-asset two-sided books).

## Economic mechanism

### Source-reported

Relative pricing / Law of One Price for close substitutes (§1.3): two securities that are close substitutes should sell for the same price. Pairs are matched as minimum-distance neighbors in normalized price space, so a >2σ divergence is treated as temporary mis-pricing of near-identical payoffs; shorting the higher-priced leg and buying the lower-priced leg harvests convergence. Bootstrap evidence (§3.6, Table 6: simulated random-pair excess returns slightly negative over 200 replications) shows the effect differs from previously documented Lehmann/Jegadeesh short-term reversal; the authors link profits to compensation for enforcing the Law of One Price (§3.8, §4).

### Research interpretation

Cross-asset spread-convergence book, dollar-neutral, two-sided. Unlike the pool's single-asset contrarians (Lehmann weekly / Jegadeesh monthly — which fade own past return), nothing here reads own past return: the book is flat when BTC and ETH move together no matter how far either has run, and fires only on their relative distance. Unlike momentum records it never holds a trend — every open position unwinds at the next price cross or dies at the window end (average open 3.76 months, Table 2). The bet is on 24/7 crypto majors sharing a common non-stationary drift with stationary relative noise at the ~months scale, under a fixed 2σ formation-σ trigger — not on any level, band, calendar, volume, or volatility-regime leg.

## Signal

Exact rule as pinned (365-bar formation, 182-bar window, trigger 2.0, strict edges — any other value is a different, unpinned rule):

- Epochs (deterministic, sequential, non-overlapping): epoch 0 formation = the 365 completed `1d` closes 2017-08-17..2018-08-16, window = the 182 bars 2018-08-17..2019-02-14; epoch `k+1` starts 182 bars after epoch `k` started (formation = the 365 completed closes immediately preceding its window, σ frozen per epoch). Pre-window bars flat by record rule.
- Normalization: `N_BTC[t] = close_BTC[t]/close_BTC[first formation bar]`, `N_ETH[t]` likewise (closes only — §2.1 total-return shape minus the dividend leg, declared above).
- Spread and σ: `D[t] = N_BTC[t]-N_ETH[t]`; `σ = sample-std(D)` over the epoch's 365 formation bars. If `σ == 0`, no entries that epoch (fenced edge, disclosed).
- Entry trigger (completed-bar decision, Panel-B analog): while flat and inside the window, if `|D[t]| > 2σ` on completed bar `t` → at the next bar open: `D[t] > +2σ` shorts BTC / longs ETH, `D[t] < -2σ` longs BTC / shorts ETH (the paper's "$1 short higher-priced, $1 long lower-priced" mapped onto fixed 50/50-notional legs).
- Exit: at the next crossing — first completed bar `t` with `sign(D[t]) != sign(D[signal bar])` (strict zero-cross of the spread) → unwind both legs at the next bar open. If no cross before the window ends → unwind both legs at the first open after the window's last bar (time unwind, mirroring the paper's last-day mark).
- Re-entry: after a flat state, a new `|D|>2σ` signal inside the same window re-opens (mirrors Table 2's ~2 round-trips per period). At most one open pair position at any time; no pyramiding, no adds, no partials.
- Missing-bar rule: if either symbol's bar is missing/unformed at a decision point, no new entry that bar; an open position is held (never force-closed on data absence).
- Risk legs (pinned absences, not invented): the paper ships no stop-loss, no take-profit, no trailing, no cooldown — none exists here either (declared explicitly, never hidden). The sole position-closing paths are the spread cross and the window-end unwind.

## Required data

- Completed `1d` bars of BTCUSDT and ETHUSDT on the same venue grid: `close` (normalization, spread, σ, cross detection), `open` (fills only). No funding, OI, mark/index price, order-book, on-chain, sentiment, macro, calendar, or cross-venue state is read by any order-gating line.
- Two synchronized daily feeds aligned by bar openTime; the decision timestamp is the completed daily close when both bars are printed. Single decision timeframe `1d`.
- Warmup: 365 completed closes per epoch before any trigger in its window (structural leg, not a researcher choice of convenience); the σ transient needs no extra seeding beyond the formation itself. No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT + ETHUSDT Binance perpetuals under fixed research notional (declared port; the source venue is 1962–2002 US equities — no cross-venue equivalence claimed beyond the same two-leg dollar-neutral shape).
- Order timing (predeclared Panel-B analog): completed-bar decision with next-bar-open execution for entries and unwinds, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). Both legs are ordered at the same next open as one pair step — no sequencing edge exists since both legs fill at printed opens. No maker-touch, queue, or intrabar-path-dependent fill.
- Sizing/capital/costs: fixed epoch notional split 50/50 across the two legs at 1× isolated (the paper's self-financing $1/$1 shape at research scale); pinned house fee assumptions apply; historical funding accounting on the pinned route is unverified — funding is a flagged unsupported economic term and this record reports no realized funding P&L of any kind (no hypothetical zero funding is claimed as realized). The house 6%+6%+6% DCA overlay is explicitly excluded (adds would break dollar-neutrality).
- Concurrency: single sleeve, at most one pair position (one long leg + one short leg) at any time; no overlapping cohorts, no shared-portfolio contention beyond the fixed two-leg notional; no cooldown specified — explicitly none, not invented. The short leg requires margin-short permission, realistic on the pinned perpetual venue.

## Evidence

### Source-reported

- Table 1 Panel A (no wait): top-20 fully-invested average excess return 1.44%/month (`t = 11.56`); committed capital 0.81%/month; 474 months, July 1963–December 2002.
- Table 1 Panel B (1-day wait, the pinned analog): top-20 fully-invested 0.90%/month (`t = 9.29`); committed capital 0.52%/month.
- Table 2 Panel A: average trigger deviation 4.76% (top 5) / 5.28% (top 20); 19.30 of top-20 pairs open per period; 1.96 round-trips per pair; average open duration 3.76 months.
- §1.2 holdout: post-1998 four-year sample, top-20 fully-invested 10.4%/annum (σ 3.8%, Newey-West `t = 4.82`) with the strategy frozen since the 1999 draft — disclosed as the paper's own anti-data-snooping evidence, not this record's claim.
- §3.6/Table 6: 200-replication bootstrap on same-decile random pairs earns slightly negative excess returns — the pairs effect is not simple short-term mean reversion.
- §3.9/Table 9: profits survive large-liquid-only screens and simulated high-volume short recalls — cited as source robustness context, not ported behavior.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Committed-capital drag, admitted plainly: epochs (or the single pair) with no `>2σ` divergence earn zero on committed notional — Table 1's committed returns run ~40% below fully-invested; a quiet-cointegration epoch is the coded flat trade, disclosed, not smoothed.
2. Single-pair concentration, admitted plainly: the paper diversifies across 20 pairs (portfolio σ falls with pair count, Table 1); this record holds one pair, so spread-widening-without-convergence is held in full to the window-end unwind — adverse drift to the last bar is the coded trade.
3. Opens-too-soon, admitted plainly: the paper's own §3.3 warns the formation-minimum σ likely underestimates true σ, opening some pairs before spreads can cover costs even on convergence — the 2σ literal is kept unmodified; raising it would be a different, unpinned rule.
4. End-of-window forced unwind, admitted plainly: §3.3 warns late-window divergences cannot earn back round-trip costs before the forced mark — late signals still fire and still unwind at the window end here; suppressing them would be invention.
5. Funding unmodeled, admitted plainly: the short perpetual leg accrues funding the record never accounts — no funding-dependent leg is gated, no realized funding number of any kind is reported, and zero is never presented as realized.
6. Index without carry, admitted plainly: normalization uses closes only — the paper's reinvested-dividend leg has no crypto analog folded in; the spread is a pure price-space construction by declared derivation.
7. Cohort economics not claimed, admitted plainly: the paper's monthly overlapping six-cohort averaging (§2.3) is absent — single sequential sleeves have lumpier epoch economics; this record is never evidence for the paper's smoothed monthly series.
8. Calendar mapping fenced: 365/182 calendar bars stand in for ~252/~126 trading days by declared 24/7 mapping; a different bar-count mapping would be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: fixed BTC+ETH pair / 365-bar formation / 182-bar window / trigger 2.0 / strict cross exit / window-end unwind / next-open fills / 50-50 1× legs / no-stop-no-target-no-trailing are frozen.

- F1 — Pair relevance: replacing the cross-asset spread with a single-asset BTC-only 2σ band-revert (same 365-bar formation σ, same window, same next-open fills, long-flat) must not improve net expectancy; fail ⇒ the cross-asset pair adds nothing over own-price mean reversion.
- F2 — Threshold relevance: loosening the trigger to 1σ (same everything else) must not improve net expectancy; fail ⇒ the paper's 2σ choice adds nothing and the record is merely trading noise sooner (engages the paper's own §3.3 too-soon caveat).
- F3 — Exit relevance: replacing the spread-cross exit with a fixed 63-bar time exit (same entries, same window-end unwind) must not improve net expectancy; fail ⇒ convergence-timed exits add nothing over elapsed-time exits.

## Crypto portability

Pinned to BTCUSDT+ETHUSDT Binance perpetuals at 1× isolated under fixed research notional (declared port of a US-equities source context). The normalized-spread arithmetic ports across same-grid daily venues without structural change; both legs are explicit, so a spot-only deployment expresses only the long half while any short half stays venue-gated (short permission unused, never silently converted). No funding-dependent leg, no stablecoin-specific assumption, no session template, no cross-venue state. The 24/7 crypto market prints a bar every calendar day, so formation/window bar counts need no holiday approximation. Extension to other pairs, universes, or timeframes would be a different, unpinned claim.

## Limitations

- Derived pair and calendar mapping: the paper selects top-20 pairs from an exhaustive minimum-distance search over liquid US equities and trades overlapping monthly cohorts; this record fixes one crypto pair and sequential single sleeves. Epoch economics of the two framings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source configuration's performance.
- No source cost declaration ports: round-trip cost discussion in §3.3 is US-equities spread reasoning — derived evaluation must carry the full house fee load plus flagged (unmodeled) funding, and this record reports no net performance of any kind.
- Window-end unwind exposure: a spread that diverges late and never crosses is closed at the window boundary at whatever mark prevails — forced realization of relative drift is the coded trade, disclosed, not smoothed.
- Single-pair idiosyncrasy: protocol, listing, or microstructure shocks to either leg move the spread without any cross-sectional diversification — concentration is the coded trade, disclosed, not hedged.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Yale ICF author-hosted working-paper version (Feb 2006; RFS 19(3):797–827): https://repec.som.yale.edu/icfpub/publications/2573.pdf
- Journal record (Crossref-verified DOI `10.1093/rfs/hhj020`): https://doi.org/10.1093/rfs/hhj020
