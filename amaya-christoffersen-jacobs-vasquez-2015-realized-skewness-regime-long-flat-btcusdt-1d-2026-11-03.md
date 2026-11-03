---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Amaya-Christoffersen-Jacobs-Vasquez 2015 realized-skewness 7-day zero-boundary regime long-flat on BTCUSDT 1d
created: 2026-11-03
updated: 2026-11-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2015-10-01
sources:
  - https://doi.org/10.1016/j.jfineco.2015.02.009
  - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1898735
  - https://repec.econ.au.dk/repec/creates/rp/13/rp13_41.pdf
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Amaya-Christoffersen-Jacobs-Vasquez 2015 realized-skewness 7-day zero-boundary regime long-flat on BTCUSDT 1d

## Provenance

Primary source identity verified end to end (Crossref API record hand-fetched plus the authors' working paper fetched live and read locally, 2026-11-03):

- Amaya, Diego, Christoffersen, Peter, Jacobs, Kris, and Vasquez, Aurelio, `Does realized skewness predict the cross-section of equity returns?` — Journal of Financial Economics, vol. 118, 135–167 (October 2015). DOI `10.1016/j.jfineco.2015.02.009` (Crossref-pinned title, container, volume `118`, issue `1`, pages `135-167`, four author surnames, print date 2015-10 — verified field by field this cycle).
- Actually-read text (disclosed as the working-paper version, not the typeset journal): CREATES Research Paper `2013-41` (February 2013), fetched live 2026-11-03 as a 718,060-byte 50-page PDF, converted locally and read (`pypdf` extraction, 121,341 characters). SSRN trail `abstract=1898735`.
- Pinned headline spec (working-paper text, read verbatim modulo PDF hyphenation noise): daily realized variance `RDVar(t) = sum r(t,i)^2` over intraday returns with `we do not estimate the mean of the high-frequency return because it is dominated by the variance at this frequency` (§2.2, eq. 2); daily realized skewness `RDSkew(t) = sqrt(N) * sum r(t,i)^3 / RDVar(t)^{3/2}`, with `negative values indicate that the stock's return distribution has a left tail that is fatter than the right` (§2.2, eq. 3); daily realized kurtosis `RDKurt(t) = N * sum r(t,i)^4 / RDVar(t)^2` (§2.2, eq. 4); weekly estimators as the mean of the five daily estimators `RSkew(t) = (1/5) sum RDSkew` (§2.2, eqs. 5–7); `The weekly realized moment estimator is the average of the available daily estimators (Wednesday through Tuesday)` (§2.2); sorts `every Tuesday` into deciles on the trailing weekly realized moments with Tuesday-close-to-Tuesday-close holding returns (§3.1); headline direction — low (negative) realized-skewness stocks earn higher subsequent returns, the skewness premium for bearing left-tail asymmetry (§§3–6, fenced to equities).
- This record adopts no performance number: the journal long-short gap, t-statistics, alphas, and decile return levels all describe the paper's equity cross-section and none is carried anywhere below.
- Licence and rights: the paper is a published journal article plus openly hosted author/SSRN/RePEc working papers — this record cites and normalizes the rule (short phrases and the definitional equations only) and reproduces no figures, tables, or extended prose.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the paper's intraday-realized-skewness sort ported to one crypto asset as a daily zero-boundary long-or-flat regime hold — not a lossless reproduction of the paper's equity cross-sectional study. Researcher-declared adaptations are exactly eleven: (1) single-asset BTCUSDT Binance USDT-M perpetual venue (every cross-sectional sort, decile breakpoint, alpha, t-statistic, and return number is fenced off, never carried); (2) 5-minute sampling kept as in the paper but on the 24/7 tape so `N = 288` per UTC day (the paper's 6.5-hour session uses `N = 78`) — scaling constant only, formulas unchanged; (3) the paper's Wednesday-through-Tuesday 5-trading-day mean becomes a rolling 7-calendar-day mean (no market holidays on this tape); (4) the paper's every-Tuesday sort becomes a every-UTC-day-boundary evaluation on the rolling 7-day window — no calendar predicate anywhere, this is not a clock rule; (5) the cross-sectional decile sort becomes a time-series zero boundary, anchored on the paper's own Table 1 Panel B (middle deciles straddling zero) and §6 sign-switch discussion — never a rolling median or fitted level; (6) the `RDVar = 0 → RDSkew := 0` degenerate-day convention (probe: zero triggers on the full tape); (7) day-boundary-close decision with next-bar-open market fills at fixed 0.01 BTC 1× (the paper ships no order timing, sizing, or costs); (8) no value-/equal-weight portfolio or rebalancing concept — one position, no adds, no partials, no pyramiding; (9) explicit research cost overlay of 0.05% per side plus realized funding while long (never hypothetical zero funding); (10) no stop/target/trailing/time exit (the paper ships none — the sole closing path is the regime exit to flat); (11) long-flat direction mapping only (the paper's high-skew short leg is explicitly closed — no short is enabled, explicitly none). The eq. 2/eq. 3 definitions, the no-mean-estimation convention, the avoid-negative-skew direction, and the no-stop stance are source-faithful.

Pre-write dedup (2026-11-03): working-tree base is current `main@7a90797f` (533 root strategy records). Case-insensitive content searches for `rdskew|rskew|realized skew`, `amaya|christoffersen`, and `kurtosis` return zero strategy records; `skew` returns exactly five records, every one a fenced non-signal mention — `bali-…-max-lottery-avoidance` (cites skewness only as a paper control variable), `da-gurun-warachka-2014-fip` (fences skewness/MAX proxies as distinguished rivals, computes none), `fmz-426571-kase-devstop` (Kase prose `volatility skew` for stop placement), `holmberg-orb` (Table 1 sample-description statistic `skew 0.16`), `worldquant-alpha9` (`rarity skew`措辭 for streak rarity). No pool record computes a third moment, a realized moment, or any intraday-return aggregation. All 16 open `research/*` PRs enumerated by number/title/branch — none is this paper, family, or construction. Nearest pool records differ in signal object: `bali-cakici-whitelaw-2011-max-lottery-avoidance-long-flat-btcusdt-1d` (monthly single largest daily return, an order statistic of return levels on `1d` bars, 36-month trailing 80th-percentile gate — this record uses 288 intraday 5-minute returns per day formed into a standardized third moment, a distribution-shape statistic, with a fixed zero boundary and daily cadence); `amihud-2002-illiquidity-premium-gated-hold` (same regime-hold long-flat next-open shape, but driven by `|r|/DVOL` price impact reading volume — this record never reads volume); `hurst-ooi-pedersen-century-trend-composite-long-flat` (paper-derived long-hold with no risk legs, but driven by 1/3/12-month return-sign majority vote — momentum level, not distribution shape, monthly not daily). Five-axis distinction: no pool record and no open PR conditions exposure on an intraday realized-skewness regime.

## Economic mechanism

### Source-reported

Skewness premium, not lottery-level chasing: investors dislike left-tail asymmetry and demand compensation for holding negatively-skewed return distributions, while positively-skewed lottery-like payoffs are overpriced and earn lower subsequent returns — so the lowest realized-skewness decile outperforms, controlling for size, book-to-market, momentum, reversals, illiquidity, and historical skewness. (All mechanism framing fenced to the paper's equity sample, never adopted as a crypto claim here.)

### Research interpretation

Left-tail-compensation regime hold, long-only, daily cadence. Unlike return-conditioned momentum records there is no formation total return and no winner/loser ranking: the position exists if and only if the trailing seven days of intraday return asymmetry lean left (negative) against a fixed zero boundary. Unlike volume-shock records volume never enters anywhere. Unlike calendar holds there is no date input anywhere — UTC day boundaries are only the evaluation grid, never a long/flat partition. The bet, as derived, is purely that the documented negative-skew compensation partition ports to BTCUSDT intraday bars, never on a level, band, return-sign, weekday, or funding anchor — and the position sits through any within-regime slide with no guardrail.

## Signal

Exact rule as pinned (daily decision on completed UTC days; next-bar-open fills; long-flat — any other sampling frequency, window, boundary, return definition, sizing, or fill is a different, unpinned rule):

- R1 — Measure grid: completed `5m` bars of BTCUSDT only. UTC days run 00:00:00 inclusive to next 00:00:00 exclusive (288 bars). A day is evaluable only if it carries exactly 288 completed bars.
- R2 — Intraday log returns: for UTC day `t` with closes `c(t,1..288)`, anchor `p(t,0)` is the previous complete day's last `5m` close; `r(t,i) = ln(c(t,i) / c(t,i-1))`, `i = 1..288`, with `c(t,0) = p(t,0)`. No demeaning (paper §2.2: high-frequency mean dominated by variance, never estimated). Closes are strictly positive on any traded tape; a non-positive print excludes that bar and the day becomes unevaluable (defensive pin, disclosed, never exercised).
- R3 — Daily realized moments (paper eqs. 2–3 straight port, `N = 288`): `RDVar(t) = Σ r(t,i)^2`; `RDSkew(t) = sqrt(288) · Σ r(t,i)^3 / RDVar(t)^{3/2}`. Degenerate convention (declared derivation): `RDVar(t) = 0 ⇒ RDSkew(t) := 0` (dead-flat day carries no asymmetry).
- R4 — Weekly realized skewness (paper eq. 6 adapted to 7 calendar days): `RSkew7(t) = (1/7) Σ RDSkew(t-j)`, `j = 0..6`, requiring seven consecutive evaluable UTC days; otherwise day `t` is not evaluated.
- R5 — Position target (pinned): target for day `t+1` is long iff `RSkew7(t) < 0` (strict inequality; the exact-zero tie maps to flat — measure-zero tie rule, pinned), else flat.
- R6 — Orders (pinned): at most one order event per day boundary, filled at the next UTC day's first `5m` bar open (00:00 open market fill after the day-boundary decision — the declared causal port; the paper ships no fill convention): flat→long target buys 0.01 BTC; long→flat target closes all; unchanged target places nothing. No intrabar evaluation, no intrabar orders, no adds, no partials, no pyramiding. Decisions on distinct day boundaries fill on distinct day opens — no same-bar dual-fire exists to sequence.
- R7 — Risk legs (pinned absence, not invented): the paper ships no stop/target/trailing concept for the skewness partition — the sole position-closing path is the regime exit to flat at a day-boundary close (filled next open). The derived posture is explicitly no stop, no target, no trailing, no opposite-signal exit, no time exit; a fully ridden within-regime slide is absorbed exactly as printed by construction.
- R8 — Direction: long-or-flat, derived-and-declared (the paper's long-short decile framing carries no short leg here — no short is enabled, explicitly none; the futures venue is pinned as research market with the short permission simply unused).
- R9 — Warmup and gaps: the first seven evaluable UTC days accumulate only, never trade; the first decision fires at the earliest day boundary backed by seven consecutive evaluable days (structural, not conventional). Any unevaluable day (missing bars, ≠288 bars, non-positive print) suspends evaluation and the target freezes at its prior value — never forced flat, never backfilled; held positions ride through frozen stretches by construction.
- R10 — Invariant identifier: `JFE:Amaya2015-10.1016_j.jfineco.2015.02.009|RDSkew-eq3-5mN288_7d-mean_zero-boundary|independent-derived-v1|BinanceFutures:BTC-USDT:5m-measure_1d-decision|LONG-FLAT|nextbar-MARKET|fee0.0005|lev1x|size0.01|warmup7d|2026-11-03` (any constant, window, frequency, boundary, direction, sizing, or cost change is a different derivative).

## Required data

- Completed `5m` bars of BTCUSDT only: `close` (all 288 intraday log returns, `RDVar`, `RDSkew`, `RSkew7`), `open` of the next day's first bar as fill price (no `high`, no `low`, no volume, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, supply-feed, sentiment, macro, session-template, or cross-venue state gates any order). No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision grid: one evaluation per UTC day boundary at the last bar's close; fills land on the next day's first bar open. All inputs are completed-bar values — no provisional intrabar value is ever used.
- Warmup: flat until the first day boundary backed by seven consecutive evaluable UTC days (structural: on this venue that is the 8th day of history). No repainting, no negative shift, no future reference, no full-sample normalization (every `RDSkew` is a same-day statistic; the 7-day mean is a trailing average; the boundary is the constant zero).

## Execution assumptions

- Research market: BTCUSDT Binance USDT-M perpetual, 1×, no margin concept beyond the single fixed 0.01 BTC position (declared port of the paper's NYSE/AMEX/NASDAQ universe; no cross-venue equivalence claimed).
- Order timing (declared causal port; the paper ships no executable timing): day-boundary-close decision with next-bar-open market fills — the same convention as the admitted `bali-cakici-whitelaw-2011-max-lottery-avoidance` record, which states it outright as compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill is claimed. At most one order exists per day boundary, so there is no same-bar dual-fire to sequence.
- 5-minute feed on the pinned path: scout-claimed (not independently proven here) that `HCH725/hummingbot@8b0e067` carries a `5m` interval in the Binance perpetual candles constants with the standard run-backtesting entry — the independent auditor must re-verify this feed claim line-level at the exact head; if the `5m` feed path cannot be established, this record must not merge.
- Cash leg: flat earns nothing by record rule. No T-bill, stablecoin-lending, funding-rebate, or synthetic yield is substituted.
- Sizing/capital/costs: fixed 0.01 BTC per entry, no adds, no leverage, no compounding concept beyond the position. Explicit research cost overlay: 0.05% taker fee per side; realized funding accrues on long days, flat days carry none — no hypothetical zero funding is claimed anywhere (long stretches are genuine holders, never an always-in accumulator). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one long position at any time; day regimes advance in order so overlapping entries are structurally impossible; after any exit the next day-boundary decision fires on schedule (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The unused short permission requires no margin-short modeling. Safety orders: explicitly none.

## Evidence

### Source-reported

The paper ships every adopted headline fact quoted in Provenance: the intraday realized-variance/skewness/kurtosis definitions (eqs. 2–4), the no-mean-estimation convention, the Wednesday-through-Tuesday 5-day weekly averaging (eqs. 5–7), the every-Tuesday decile formation with following-week holding, and the negative-skew-compensation headline direction. It ships zero adopted performance numbers for this record: every long-short gap, alpha, and t-statistic describes its equity cross-section, never a single-asset BTCUSDT derivative — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Research probe executed during this scout cycle (tape-exact for the declared spec — Binance USDT-M `5m` closes, 2023-06-02 → 2026-11-03, 1,251 UTC days of which 1,249 complete 288-bar days; rule R1–R9 as printed; next-open fills; degenerate-day count zero):

- Signal distribution: `RDSkew` n = 1,249 (mean −0.0187, median −0.0243, sd 1.327, min −10.877, max 11.832, negative share 51.5%); `RSkew7` n = 1,243 (mean −0.0173, median −0.0035, sd 0.493, min −2.760, max 2.059, negative share 50.5%) — the zero boundary binds on roughly half the tape, never degenerate-always-long or always-flat.
- Events: 102 entries / 101 exits (long into the 2026-11-02 decision), median hold 5 days, mean 6.06 days; double-run digest stable across independent replays.
- Implant tapes: dead-flat tape ⇒ `RDSkew = 0 ⇒ RSkew7 = 0 ⇒` flat with zero events (tie-to-flat verified); single −2% shock day followed by calm ⇒ `RDSkew = −14.357 ⇒ RSkew7 = −2.051 ⇒` long (left-tail sign verified); mirrored +2% shock ⇒ flat (asymmetry sign verified).
- No profitability, Sharpe, drawdown, fee-drag, or funding figure is adopted from the probe — event existence and boundary behavior only.

### Negative evidence

1. Cross-section fenced: every decile sort, alpha, t-statistic, transition matrix, bivariate sort, and Fama-MacBeth slope in the paper belongs to its equity cross-section — none transfers to a single-asset crypto time-series rule, and none is adopted.
2. Number silence fenced: no return gap, alpha, t-statistic, percentile level, or sample-window moment from any paper table or figure is adopted anywhere — figures are omitted by rule, and any dispute over exact magnitudes is decided against this record, never patched by inference.
3. Boundary pin disclosed: the paper sorts and holds deciles but never trades a single-asset `RSkew7 < 0` time-series rule — the zero boundary is researcher-pinned from the paper's Table 1 middle-decile straddle and §6 sign-switch discussion, never a paper convention. Any other window, boundary, or level would be a different, unpinned rule.
4. Sampling-port derivation disclosed: the paper's `N = 78` (6.5-hour session) and 5-trading-day week are equity-market facts; this record's `N = 288` and 7-calendar-day mean are 24/7-tape ports. The paper's own §2.3 warns moment estimates shift with sampling frequency — so this record pins `5m` exactly and claims nothing about any other frequency.
5. Fully exposed inside the regime: once long for a regime, the position rides the entire adverse excursion with no guardrail — a sharp selloff inside a negative-skew hold is held to the next day-boundary close by construction. This is the coded trade, disclosed, not a tunable parameter here (negative-skew regimes by the paper's own logic concentrate left-tail realizations).
6. Derivation boundary fenced: the only non-paper behavior is the eleven declared adaptations (single asset, `N = 288` plus 7-day mean, daily grid, zero boundary, degenerate convention, next-open fills plus fixed sizing plus warmup plus house costs, no risk legs, long-flat mapping); the eq. 2/eq. 3 definitions, the no-mean convention, the negative-skew-long direction, and the no-stop stance are source-faithful. This record is therefore never evidence that the paper's equity study passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `5m` sampling / log returns / `N = 288` / 7-day mean / zero boundary with strict-inequality tie-to-flat / day-boundary-close decision / next-open fills / fixed 0.01 BTC 1× long-flat / BTCUSDT are frozen.

- F1 — Frequency relevance: a `1h`-sampling twin (same formulas with `N = 24`, same 7-day mean, boundary, grid, and fills) must not improve net expectancy; fail ⇒ the paper's §2.3 frequency dependence bites and the `5m` pin is doing unacknowledged work (probe note: the two samplings agree in sign on only about seven-in-ten overlapping days — disclosed, never carried as a record fact).
- F2 — Boundary relevance: a trailing-median-boundary twin (long iff `RSkew7` sits below its own trailing-182-day median, same grid and fills) must not improve net expectancy; fail ⇒ the fixed zero pin adds nothing over an adaptive level and the Table 1 anchoring is decorative.
- F3 — Direction-mapping relevance: a long-short twin (short enabled on `RSkew7 ≥ 0`, same grid and fills) must not owe its full result to the short leg; fail ⇒ the paper's long-short framing does not survive the long-flat port and the short closure hides the effect.
- F4 — Selectivity relevance: buy-and-hold over the same sample must not improve net expectancy; fail ⇒ sitting out non-negative-skew days costs more in missed drift than it saves in avoided exposure.

## Crypto portability

Pinned to BTCUSDT Binance USDT-M perpetual (decision grid day-boundary `5m` bar closes; fills at next-day first-bar opens; no venue-specific read). The arithmetic ports across perpetual venues without structural change (no volume, corporate-action, or calendar adjustment exists to recheck; a spot-only deployment expresses the identical event set — pinned, not approximated). No short leg exists to port. Extension to other house-universe assets, sampling frequencies, windows, boundaries, or timeframes would be a different, unpinned claim.

## Limitations

- Single-asset port: the paper's evidence is an equity cross-section; BTCUSDT skew-regime behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Mechanism mismatch: whatever institutional clientele sits behind the equity skewness premium has no established crypto analogue (24/7 global holder base, different spike rhythms, perpetual-funding holders) — the port bets on regime persistence, not on a verified crypto mechanism.
- Boundary rigidity: the fixed zero boundary never adapts — a structurally shifted tape goes nearly always-long or nearly always-flat by construction, with no recalibration inside this record.
- Day-definition rigidity: a shock arriving across a UTC boundary is attributed to whole days; a gap against the fresh regime is taken at the post-move open, never at the edge.
- Warmup cost: everything before the first seven-evaluable-day boundary is flat by record rule, so early history is deliberately untraded — pinned, not recovered.
- Feed contingency: the `5m` pinned-engine feed claim is scout-asserted and auditor-unverified at submission — if the exact-head review cannot establish it, this record must close rather than remap to another timeframe.

## Implementation status

not-implemented. No Hummingbot controller/executor has been written for this record; the Execution assumptions section names the exact pinned engine path (package `20260920`, VERSION `dev-2.17.0`, day-boundary-close decision on completed `5m` bars, next-day-first-open market fills, single-asset fixed 0.01 BTC 1× long-or-flat) that a future implementation must target, with representative event-level Qlib/Hummingbot parity required before any mass screening.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. `hb_ready_status: PASS` here is the Scout's evidence-backed admission proposal for this independent derivative only, pending independent Hermes Auditor exact-head review — not self-approval, not profitability, not Qlib parity, not source-equivalence, not live-tradable. Only the independent reviewer may remediate source-verifiable facts, exact-head merge on six-gate PASS, or close as NOT_LOSSLESS.

## Related Wiki records

None.

## Sources

- Amaya, Diego, Christoffersen, Peter, Jacobs, Kris, and Vasquez, Aurelio (2015). Does realized skewness predict the cross-section of equity returns? Journal of Financial Economics 118, 135–167. https://doi.org/10.1016/j.jfineco.2015.02.009 (Crossref-verified 2026-11-03; SSRN trail https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1898735; RePEc trail https://repec.econ.au.dk/repec/creates/rp/13/rp13_41.pdf; CREATES RP 2013-41 fetched live 2026-11-03, 718,060-byte 50-page PDF, read in full locally)
