---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Heston-Sadka 2008 seasonal same-month mean long-flat on BTCUSDT 1d bars
created: 2026-10-13
updated: 2026-10-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2002-12-31
sources:
  - https://doi.org/10.1016/j.jfineco.2007.02.003
  - https://w4.stern.nyu.edu/finance/docs/pdfs/Seminars/063f-sadka.pdf
  - https://ideas.repec.org/a/eee/jfinec/v87y2008i2p418-445.html
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Heston-Sadka 2008 seasonal same-month mean long-flat on BTCUSDT 1d bars

## Provenance

Primary source identity verified end to end (Crossref record read firsthand 2026-10-13 confirming title, authors, journal, volume/issue/pages, and DOI; NYU Stern working-paper PDF read firsthand the same evening — 55 pages, October 2006 version — confirming authorship, sample, CRSP tape, Eq. 1–10, Figure 2, Tables 1–4, and the §2–§5 method prose; RePEc IDEAS page read firsthand confirming the same citation — all agree):

- Heston, Steven L. & Sadka, Ronnie, `Seasonality in the Cross-Section of Stock Returns` — Journal of Financial Economics, vol. 87, no. 2, 418–445 (February 2008). DOI `10.1016/j.jfineco.2007.02.003`. Canonical DOI landing: https://doi.org/10.1016/j.jfineco.2007.02.003 (paywalled at read time, so no method or number is sourced from it beyond the Crossref-confirmed citation).
- Freely readable preprint lineage: October 2006 working paper, https://w4.stern.nyu.edu/finance/docs/pdfs/Seminars/063f-sadka.pdf — every method and number adopted below was read verbatim in this PDF (SSRN lineage `10.2139/ssrn.687022` noted for provenance only; no claim is sourced from it).
- Pinned sample (§1, read verbatim): `This paper calculates returns on portfolio strategies over the years 1965-2002. Our sample includes NYSE/AMEX-listed firms whose data is available on the CRSP monthly returns file.` Long-lag legs use `stock returns back to January 1945`; `Over 500 firms had 20 years of return history over all years of our relevant sample, and over 1,000 firms had at least 10 years of history by 1999.`
- Pinned seasonal model (§1/§3, read verbatim): `μit = μit+12` — `particular stocks may have distinctly high or low expected returns every 12 months`; `we allow them to differ across calendar months but assume they are constant across the same calendar month in different years`.
- Pinned trading illustration (§1, read verbatim): `form winner-loser decile spreads based on seasonal returns in previous years. For example, we would buy and hold stocks in April of a particular year if their average returns were in the upper 10% of all stocks' returns over previous Aprils.`
- Pinned formation grid (§2, read verbatim): `We form decile portfolios based on the average monthly return of stocks over all months in each lagged interval and measure the returns over the next month. For example, the 2–5 year winner portfolio held in January 2003 would be an equally weighted combination of stocks that had the highest average return from January 1998 to December 2001.` Annual-lag legs sort `only on annual lags 12, 24, …, 240` (noncontiguous same-month lags) vs non-annual lags.
- Pinned headline spreads (Table 2 discussion, read verbatim): year-1 all-months decile 10 minus decile 1 `146 basis points per month`; 12-month-lag alone `115 basis points` with the note `the t-statistic for this 12-month winner-loser strategy exceeds the t-statistic for the full-year strategy, indicating it produces a higher Sharpe ratio`; years 2–5 all-months `-107 basis points per month`, but annual lags 24/36/48/60 alone `67 basis points` positive; years 6–10 `68 basis points`, years 11–15 `66 basis points`, years 16–20 `52 basis points` (`All these returns are statistically significant at conventional levels`); `average winner-loser returns based on non-annual months are negative for all formation intervals`.
- Pinned periodicity (Figure 2 / Table 1 discussion, read verbatim): positive `pulses at annual intervals from 12 to 240 months`; `all the annual return effects are statistically positive at the 95% level for the first 10 years of lags` (univariate 20-year lag t-statistic `2.99`, multivariate `1.47`; multivariate t exceeding 2 at lags 14–16 years).
- Pinned magnitude (§3/Table 3, read verbatim): all-months variance estimate `small, and statistically insignificant at -0.0009% per month`, but annual-lag estimate `1.33 basis points` implying `the implied cross-sectional standard deviation of expected stock returns is 1.15% per month` and `equivalent annualized standard deviation … 13.8%`, against a CAPM-benchmark `1.86%` (`0.31` beta dispersion × `6%` premium) — `over seven times as large`.
- Pinned attribution (Table 4 discussion, read verbatim): all-months mean adjustment `does not substantially alter the profitability of annual strategies`, but `adjusting the means using seasonal estimates sharply reduces the magnitude of the one-year annual effect and eliminates the statistical significance of profits beyond one year` — `entirely explained by seasonal variation in individual stock returns`.
- Pinned turnover caveat (§1, read verbatim): `While the returns are large on an annualized basis, they last for only one month and may not justify 100% portfolio turnover.`
- Licence and rights: the JFE article is paywalled and the working paper is © by the authors — this record cites and normalizes the rule (short phrases and formulas only) and reproduces no figures, tables, or extended prose.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the paper's same-calendar-month seasonal sensor ported to BTCUSDT Binance spot as a sequential monthly mean-sign long-or-flat hold — not a lossless reproduction of the paper's NYSE/AMEX CRSP cross-sectional decile study. Researcher-declared adaptations are exactly eight: (1) cross-sectional decile rank → single-asset same-month mean sign split at zero (a live month has no peer distribution to rank against; the zero cut is the declared decile substitute, frozen, never re-tuned); (2) winner-long/loser-short → long-or-flat with the short permission explicitly unused (the paper reports both legs' forward spreads; this record holds long only when the seasonal mean is positive and flat otherwise — see Signal/Execution); (3) multi-window annual-lag apparatus (single 12-month lag; 24/36/48/60 average; 6–10/11–15/16–20 averages; up to 240-month evidence) → frozen 5-prior-same-month mean with a minimum-3-observations rule (see Signal); (4) NYSE/AMEX CRSP monthly tape 1965–2002 → BTCUSDT Binance spot venue port with months derived from `1d` bars (venue and tape basis disclosed, never equated); (5) CRSP month-end turnover → last-daily-close decision with next-month-first-open fills (the declared causal port, never implied); (6) simple monthly-return read kept source-faithful (`C_end/C_start − 1` on month-boundary closes; the CRSP file ships simple returns and the §2 sorts average monthly returns — no log substitution is made here); (7) volume/volatility/size/industry/earnings/dividend/universal-calendar/fiscal-year legs dropped outright (§4–§5 findings have no pinned single-asset engine path as signals and are explicitly not adopted — see Negative evidence); (8) holding fixed at one full calendar month (the paper measures `returns over the next month`; its 20-year persistence is an evidence horizon across repeated monthly holds, never a multi-year buy-and-hold — fenced, never traded).

Pre-write dedup (2026-10-13): working-tree case-insensitive filename sweeps for `heston`, `sadka`, `seasonal`, `same-month`, `same-calendar`, `annual-lag` return no strategy record — content hits for `seasonal`/`calendar` are the universal-calendar records compared line by line below. Closed-PR title scan (60 most recent, #125–#184) shows only #162 (January Barometer), #161 (Santa Claus), #173 (pre-holiday), #172 (FOMC pre-drift), #170 (intraday half-hour), #176/#177 (Jegadeesh/Lehmann), #178/#171 (BLL), #179/#180/#181/#182/#183/#184 (Novy-Marx/JT/George-Hwang/Moreira-Muir/DeBT/Liu) — no Heston, Sadka, seasonal, or same-month title. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak), #49 (Gaussian channel StochRSI breakout), #63 (SuperTrend ATR-flip), #89 (Chandelier Exit stop-flip), #92 (SSL channel reversal) — different mechanisms, indicators, and sources. Closest pool records differ in sensor, grid, or conditioning: `january-barometer-conditional-annual-hold-long-btcusdt-1d-2026-10-12.md` conditions a full-year posture on January alone (one annual gate, never twelve independent monthly sensors); `santa-claus-rally-yearend-hold-long-btcusdt-1d-2026-10-12.md`, `sell-in-may-seasonal-hold-long-btcusdt-1d-2026-10-10.md`, `turn-of-month-4day-hold-long-btcusdt-1d-2026-10-10.md`, `monday-drift-weekly-calendar-hold-btcusdt-1h-2026-10-06.md`, `pre-holiday-drift-scheduled-preclosure-hold-long-btcusdt-1d-2026-10-13.md`, `fomc-pre-announcement-drift-scheduled-hold-long-btcusdt-1d-2026-10-13.md`, `lunar-phase-new-moon-regime-long-flat-btcusdt-1d-2026-10-13.md` all trade fixed universal-calendar windows identical for every asset (never the asset's own same-month history); `jegadeesh-titman-6m-6m-momentum-long-flat-btcusdt-1d-2026-10-13.md`, `novy-marx-12-7-intermediate-momentum-long-flat-btcusdt-1d-2026-10-13.md`, `tsmom-12m-sign-monthly-long-btcusdt-1d-2026-10-10.md`, `liu-tsyvinski-1w-momentum-long-flat-btcusdt-1d-2026-10-13.md` sort contiguous trailing formations (never noncontiguous same-month lags); `jegadeesh-1990-monthly-reversal-long-flat-btcusdt-1d-2026-10-13.md` and `lehmann-1990-weekly-reversal-long-flat-btcusdt-1d-2026-10-13.md` fade the immediately prior month/week (nearest lag, opposite seasonal construction); `debondt-thaler-36m-overreaction-long-flat-btcusdt-1d-2026-10-13.md` reverses a contiguous 36-month formation; `george-hwang-52w-high-proximity-long-flat-btcusdt-1d-2026-10-13.md` reads a proximity level; `faber-gtaa-10m-sma-monthly-regime-long-flat-btcusdt-1d-2026-10-13.md` reads a 10-month average level; `bll-vma-1-200-percent-band-two-sided-btcusdt-1d-2026-10-13.md` / `bll-trb-200-percent-band-fixed-10d-two-sided-btcusdt-1d-2026-10-13.md` read moving-average/band breaks; `moreira-muir-volatility-managed-long-only-btcusdt-1d-2026-10-13.md` scales by trailing variance; `bitcoin-intraday-first-last-halfhour-momentum-timing-two-sided-btcusdt-30m-2026-10-13.md` times intraday halves — none averages prior same-calendar-month returns.

## Economic mechanism

### Source-reported

Asset-specific calendar-month persistence: `Stocks with relatively high (low) returns tend to have high (low) returns every year in the same calendar month`, recognized as `part of a general pattern that lasts up to 20 annual lags, superimposed on the general momentum/reversal patterns`, with `winners outperforming losers at annual intervals for up to 20 years, while underperforming in between`. The paper frames it as `a persistent seasonal effect in stock returns` consistent with `large cross-sectional variation in average returns that depends on the calendar month` (Conrad-Kaul interpretation), explains `an economically and statistically significant magnitude of the cross-sectional variation in average stock returns`, and stresses the seasonal attribution: `profits vanish when returns are demeaned seasonally`, `entirely explained by seasonal variation in individual stock returns`, `independent of size, industry, earnings announcements, dividends, and fiscal year`, while `Volume and volatility exhibit similar seasonal patterns but they do not explain the seasonality in returns` (all mechanism framing fenced to the paper's 1965–2002 CRSP sample, never adopted as a standing crypto claim here).

### Research interpretation

Twelve independent monthly clocks, one asset: each calendar month owns its own sensor built only from that same month's completed history — January's posture comes only from prior Januarys, February's only from prior Februarys, and so on. A month whose own past prints compounded positive on average earns the long book for its whole length; a month whose own past averaged at-or-below zero earns nothing. There is no trailing trend, no moving average, no band, no oscillator, no variance read, and no cross-asset rank anywhere: the strategy holds one posture per calendar month and the only thing that ever moves is the month boundary. Unlike contiguous-formation continuation (Jegadeesh-Titman 6/6, Novy-Marx 12-7, TSMOM-12m, Liu weekly) the sensor integrates noncontiguous same-month lags (12/24/36/48/60-month anniversaries, never the months in between) — a six-month-old rally is invisible unless it fell in the same calendar month. Unlike nearest-lag reversal (Lehmann weekly, Jegadeesh monthly) the construction skips the adjacent months entirely — the most recent input is twelve months old by design. Unlike universal-calendar bets (January Barometer, Santa, Sell-in-May, turn-of-month, Monday drift, FOMC/pre-holiday, lunar) no month is structurally long or flat — every month's posture is earned by its own history and can flip across years as that history accrues. The bet, as derived, is purely on the paper's `top quintiles outperform the bottom quintiles`-analog seasonal persistence surviving the port to BTCUSDT at sequential monthly cadence with up-seasonal months mapped to long and down-seasonal months to flat, never on a size, value, liquidity, attention, volatility, band, or funding anchor.

## Signal

Exact rule as pinned (5-prior same-month simple-return mean, zero-threshold sign split with tie to flat, sequential non-overlapping UTC calendar months — any other value is a different, unpinned rule):

- Month definition: UTC calendar months; a bar belongs to the month of its UTC date. Decision bar for upcoming month M=(y,m): the last completed `1d` bar dated in the preceding calendar month.
- Monthly return (source-faithful simple read): `R_{Y,m} = C_{Y,m} / C_{Y,m-1} − 1` where `C_{Y,m}` is the close of the last completed `1d` bar dated in month (Y,m) and `C_{Y,m-1}` is the close of the last completed `1d` bar dated in the preceding calendar month. `C > 0` on any traded tape so the division needs no zero-guard branch. A month return is defined only when both boundary closes exist; the tape-start month (no prior close) is undefined and excluded by record rule.
- Seasonal sensor for month M=(y,m) (declared derivation of the paper's previous-Aprils average): `S_{y,m} = mean(R_{y−k,m} for k = 1..5, restricted to defined completed same-month returns)`, requiring at least 3 defined observations — otherwise there is no signal and the month maps to flat by record rule. All inputs are fully completed months; the most recent admissible input is the same month one year earlier, so the minimum information lag is twelve months minus month-boundary alignment — causal by construction with an eleven-month gap to any contiguous-formation sensor.
- Position target for the whole calendar month M (pinned sign split, tie to flat): `S_{y,m} > 0` (up-seasonal — seasonal bid) → long; `S_{y,m} <= 0` or undefined (fewer than 3 observations) → flat. The `<=` spelling pins the measure-zero exact-zero print to flat with no second rule and no float-tolerance concept; no threshold constant exists anywhere in this record — zero is the record's declared decile-rank substitute, frozen, never re-tuned.
- Skip (by construction, not a parameter): all non-annual lags are skipped — the sensor never reads the 1–11 months immediately preceding M.
- Orders (pinned): at most one order event per month boundary, placed for the first `1d` open of month M (day-1 00:00 UTC open — the declared causal port of the paper's month-end turnover): flat→long target buys 100% equity; long→flat target closes all; unchanged target places nothing. No intra-month evaluation, no intra-month orders, no adds, no partials, no second decision inside M for any reason including large adverse excursion.
- Risk legs (pinned absence, not invented): the paper ships no stop/target/trailing concept — the sole position-closing path is the next month-boundary decision mapping to flat (a 1-month time exit). The derived posture is explicitly no stop, no target, no trailing; a full-month adverse move is ridden in full by construction.
- Direction: long-or-flat, derived-and-declared (the long maps the paper's winner leg; the flat maps the loser leg with the short permission simply unused, and a spot-only deployment expresses the identical event set).

## Required data

- Completed `1d` bars of BTCUSDT only: daily `close` (month-boundary arithmetic and settlement) and `open` as fill price only. No `high`/`low` range read, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, attention, sentiment, macro, earnings, dividend, fiscal-year, session-template, or cross-venue state gates any order. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision grid: month-end UTC closes. One evaluation per month on the last completed daily bar of the preceding month; fills land on the next daily bar's open (day-1 00:00 UTC of month M). All window inputs are completed-month values — no provisional month return is ever used.
- Warmup: months before the first signal-eligible month are position-free by record rule. General rule (≥3 defined same-month histories over the 5-prior window) governs every month including tape start and any later data gap; a month with missing boundary closes contributes no return and cannot count toward the 3. On the Binance BTCUSDT tape (tradable history opening August 2017, whose own August return is undefined for lack of a July close), the earliest satisfiable month is September 2020 (September 2017/2018/2019 complete) — every calendar month before its own third history is flat by the same rule, with January-type months first eligible in 2021. No repainting, no negative shift, no future reference, no full-sample normalization, no rolling calibration window.

## Execution assumptions

- Research market: BTCUSDT Binance spot (declared port — spot is chosen deliberately so no funding leg exists to model; no CRSP-index equivalence claimed).
- Order timing (declared causal port of the paper's month-end turnover cadence): month-end completed-bar decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill is claimed. At most one order exists per month boundary, so there is no same-bar dual-fire to sequence.
- Cash leg: flat earns nothing by record rule. No T-bill, stablecoin-lending, funding-rebate, or synthetic yield is substituted; the paper's cost-free accounting accrues no cash yield to either leg.
- Sizing/capital/costs: fixed 100%-equity single position, no adds, no leverage (1×, no margin concept), no compounding concept beyond equity. The paper reports cost-free strategy returns, so derived evaluation must carry the explicit house overlay (pinned house spot fees on each month-boundary delta — up to 12 turnovers a year at full toggle; no funding leg exists on spot — and this record claims no hypothetical zero funding on any venue where funding would apply). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one long position at any time; re-entry after a flat month needs only the next up-seasonal print (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic, no overlapping sleeves (the paper's decile sleeves are replaced by the declared sequential single sleeve — see Limitations). The unused short permission requires no margin-short modeling.

## Evidence

### Source-reported

The paper ships every adopted construction fact: the CRSP NYSE/AMEX 1965–2002 sample (lags to 1945; 500+ 20-year-history firms), the seasonal model `μit = μit+12`, the previous-calendar-months decile illustration, the §2 formation grid (all-months vs annual-lag 12/24/…/240 vs non-annual sorts), the Figure 2 annual pulses (12–240 months) with Table 1 significance through 10 annual lags, the Table 2 headline spreads (year-1 all-months `146bp`, 12-lag alone `115bp` at higher Sharpe; years 2–5 annual `67bp` against all-months `−107bp`; 6–10 `68bp`; 11–15 `66bp`; 16–20 `52bp`, significant; non-annual negative throughout), the Table 3 variance magnitudes (`−0.0009%` all-months vs `1.33bp` annual → `1.15%/mo`, `13.8%` annualized, `7×` the CAPM `1.86%` benchmark), the Table 4 seasonal-demeaning attribution, and the one-month-hold/100%-turnover caveat. It ships zero adopted performance numbers for this record: the decile spreads, t-statistics, Sharpe comparison, and variance decompositions all describe the paper's CRSP cross-sectional decile study, never a single-asset zero-cut BTCUSDT derivative — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Decile frame fenced: every headline spread (146bp, 115bp, 67/68/66/52bp, −107bp all-months, variance and Sharpe comparisons) belongs to an across-stocks decile sort — a live month cannot be deciled against itself, and the zero-cut mean split adopted here is a strictly weaker, researcher-declared substitute with no source equivalence claim.
2. Cross-sectional short leg abandoned: the source's loser-short contribution is mapped to flat, so any seasonal-spread contribution from shorting down-seasonal months is deliberately left behind.
3. Window choice declared: the source spreads its evidence across a single 12-month lag and 4/5-lag annual averages out to 20 years; the frozen 5-prior/ minimum-3 rule is a researcher compromise for a short crypto tape with no source optimality claim — early BTC signals rest on 3 observations where the paper averages 4–5, with higher sampling variance disclosed, not hidden.
4. Universal-calendar effects fenced: Keim/Reinganum January-size and Tinic-West January-beta effects surveyed in the paper are cross-sectional January tilts, never twelve independent monthly sensors — no universal long-January, long-December, or Halloween-window claim is carried here.
5. Volume/volatility legs dropped: §4 finds `similar seasonal patterns` in volume and volatility but they `do not explain the seasonality in returns` — explicitly not adopted as signals, never smuggled in as activity filters.
6. Size/industry/earnings/dividend/fiscal-year robustness fenced: §5 independence results are validity checks on the paper's sample, not portable signals — explicitly not adopted here.
7. Turnover economics disclosed: the paper warns one-month profits `may not justify 100% portfolio turnover`; this derivative turns over at most 12 times a year (vs the paper's monthly 100% two-sided churn) yet must still carry the full house spot-fee load — and this record reports no net performance of any kind.
8. Sample age and venue fenced: the source sample ends December 2002 on US equities; post-2002 microstructure and all crypto market structure, liquidity, and participant mix are outside every claim the paper makes — pinned, not recovered.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 5-prior same-month simple-mean / minimum-3 / zero sign split with tie to flat / sequential non-overlapping UTC months / month-end-close decision / next-month-first-open fills / single-position long-or-flat 1× / turnover-only changes / `1d` BTCUSDT spot are frozen.

- F1 — Seasonality relevance: replacing the pinned same-month mean with a contiguous trailing-12-month mean on the identical month-end grid must not improve net expectancy; fail ⇒ the same-month clock carries no advantage over the buy-and-hold-drift clock on the same tape — or the seasonal sensor is arbitrary resolution in disguise.
- F2 — Direction-of-mapping relevance: the perverse twin mapping long onto `S_{y,m} <= 0` (the fade-seasonal twin) on the identical grid must not outperform the pinned seasonal mapping; fail ⇒ the seasonal sensor points the wrong way and the tape rewards fading own-month history instead.
- F3 — Threshold relevance: replacing the pinned zero cut with a high-bar cut (`S_{y,m} > +0.02`, same grid, same tie convention, same minimum-3) must not improve net expectancy; fail ⇒ the zero split is doing unacknowledged work as a hidden participation filter — or the tail-concentration story the decile source actually tells was flattened away by the sign split.
- F4 — Participation relevance: replacing the pinned long-or-flat posture with fixed full-size always-long buy-and-hold on the identical grid must not improve net expectancy while also not lowering realized volatility; fail on either clause ⇒ the seasonal gate is decoration — or flat months are the only thing working.

## Crypto portability

Pinned to BTCUSDT Binance spot (decision grid month-end UTC closes on `1d` bars; simple-return month arithmetic with no venue-specific read). The arithmetic ports across spot venues without structural change — the source asset class (US equities) is never equated to crypto beyond the disclosed venue-basis port. No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session template, no cross-venue state. The 24/7 crypto market has no closes/sessions for the rule to read (month membership is the UTC calendar date of the daily bar — deterministic on any continuously traded tape; the CRSP month is itself a calendar convention). Partial first/last tape months contribute only when both boundary closes exist, by record rule. Extension to other house-universe assets, to other lookbacks (3/10/20 same-months), to a decile-calibrated cut, to a volume-gated seasonal, or to any universal-calendar overlay would each be a different, unpinned claim.

## Limitations

- Single-sensor port: the paper's evidence is an across-stocks decile sort with up to 20 annual lags; the live same-month-mean single sleeve is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Cut substitution: the source's decile membership is replaced by a single-asset mean-sign split at zero; any distributional property tied to tail membership is lost by declared derivation, and replication disputes are decided against this record's pin, never patched silently.
- Researcher window: the 5-prior/minimum-3 rule, the zero threshold, the month grid, and the warmup are record rules — the same-month construction is source-pinned but the depth, cut, grid port, and warmup are declared choices, frozen, falsifiable, never re-tuned.
- Monthly posture: each UTC month holds one posture for its whole length; the flat-month opportunity cost and the long-month drawdown absorption are the record's principal risks, disclosed, not patched.
- Loser short abandoned: the source's bottom-decile leg is mapped to flat, so any seasonal-spread contribution from shorting down-seasonal months is deliberately left behind.
- Timing mismatch: the CRSP study turns over at month-end prints while this record fills at the next month's first daily open — on gapping month boundaries the two fills differ, and the difference is a declared derivation boundary.
- No price stop, no intra-month exit: adverse excursion inside the holding month has no guardrail; the next decision is up to 31 days away by construction. This is the source-faithful posture, disclosed as risk, not patched.
- Sample age and short tape: the source sample ends 12/31/2002 on US equities while BTCUSDT contributes at most a handful of same-month histories per month — early signals are high-variance by construction, and post-2002/cross-asset transfer is outside every source claim.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- https://doi.org/10.1016/j.jfineco.2007.02.003
- https://w4.stern.nyu.edu/finance/docs/pdfs/Seminars/063f-sadka.pdf
- https://ideas.repec.org/a/eee/jfinec/v87y2008i2p418-445.html
