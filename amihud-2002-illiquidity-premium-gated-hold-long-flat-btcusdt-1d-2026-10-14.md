---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Amihud 2002 illiquidity-premium expected-ILLIQ-gated hold long-flat on BTCUSDT 1d bars
created: 2026-10-14
updated: 2026-10-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2002-01-01
sources:
  - https://doi.org/10.1016/S1386-4181(01)00024-6
  - https://www.cis.upenn.edu/~mkearns/finread/amihud.pdf
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Amihud 2002 illiquidity-premium expected-ILLIQ-gated hold long-flat on BTCUSDT 1d bars

## Provenance

Primary source identity verified end to end (Crossref metadata hand-fetched plus the full journal text read locally, 2026-10-14):

- Yakov Amihud, `Illiquidity and stock returns: cross-section and time-series effects` — Journal of Financial Markets, vol. 5, issue 1, 31–56 (January 2002). DOI `10.1016/S1386-4181(01)00024-6` (Crossref-pinned title, container, volume `5`, pages `31-56`, print date `2002-01`).
- Actually-read text (disclosed as an openly hosted PDF of the typeset journal article, not a working paper): `https://www.cis.upenn.edu/~mkearns/finread/amihud.pdf`, fetched live 2026-10-14 as a 201,728-byte 26-page PDF (SHA-256 `349823bb…5f7118b`), converted locally and read in full (`pypdf` extraction, 64,421 characters).
- Pinned headline spec (journal text, read verbatim modulo PDF spacing noise): `Stock illiquidity is defined here as the average ratio of the daily absolute return to the (dollar) trading volume on that day, |R|/VOLD`; the cross-sectional construction is the annual average `ILLIQ = 1/D Σ |R|/VOLD` over the year's available days (eq. 1); it is `interpreted as the daily price response associated with one dollar of trading volume, thus serving as a rough measure of price impact`, following `Kyle's concept of illiquidity — the response of price to order flow`.
- Pinned headline sample and design: NYSE stocks 1963–1997 from CRSP daily/monthly files (stocks admitted with 200+ day histories, end-of-year price above $5, 1% ILLIQ-tail trimming); monthly Fama-MacBeth cross-sections over 1964–1997 (408 months); annual market illiquidity `AILLIQ` as the cross-stock mean each year (34 annual values, 1963–1996).
- Pinned headline findings (journal text, qualitative only — no slope, t-statistic, R², or return number is adopted anywhere in this record): `across NYSE stocks during 1964–1997, ILLIQ has a positive and highly significant effect on expected return`; the new time-series tests show `expected market illiquidity has a positive and significant effect on ex ante stock excess return, and unexpected illiquidity has a negative and significant effect on contemporaneous stock return`; expected illiquidity is obtained from an autoregressive model (`lnAILLIQ` AR(1), raw slope 0.768, Kendall-bias-corrected 0.869 — cited as source texture only, never imported); the conclusion fences the mechanism to compensation: the excess return `also provides compensation for the lower liquidity of stocks relative to that of Treasury securities` and `expected stock excess returns are not constant but rather vary over time as a function of changes in market illiquidity`.
- Licence and rights: the record cites and normalizes the rule (short phrases and the one definitional equation only) and reproduces no figures, tables, or extended prose.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the paper's expected-illiquidity premium ported to one crypto asset as a monthly expected-ILLIQ-gated long-or-flat hold — not a lossless reproduction of the paper's equity market study. Researcher-declared adaptations are exactly six: (1) single-asset BTCUSDT Binance venue (every cross-stock sort, Fama-MacBeth slope, alpha, t-statistic, and return number is fenced off, never carried — see Negative evidence 1–2); (2) calendar-month formation grid on the 24/7 tape with close-to-close simple daily returns and notional dollar volume `C×V` in USDT (the paper's CRSP daily returns include distributions; BTC has none — see Signal and Negative evidence 4); (3) a trailing-252-daily-bar ILLIQ window ported bar-for-bar from the paper's ~252-trading-day annual average, evaluated at each month-end (the paper forms annual characteristics and monthly FM tests — see Negative evidence 3); (4) a trailing-36-month median gate as the expected-illiquidity partition (the paper forecasts expected illiquidity with a fitted AR(1); no fitted coefficient is imported — see Negative evidence 5); (5) month-end-close decision with next-bar open fills, fixed 100%-equity 1× sizing, and a structural warmup to the 37th computable month-end (the paper ships no order timing, sizing, or costs — see Execution assumptions); (6) long-flat direction mapping only (the paper's long-only market-premium framing carries no short leg here — no short is enabled, explicitly none). The ILLIQ definition, the hold-when-illiquid direction (H-1), and the no-stop time-hold stance are source-faithful.

Pre-write dedup (2026-10-14): working-tree case-insensitive content search for `amihud` returns zero strategy records; filename search for `amihud` returns zero; no pool record computes a `|return| / dollar-volume` price-impact ratio under any name. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak), #49 (Gaussian channel StochRSI breakout), #63 (SuperTrend ATR-flip), #89 (Chandelier Exit stop-flip), #92 (SSL channel reversal) — different mechanisms, indicators, and sources; the last-100 closed PR titles carry no illiquidity/Amihud-family record. Closest pool records differ in mechanism class: `gervais-kaniel-mingelgrin-high-volume-premium-long-flat-btcusdt-1d-2026-10-14.md` trades a volume-shock event with no return input anywhere (this record never fires on volume alone — a high-volume day with a tiny absolute return prints low ILLIQ and pushes toward flat); `alma-cross-volume-gate-btcusdt-1d-2026-10-09.md` trades an ALMA 60/120 cross gated by a volume-momentum oscillator with fixed-percentage TP/SL exits (this record has no average, no cross, no oscillator, and no percentage exits); `obv-ema-crossover-trend-*.md`, `mfi-threshold-divergence-*.md`, `cmf-velocity-zero-cross-*.md`, `klinger-volume-oscillator-*.md`, `force-index-100-zero-state-*.md`, `pvo-signal-cross-*.md`, and `chaikin-oscillator-ad-zero-cross-*.md` are cumulative/oscillator volume-momentum constructions with zero-cross or divergence triggers (none forms a per-notional price-impact level, none gates on a trailing median of that ratio); `bali-cakici-whitelaw-2011-max-lottery-avoidance-long-flat-btcusdt-1d-2026-10-14.md` gates on the single largest daily spike versus its own history with no volume input (a high-spike low-volume month forces flat there and long here — opposite triggers from disjoint inputs); momentum/reversal records (`jegadeesh-titman-6m-6m`, `novy-marx-12-7`, `liu-tsyvinski-1w`, `tsmom-12m`, `lehmann-1990-weekly`, `jegadeesh-1990-monthly`, `debondt-thaler-36m`) condition on return levels or signs with no volume normalization; calendar records (`monday-drift`, `turn-of-month-4day`, `ariel-1987-monthly-half`, `sell-in-may`, `fomc-pre-announcement`, `pre-holiday-drift`) are pure date partitions with no price input. Five-axis distinction: no pool record and no open PR computes `mean(|r| / dollar-volume)`, ranks it against its own trailing history, holds the illiquid regime for a compensation premium, or exits to flat on liquefaction.

## Economic mechanism

### Source-reported

Illiquidity-premium compensation, not risk compensation: `expected stock excess return partly represents an illiquidity premium`, increasing in expected market illiquidity — the excess return `usually referred to as "risk premium", also provides compensation for the lower liquidity of stocks relative to that of Treasury securities`. The companion time-series leg (H-2) is contemporaneous pain: `unexpected illiquidity has a negative and significant effect on contemporaneous stock return`, because higher realized illiquidity raises expected illiquidity and prices must fall for expected returns to rise. (All mechanism framing fenced to the paper's equity sample, never adopted as a crypto claim here.)

### Research interpretation

Expected-friction-regime holding, long-only, monthly cadence. Unlike return-conditioned momentum systems there is no formation total return and no winner/loser ranking: the position exists if and only if the trailing-year price-impact-per-notional sits at or above its own three-year median. Unlike volume-shock or volume-oscillator records raw volume never triggers anything — volume appears only as the denominator that converts an absolute move into a per-notional impact. Unlike the MAX lottery-avoidance record the direction mapping is inverted in spirit (hold the frictional regime for compensation, rather than avoid the spiky regime for underperformance) and the statistic is a 252-day mean, not a single-day extremum. The bet, as derived, is purely that the documented expected-illiquidity premium partition ports to BTCUSDT monthly bars — and the position absorbs the paper's own H-2 contemporaneous drawdown inside the regime with no guardrail.

## Signal

Exact rule as pinned (calendar-month evaluation; 252-bar ILLIQ window; 36-month median pool; month-end-close decision; next-bar-open fills; long-flat — any other month definition, return definition, volume definition, window, pool length, cutoff statistic, or tie rule is a different, unpinned rule):

- Bar grid: completed `1d` bars of BTCUSDT only. Evaluations occur at calendar month-ends in UTC (last bar dated in the month), in month order, one per month.
- Daily return (pinned): `r(t) = (C(t) − C(t−1)) / C(t−1)` on consecutive completed daily bars (`C` = close; simple, not log; close-to-close, never high/low/open-based). The first history bar carries no `r` (no predecessor — skipped, pinned).
- Daily dollar volume (pinned declared derivation): `DVOL(t) = C(t) × V(t)` where `V(t)` is the bar's base-asset volume, i.e. USDT notional traded (the venue's kline quote-volume field is the same quantity to tape precision; either field is the identical input, pinned to the product form). Venue-checked guards: closes are strictly positive on any traded tape, so no divide-by-zero branch can trigger; any bar with a non-positive close or a missing/non-positive `DVOL` is excluded from that month's average and the window still ends on the month's last bar (defensive pin, disclosed, never exercised on this venue — verified live 2026-10-14 that the venue's first three daily bars, 2017-08-17 onward, carry strictly positive closes and volumes).
- Monthly ILLIQ (pinned, paper eq. 1 ported bar-for-bar): `ILLIQ(M) = mean over exactly the 252 completed daily bars ending on month M's last bar of |r(t)| / DVOL(t)`. The paper multiplies by 10⁶ for display; this record computes the ratio unscaled — the factor is comparison-neutral under the median gate and is fenced as cosmetic, never a behavioral difference.
- Trailing pool (pinned declared derivation): `S(M) = {ILLIQ(M−36) … ILLIQ(M−1)}` — the 36 completed monthly values strictly preceding M.
- Cutoff (pinned median, no interpolation): `med(M)` = mean of the 18th and 19th smallest values of `S(M)` (even-count median, pinned; any other quantile is a different, unpinned rule).
- Position target (pinned, paper H-1 direction): the target for calendar month `M+1` is long iff `ILLIQ(M) ≥ med(M)` (weak inequality; the exact tie maps to long — measure-zero tie rule, pinned), else flat.
- Orders (pinned): at most one order event per month boundary, placed for the next month's first bar open (next-open fill after the month-end decision bar — the declared causal port; the paper ships no fill convention): flat→long target buys 100% equity at the first bar's open of month M+1; long→flat target closes all at the first bar's open of month M+1; unchanged target places nothing. No intrabar evaluation, no intrabar orders, no adds, no partials. Decisions on distinct month-ends fill on distinct month-opens — no same-bar dual-fire exists to sequence.
- Risk legs (pinned absence, not invented): the paper ships no stop/target/trailing concept for the illiquidity premium — the sole position-closing path is the regime exit to flat at a month-end close (filled next open). The derived posture is explicitly no stop, no target, no trailing, no opposite-signal exit, no calendar extension; a fully ridden within-regime slide is absorbed exactly as printed by construction.
- Direction: long-or-flat, derived-and-declared (the futures venue is still pinned as the research market under the house overlay with the short permission simply unused, and a spot-only deployment expresses the identical event set).

## Required data

- Completed `1d` bars of BTCUSDT only: `close` (daily `r`), `close × volume` (daily `DVOL`), `open` as fill price (no `high`, no `low`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, supply-feed, sentiment, macro, session-template, or cross-venue state gates any order). No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision grid: one evaluation per month at the last bar's close; fills land on the next month's first bar open. All inputs are completed-bar values — no provisional intrabar value is ever used.
- Warmup: flat until the month-end close at which the first computable target exists (the first computable target needs one 252-bar ILLIQ plus 36 trailing monthly ILLIQs = the 37th computable month-end) — structural, not conventional: the venue's 1d tape opens 2017-08-17 (verified live 2026-10-14 against the public spot kline feed), the 252nd daily bar prints 2018-04-25, the first computable month-end is 2018-04-30, the 37th is 2021-04-30, so the first position month is May 2021. No repainting, no negative shift, no future reference, no full-sample normalization (every ILLIQ is a trailing mean; the cutoff is a trailing median).

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared port of the paper's NYSE universe; no cross-venue equivalence claimed).
- Order timing (declared causal port; the paper ships no executable timing): month-end-bar-close decision with next-bar open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill is claimed. At most one order exists per month boundary, so there is no same-bar dual-fire to sequence.
- Cash leg: flat earns nothing by record rule. No T-bill, stablecoin-lending, funding-rebate, or synthetic yield is substituted; the paper's cost-free accounting accrues no cash yield to either regime.
- Sizing/capital/costs: fixed 100%-equity single position, no adds, no leverage (1×, no margin concept), no compounding concept beyond equity. The paper reports cost-free sample statistics, so derived evaluation must carry the explicit house overlay (pinned house fees plus historical funding treatment; no hypothetical zero funding claimed — long months carry realized funding, flat months carry none, and the form holds genuine flat stretches so it is never an always-in-position funding accumulator). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one long position at any time; month regimes are disjoint by calendar construction, so overlapping entries are structurally impossible (no ignore-rule needed beyond the single-position book); after any month-end exit the next month-end decision fires on schedule (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The unused short permission requires no margin-short modeling. Safety orders: explicitly none.

## Evidence

### Source-reported

The paper ships every adopted headline fact quoted in Provenance: the `|R|/VOLD`-averaged ILLIQ definition (eq. 1) with its Kyle-price-impact reading, the NYSE 1963–1997 CRSP design with its 200-day/$5/1%-tail admission rules, the 408-month Fama-MacBeth cross-section, the AR-forecast expected-market-illiquidity construction, and the H-1/H-2 time-series headline with its compensation conclusion. It ships zero adopted performance numbers for this record: every slope, t-statistic, R², and premium magnitude in the paper describes its equity sample, never a single-asset BTCUSDT derivative — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Cross-section fenced: every Fama-MacBeth slope, t-statistic, size/beta/dividend-yield control, and Table-I moment in the paper belongs to its 1963–1997 NYSE cross-section — none transfers to a single-asset crypto time-series rule, and none is adopted.
2. Number silence fenced: no slope, t-statistic, R², AR coefficient, premium magnitude, or sample-window moment from any paper table, equation fit, or figure is adopted anywhere — figures are omitted by rule, and any dispute over exact magnitudes is decided against this record, never patched by inference.
3. Window pin disclosed: the paper averages ILLIQ over annual (calendar-year, ~252-trading-day) characteristic windows and tests monthly FM cross-sections — it never trades a trailing-252-bar monthly-evaluated single-asset rule. The 252-bar window ports the paper's trading-year bar count; the monthly grid mirrors the paper's monthly test cadence; both are researcher-pinned, never paper conventions. Any other window, grid, or pool length would be a different, unpinned rule.
4. Return/volume-definition derivation disclosed: the paper's CRSP daily returns are distribution-inclusive equity returns and its dollar volume is share-volume × price; this record uses simple close-to-close crypto returns (BTC has no distributions) and `C×V` USDT notional (the venue's quote-volume field is the same quantity to tape precision). Skipped-day calendars differ (equity weekends/holidays versus the 24/7 tape) — fenced, never adjusted.
5. Expectation-model derivation disclosed: the paper's expected illiquidity is a fitted AR(1) forecast with bias-corrected coefficients — this record imports no fitted coefficient and estimates no regression. The trailing-36-month median is a nonparametric researcher-pinned expected-illiquidity partition, never the paper's AR forecast. Fitting an AR on this tape here would be a different, unpinned rule.
6. H-2 pain ridden by construction: the paper's own second leg says unexpected illiquidity depresses contemporaneous returns — this rule holds exactly through high-realized-ILLIQ months and absorbs those drawdowns to the next month-end close. The bet is purely the H-1 ex ante premium; the H-2 exposure is the coded trade, disclosed, not a tunable parameter here.
7. No-short, no-stop exposure disclosed: once long for a month, the position rides the entire adverse excursion with no guardrail — a −20% month inside an above-median hold is held to the next month-end close by construction.
8. Derivation boundary fenced: the only non-paper behavior is the six declared adaptations (single asset, calendar months plus close-to-close returns plus `C×V` notional, 252-bar/36-month median gate, next-open fills plus fixed sizing plus structural warmup plus house costs, long-flat mapping); the ILLIQ definition, the hold-when-illiquid direction, and the no-stop stance are source-faithful. This record is therefore never evidence that the paper's equity study passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: calendar-month evaluation / close-to-close `|r|` / `C×V` notional / 252-bar ILLIQ / 36-month median pool / tie-to-long / month-end-close decision / next-open fills / single-position long-flat / `1d` BTCUSDT are frozen.

- F1 — Sign relevance: an inverted twin (long iff `ILLIQ(M) < med(M)`, flat otherwise, same grid and fills) must not improve net expectancy; fail ⇒ the premium sign points the wrong way on this tape and the compensation read inverts.
- F2 — Ratio-vs-volume relevance: a raw-volume twin (long iff the trailing-252-bar mean `DVOL` sits at or above its own trailing-36-month median, same grid and fills) must not improve net expectancy; fail ⇒ the per-notional normalization adds nothing over a plain volume level and the paper's core construction is doing no work here.
- F3 — Ratio-vs-move relevance: an absolute-move twin (long iff the trailing-252-bar mean `|r|` sits at or above its own trailing-36-month median, same grid and fills) must not improve net expectancy; fail ⇒ the dollar-volume normalization adds nothing over raw move size and the impact interpretation is doing no work here.
- F4 — Selectivity relevance: buy-and-hold over the same sample must not improve net expectancy; fail ⇒ sitting out below-median liquefaction months costs more in missed drift than it saves — or the record's selectivity pin is doing unacknowledged work.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid month-end `1d` bar closes; fills at next-month first-bar opens; no venue-specific read). The arithmetic ports across perpetual venues without structural change (no corporate-action or calendar adjustment exists to recheck; quote-volume is the same notional to tape precision). No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. Extension to other house-universe assets, month definitions, return definitions, volume definitions, windows, pools, cutoffs, or timeframes would be a different, unpinned claim.

## Limitations

- Single-asset port: the paper's evidence is an equity market study (cross-section plus market time series); BTCUSDT illiquidity-regime behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Mechanism mismatch: whatever adverse-selection/inventory clientele sits behind the equity premium has no established crypto analogue (24/7 global tape, concentrated venues, perpetual-funding holders, stablecoin quote) — the port bets on regime persistence, not on a verified crypto mechanism.
- Median-rigidity: the trailing-36-month pool adapts slowly — a structural liquefaction (or desiccation) of the venue reprices the cutoff only as old months roll off; a permanently deep tape goes nearly always-flat, a permanently thin tape nearly always-long, both by construction.
- Month-definition rigidity: an illiquidity shock arriving across a month boundary is attributed to whole months; a first-of-month gap against the fresh regime is taken at the post-move open, never at the edge.
- Warmup cost: everything before the first computable-target month-end close (2021-04-30) is flat by record rule, so the 2017–2021 tape is deliberately untraded — pinned, not recovered.

## Implementation status

not-implemented. No Hummingbot controller/executor has been written for this record; the Execution assumptions section names the exact pinned engine path (package `20260920`, VERSION `dev-2.17.0`, month-end-close decision on completed `1d` bars, next-month-first-open market fills, single-asset 100%-equity 1× long-or-flat) that a future implementation must target, with representative event-level Qlib/Hummingbot parity required before any mass screening.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. PASS means the declared derived strategy is causally expressible under the pinned Hummingbot model — not profitable, not Qlib-paritied, not source-equivalent, not live-tradable.

## Related Wiki records

None.

## Sources

- Amihud, Yakov (2002). Illiquidity and stock returns: cross-section and time-series effects. Journal of Financial Markets 5(1), 31–56. https://doi.org/10.1016/S1386-4181(01)00024-6 (Crossref-verified 2026-10-14; openly hosted journal-text PDF https://www.cis.upenn.edu/~mkearns/finread/amihud.pdf fetched live 2026-10-14, 201,728-byte 26-page PDF, SHA-256 `349823bb…5f7118b`, read in full locally)
