---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Da-Gurun-Warachka 2014 FIP continuous-information momentum long-flat on BTCUSDT 1d bars
created: 2026-10-14
updated: 2026-10-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2014-07-01
sources:
  - https://academicweb.nd.edu/~zda/Frog.pdf
  - https://doi.org/10.1093/rfs/hhu003
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Da-Gurun-Warachka 2014 FIP continuous-information momentum long-flat on BTCUSDT 1d bars

## Provenance

Primary source identity verified end to end (Crossref metadata hand-fetched plus the full author-hosted text read locally, 2026-10-14):

- Zhi Da, Umit G. Gurun, Mitch Warachka, `Frog in the Pan: Continuous Information and Momentum` — Review of Financial Studies, vol. 27, issue 7, 2171–2218 (July 2014). DOI `10.1093/rfs/hhu003` (Crossref-pinned title, container `Review of Financial Studies`, volume `27`, pages `2171-2218`, print date `2014-07`).
- Actually-read text (disclosed as the author-hosted working-paper PDF of the published article, not the publisher typeset): `https://academicweb.nd.edu/~zda/Frog.pdf`, fetched live 2026-10-14 as a 597,218-byte 48-page PDF (SHA-256 `7202cb81…ca14c525f`), converted locally and read in full (`pypdf` extraction, 144,949 characters, page header `[12:02 31/1/2014 RFS-hhu003.tex]`).
- Pinned headline spec (paper text, read verbatim modulo PDF spacing noise): the benchmark information-discreteness proxy is `ID = sgn(PRET) × [%neg − %pos]` (eq. 1), where `%pos`/`%neg` are the percentage of days during the formation period with positive/negative returns — `determined by the sign of daily returns and ignores their magnitude by equally weighting each observed return`; `PRET` is `a firm's cumulative return over the past twelve months after skipping the most recent month`; `sgn(PRET)` equals `+1 when PRET > 0 and −1 when PRET < 0`; `A large ID measure signifies discrete information, while a small ID measure signifies continuous information`.
- Pinned headline design: CRSP return data `after adjusting for delistings` plus Compustat accounting data with `negative book values` eliminated; sample `ends in 2007` with `starting dates ranging from 1927 to 1992 depending on firm-characteristic availability`; `incorporating a one-month interval between the formation period and holding period mitigates the impact of short-term return reversals due to illiquidity`; `sequential double-sorted portfolios that condition on formation-period returns, then ID`; `six-month holding period` (`ri,t+1,t+6` / `FIPRet t+1,t+6`); the `enhanced momentum strategy buys past winners and sells past losers following continuous information in the formation period`; continuous-information continuation `does not reverse in the long run` and `persists for eight months, while the momentum profit following discrete information becomes insignificant after two months`; Figure 1 illustrates the same-PRET contrast over `250 "daily" periods` (`ID equals −0.136` for the continuous path versus `0.072` for the discrete path).
- Pinned disentanglement boundary (all fenced, never carried): the paper distinguishes ID from Bali-Cakici-Whitelaw 2011 extreme-return proxies (`ignores magnitude` versus skewness/extremes over the same formation), from Grinblatt-Moskowitz 2004 return consistency (`RC` dummy requiring `eight of the twelve monthly returns` to share PRET's sign, motivated by disposition), from Grinblatt-Han 2005 `UCG` / Frazzini 2006 `CGO` unrealized-gain reference prices, from Fu 2009 four-factor-residual `IVOL`, from Hou-Moskowitz 2005 price-delay, and from Lesmond-Ogden-Trzcinka 1999 zero-return illiquidity (benchmark ID is `implicitly normalized by one since %pos + %neg + %zero = 1`; `IDZ`/`IDMAG` variants fenced, never computed here).
- Licence and rights: the record cites and normalizes the rule (short phrases and the two definitional equations only) and reproduces no figures, tables, or extended prose.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the paper's enhanced-momentum long leg (continuous-information winners) ported to one crypto asset as a 6-month-block long-or-flat hold — not a lossless reproduction of the paper's cross-sectional equity study. Researcher-declared adaptations are exactly six: (1) single-asset BTCUSDT Binance venue (every cross-stock sort, double-sort, Fama-MacBeth slope, factor adjustment, and return number is fenced off, never carried — see Negative evidence 1–2); (2) calendar-month grid on the 24/7 tape with simple close-to-close daily returns (CRSP distribution-inclusive equity returns versus BTC with no distributions; ~250 trading-day formation versus ~365 24/7 bars — see Negative evidence 4); (3) a 12-calendar-month formation ending one month before the decision (skip-latest-month) plus the paper's one-month formation-holding interval, with PRET compounded bar-for-bar from daily closes and ID from daily sign composition including zero-return days in the denominator (benchmark ID only — see Signal and Negative evidence 5); (4) a binary continuity gate `ID <= 0` collapsing the paper's ID quintiles plus a winner gate `PRET > 0`, with long iff both hold (the paper buys continuous winners and sells continuous losers; the short leg is fenced — see Negative evidence 3); (5) six-calendar-month sequential single-sleeve blocks with month-end-close decisions and next-bar-open fills, fixed 100%-equity 1× sizing, and a structural warmup to the September-2018 decision (the paper holds overlapping monthly cohorts with no order timing, sizing, or costs — see Execution assumptions); (6) long-flat direction mapping only (no short is enabled, explicitly none). The ID definition, the hold-continuous-winners direction, and the no-stop time-hold stance are source-faithful.

Pre-write dedup (2026-10-14): working-tree case-insensitive content searches for `frog`, `warachka`, `information discreteness`, `continuous information`, `discrete information`, `%pos`, `%neg`, `ID = sgn` return zero strategy records; filename searches for `frog`, `fip`, `warachka`, `gurun`, `discrete`, `continuous` return zero. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak), #49 (Gaussian channel StochRSI breakout), #63 (SuperTrend ATR-flip), #89 (Chandelier Exit stop-flip), #92 (SSL channel reversal) — different mechanisms, indicators, and sources; the last-100 closed PR titles carry no frog/FIP/discreteness-family record. Closest pool records differ in mechanism class: `jegadeesh-titman-6m-6m-momentum-long-flat-btcusdt-1d-2026-10-13.md` trades the bare 6-month formation sign with no skip and no daily-sign composition (a discrete winner with few large up-days prints long there and flat here — opposite triggers from disjoint inputs); `tsmom-12m-sign-monthly-long-btcusdt-1d-2026-10-10.md` trades the bare 12-month sign on a 1-month hold with no skip and no composition (same opposite-trigger split on discrete winners, plus a 1-month versus 6-block horizon); `novy-marx-12-7-intermediate-momentum-long-flat-btcusdt-1d-2026-10-13.md` trades the lagged intermediate window with no composition; `lee-swaminathan-2000-momentum-lifecycle-early-stage-long-flat-btcusdt-1d-2026-10-14.md` interacts formation returns with turnover terciles (this record never reads volume — a high-volume continuous winner prints early-stage-flat there by volume regime and long here by sign composition); `bali-cakici-whitelaw-2011-max-lottery-avoidance-long-flat-btcusdt-1d-2026-10-14.md` gates on the single largest daily spike with no formation return and no sign composition (a spiky discrete winner forces flat in both, but for opposite reasons — spike level there versus sign minority here); `gervais-kaniel-mingelgrin-high-volume-premium-long-flat-btcusdt-1d-2026-10-14.md` trades a volume-shock event with no return input; `amihud-2002-illiquidity-premium-gated-hold-long-flat-btcusdt-1d-2026-10-14.md` gates on the `|r| / notional` price-impact mean with no sign composition; `grinblatt-han-2005-capital-gain-overhang-long-flat-btcusdt-1d-2026-10-14.md` gates on a turnover-weighted cost-basis reference price (this record has no reference price, no turnover, no holdings); calendar records (`ariel-1987-monthly-half`, `turn-of-month-4day`, `monday-drift`, `sell-in-may`, `january-barometer`, `fomc-pre-announcement`, `pre-holiday-drift`, `heston-sadka-seasonal-same-month`) are pure date partitions with no price input. Five-axis distinction: no pool record and no open PR computes `sgn(PRET) × (%neg − %pos)` from daily sign composition over a 12-month skip-1 formation and holds only continuous winners for 6-month blocks.

## Economic mechanism

### Source-reported

Limited-attention underreaction to continuous information: `investors are inattentive to information arriving continuously in small amounts` — `a series of frequent gradual changes attracts less attention than infrequent dramatic changes`; `signals whose magnitudes are below a lower threshold k are processed with a delay`, so `continuous information induces strong persistent return continuation that does not reverse in the long run`, while discrete information attracts attention (higher media coverage, more press releases, larger earnings surprises coincide with discrete paths) and its continuation fades within two months. The ID proxy captures `the relative frequency of small signals (below k)` by sign composition alone, conditional on the formation return magnitude.

### Research interpretation

Continuity-filtered momentum, long-only, half-year cadence. Unlike bare-sign momentum systems there is no formation level that alone triggers exposure: a large 12-month gain built from a few jump days prints flat here and long in JT/TSMOM — the position exists if and only if the gain arrived gradually through a majority of green days. Unlike volume-conditioned records volume never appears anywhere: high-volume and low-volume continuous winners are treated identically, and a low-volume discrete winner is still flat. Unlike spike-avoidance records the statistic is a 12-month sign frequency, not a single-day extremum: a formation with no outsized day but a negative-day majority still prints discrete-flat. Unlike cost-basis/overhang records there is no reference price, no turnover weighting, and no holdings input. The bet, as derived, is purely that the documented continuous-winner continuation ports to BTCUSDT half-year blocks — and the position absorbs the paper's own discrete-leg pain (missed discrete continuations) plus full half-year drawdowns with no guardrail.

## Signal

Exact rule as pinned (12-calendar-month formation ending one month before the decision; one-month gap; daily-sign ID; 6-calendar-month sequential blocks; month-end-close decision; next-bar-open fills; long-flat — any other month definition, return definition, formation length, skip, gap, block length, cutoff, or tie rule is a different, unpinned rule):

- Bar grid: completed `1d` bars of BTCUSDT only. Month membership is the UTC calendar date of each daily bar — deterministic on the 24/7 tape.
- Daily return (pinned): `r(t) = (C(t) − C(t−1)) / C(t−1)` on consecutive completed daily bars (`C` = close; simple, not log; close-to-close, never high/low/open-based). The first history bar carries no `r` (no predecessor — skipped, pinned).
- Decision months (pinned phase): block-end months tiling every 6 calendar months forward from the first decidable month-end `2018-09-30`: `2018-09`, `2019-03`, `2019-09`, `2020-03`, and so on (March/September phase, pinned; any other phase is a different, unpinned rule).
- Formation for decision month `M` (pinned, skip-latest-month plus gap): the 12 calendar months `M−12 … M−1` (month `M` itself is the one-month formation-holding interval and is excluded from both statistics — the declared port of the paper's skip plus interval). Let `E(X)` be the close of the last completed daily bar dated in month `X`.
- PRET (pinned, paper definition ported bar-for-bar): `PRET(M) = E(M−1) / E(M−13) − 1` — the compounded 12-month return over formation months `M−12 … M−1` (base `E(M−13)` is the month-end close preceding the formation). No dividend or distribution adjustment exists for BTC.
- ID (pinned, paper eq. 1 benchmark): over exactly the `N` completed daily bars dated in formation months `M−12 … M−1`, count `n_pos` bars with `r > 0`, `n_neg` bars with `r < 0`, `n_zero` bars with `r == 0` (measure-zero on live tape); `%pos = n_pos / N`, `%neg = n_neg / N` (zeros stay in the denominator per `%pos + %neg + %zero = 1` — pinned, never renormalized); `sgn = +1` iff `PRET(M) > 0` else `−1` (the paper is silent at exactly zero — pinned here so ID is always computable, but the position rule below sends `PRET == 0` to flat regardless); `ID(M) = sgn × (%neg − %pos)`, range `[−1, +1]`.
- Position target for the next block of six calendar months `M+1 … M+6` (pinned, enhanced-long-leg direction): long iff `PRET(M) > 0` AND `ID(M) <= 0` (weak inequality; the exact `ID == 0` tie maps to long — pinned); else flat (this sends `PRET(M) <= 0` to flat with no short, and sends discrete winners `PRET(M) > 0, ID(M) > 0` to flat — the paper's attention-already-arrived leg, ridden as flat by construction).
- Orders (pinned): at most one order event per 6-month block boundary, placed for the first `1d` open of month `M+1` (next-open fill after the decision bar — the declared causal port; the paper rebalances overlapping cohorts with no executable fill convention): flat→long target buys 100% equity; long→flat target closes all; unchanged target places nothing. No intra-block evaluation, no intra-block orders, no adds, no partials, no second decision inside months `M+1 … M+6` for any reason including large adverse excursion.
- Risk legs (pinned absence, not invented): the paper ships no stop/target/trailing concept for the enhanced leg — the sole position-closing path is the next block-end signal mapping to flat. The derived posture is explicitly no stop, no target, no trailing, no opposite-signal exit, no calendar extension; a half-year adverse move inside a continuous-winner block is ridden in full by construction.
- Direction: long-or-flat, derived-and-declared (the paper's enhanced leg is long-short across continuous winners/losers; the loser leg is fenced and the futures venue is still pinned as the research market under the house overlay with the short permission simply unused, and a spot-only deployment expresses the identical event set).

## Required data

- Completed `1d` bars of BTCUSDT only: `close` (daily `r`, `PRET`, `%pos`/`%neg` composition) and `open` as fill price (no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, supply-feed, sentiment, macro, media-count, session-template, or cross-venue state gates any order). No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision grid: 6-calendar-month blocks on the March/September phase. One evaluation per block on the last completed daily bar of the block-end month; fills land on the next daily bar's open (first open of the new block). All formation inputs are completed-bar values — no provisional month-end value is ever used.
- Warmup: flat until the first holding block (structural, not conventional): the venue's 1d tape opens 2017-08-17 (verified live 2026-10-14 against the public spot kline feed — first three daily bars 2017-08-17 onward carry strictly positive closes and volumes); the first decidable block-end is 2018-09-30 (needs base `E(2017-08)` through gap `E(2018-09)` — month-ends 2018-08-31 and 2018-09-30 verified live); the first position block is October 2018 – March 2019. No repainting, no negative shift, no future reference, no full-sample normalization (PRET is a trailing compounded ratio; ID is a trailing sign frequency).

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared port of the paper's CRSP universe; no cross-venue equivalence claimed).
- Order timing (declared causal port; the paper ships no executable timing): block-end-bar-close decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill is claimed. At most one order exists per block boundary, so there is no same-bar dual-fire to sequence.
- Cash leg: flat earns nothing by record rule. No T-bill, stablecoin-lending, funding-rebate, or synthetic yield is substituted; the paper's cost-free accounting accrues no cash yield to either leg.
- Sizing/capital/costs: fixed 100%-equity single position, no adds, no leverage (1×, no margin concept), no compounding concept beyond equity. The paper reports cost-free sample statistics, so derived evaluation must carry the explicit house overlay (pinned house fees plus historical funding treatment; no hypothetical zero funding claimed — long blocks carry realized funding, flat blocks carry none, and the form holds genuine flat blocks so it is never an always-in-position funding accumulator). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one long position at any time; block regimes are disjoint by calendar construction, so overlapping entries are structurally impossible (no ignore-rule needed beyond the single-position book); after any block-end exit the next block-end decision fires on schedule (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic, no overlapping cohorts (the paper's overlapping monthly sleeves with 1/K turnover are replaced by the declared sequential single sleeve — see Limitations). The unused short permission requires no margin-short modeling. Safety orders: explicitly none.

## Evidence

### Source-reported

The paper ships every adopted headline fact quoted in Provenance: the sign-only `ID = sgn(PRET) × [%neg − %pos]` definition (eq. 1) with its equally-weighted daily-sign construction, the 12-month-skip-most-recent-month PRET definition, the CRSP-delisting-adjusted plus Compustat design ending 2007, the one-month formation-holding interval, the PRET-then-ID sequential double-sorts, the six-month holding grid with its eight-month persistence versus two-month discrete fade and no long-run reversal, the Figure-1 same-PRET illustration, and the enhanced continuous-winner/continuous-loser long-short construction with its limited-attention reading. It ships zero adopted performance numbers for this record: every spread, t-statistic, R², autocorrelation, and Figure-1 level describes its equity sample, never a single-asset BTCUSDT derivative — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Cross-section fenced: every double-sort, independent-sort, Fama-MacBeth slope, three-factor adjustment, size/BM control, institutional-ownership/analyst/media split, and Table/Figure moment belongs to the paper's equity cross-section — none transfers to a single-asset crypto time-series rule, and none is adopted.
2. Number silence fenced: no spread, t-statistic, R², autocorrelation, Figure-1 ID level, or sample-window moment from any paper table, equation fit, or figure is adopted anywhere — figures are omitted by rule, and any dispute over exact magnitudes is decided against this record, never patched by inference.
3. Quintile-to-binary collapse disclosed: the paper sorts ID into quintiles (plus `PosID`/`NegID` signed splits); this record collapses continuity to the fixed `ID <= 0` versus `ID > 0` partition with the tie to long. Any other quantile, median pool, or cutoff would be a different, unpinned rule — the binary gate is a researcher pin, never a paper convention.
4. Timing-derivation disclosed: the paper holds overlapping monthly cohorts over ~250 trading-day formations with a one-month gap; this record holds one sequential 6-month sleeve per block over ~365-bar 24/7 formations with the gap pinned to the decision month. Any turnover, smoothing, or diversification property of the overlapping construction is discarded, not carried.
5. Zero/variant derivation disclosed: benchmark ID keeps zero-return days in the denominator (`%pos + %neg + %zero = 1`); `IDZ` (renormalized) and `IDMAG` (declining |return|-weighted) are fenced, never computed. CRSP daily returns are distribution-inclusive; BTC closes are not — fenced, never adjusted.
6. Rival-measure disentanglement fenced: return consistency (8/12-month `RC`), unrealized-gain overhang (`UCG`/`CGO`), idiosyncratic volatility (`IVOL`), price delay, skewness, and MAX-extreme proxies are all distinguished in-paper from ID and none is computed here — this record never forms a monthly-consistency dummy, a reference price, a factor residual, a volatility level, or a spike extremum.
7. No-short, no-stop exposure disclosed: discrete winners print flat and can drift upward without participation for six months; continuous-winner blocks ride entire adverse half-years with no guardrail; all losers print flat so any loser-continuation downside hedge in the paper's short leg is deliberately unowned here.
8. Derivation boundary fenced: the only non-paper behavior is the six declared adaptations (single asset, calendar months plus close-to-close returns, 12m-skip-1 plus gap plus daily-sign ID with zero-in-denominator, binary `ID <= 0` plus winner gate, sequential 6m blocks plus next-open fills plus fixed sizing plus structural warmup plus house costs, long-flat mapping); the ID definition, the hold-continuous-winners direction, and the no-stop stance are source-faithful. This record is therefore never evidence that the paper's equity study passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 12-month formation `M−12 … M−1` / skip-plus-gap month `M` / compounded PRET / daily-sign ID with zeros in denominator / `PRET > 0` plus `ID <= 0` long gate with ties pinned / block-end-close decision / next-open fills / sequential 6-month single-position long-flat / `1d` BTCUSDT are frozen.

- F1 — Continuity relevance: a discrete-winner twin (long iff `PRET(M) > 0` AND `ID(M) > 0`, flat otherwise, same block grid and fills) must not improve net expectancy; fail ⇒ the continuity partition points the wrong way on this tape and the limited-attention read inverts.
- F2 — Composition-vs-sign relevance: a bare-sign twin (long iff `PRET(M) > 0`, ignoring ID entirely, same block grid and fills) must not improve net expectancy; fail ⇒ the daily-sign composition adds nothing over the raw 12-month sign and the paper's core construction is doing no work here.
- F3 — Winner-direction relevance: a continuous-loser twin (long iff `PRET(M) < 0` AND `ID(M) <= 0`, flat otherwise, same block grid and fills) must not improve net expectancy; fail ⇒ the winner leg does not survive the port and the record's long side is doing negative work.
- F4 — Selectivity relevance: buy-and-hold over the same sample must not improve net expectancy; fail ⇒ sitting out discrete-winner and loser blocks costs more in missed drift than it saves — or the record's selectivity pin is doing unacknowledged work.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid 6-calendar-month March/September blocks on `1d` closes; fills at next-block first-bar opens; no venue-specific read). The arithmetic ports across perpetual venues without structural change (no corporate-action or calendar adjustment exists to recheck). No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no media-count input, no cross-venue state. Extension to other house-universe assets, month definitions, formation lengths, skips, gaps, block lengths, cutoffs, or timeframes would be a different, unpinned claim.

## Limitations

- Single-asset port: the paper's evidence is a cross-sectional equity study; BTCUSDT continuity-regime behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Mechanism mismatch: whatever limited-attention clientele sits behind the equity effect has no established crypto analogue (24/7 global tape, concentrated venues, perpetual-funding holders, stablecoin quote, thin early history) — the port bets on regime persistence, not on a verified crypto mechanism.
- Binary-collapse rigidity: the fixed `ID <= 0` partition never adapts — a tape where every formation prints majority-positive drifts nearly always-long on winners, while a jump-dominated tape goes nearly always-flat on winners, both by construction.
- Month-definition rigidity: gap-month information is observed at the decision but excluded from both statistics by rule; a shock arriving across a block boundary is attributed to whole blocks; a first-of-block gap against the fresh regime is taken at the post-move open, never at the edge.
- Sequential-holding deviation: the source's overlapping-cohort turnover smoothing and diversification are lost by declared derivation; replication disputes are decided against this record's pin, never patched silently.
- No price stop, no intra-block exit: adverse excursion inside the six-month holding block has no guardrail; the next decision is months away by construction.
- Warmup cost: everything before the October-2018 first holding block is flat by record rule, so the 2017–2018 tape is deliberately untraded — pinned, not recovered.

## Implementation status

not-implemented. No Hummingbot controller/executor has been written for this record; the Execution assumptions section names the exact pinned engine path (package `20260920`, VERSION `dev-2.17.0`, block-end-close decision on completed `1d` bars, next-block-first-open market fills, single-asset 100%-equity 1× long-or-flat) that a future implementation must target, with representative event-level Qlib/Hummingbot parity required before any mass screening.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. PASS means the declared derived strategy is causally expressible under the pinned Hummingbot model — not profitable, not Qlib-paritied, not source-equivalent, not live-tradable.

## Related Wiki records

None.

## Sources

- Da, Zhi / Gurun, Umit G. / Warachka, Mitch (2014). Frog in the Pan: Continuous Information and Momentum. Review of Financial Studies 27(7), 2171–2218. https://doi.org/10.1093/rfs/hhu003 (Crossref-verified 2026-10-14; author-hosted working-paper PDF https://academicweb.nd.edu/~zda/Frog.pdf fetched live 2026-10-14, 597,218-byte 48-page PDF, SHA-256 `7202cb81…ca14c525f`, read in full locally — 144,949 characters)
