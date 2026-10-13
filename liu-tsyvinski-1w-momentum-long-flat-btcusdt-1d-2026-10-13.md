---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Liu-Tsyvinski 2021 weekly time-series momentum 1-week long-flat on BTCUSDT 1d bars
created: 2026-10-13
updated: 2026-10-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2018-05-31
sources:
  - https://doi.org/10.1093/rfs/hhaa113
  - https://www.nber.org/papers/w24877
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Liu-Tsyvinski 2021 weekly time-series momentum 1-week long-flat on BTCUSDT 1d bars

## Provenance

Primary source identity verified end to end (Crossref record read firsthand 2026-10-13 confirming title, authors, journal, volume/issue/pages, and DOI; NBER working-paper PDF read firsthand the same evening — 68 pages — confirming authorship, sample, data source, timing convention, §4.1 method, Tables 14–18, and both calculation footnotes — all agree):

- Liu, Yukun & Tsyvinski, Aleh, `Risks and Returns of Cryptocurrency` — The Review of Financial Studies, vol. 34, no. 6, 2689–2727 (2021; published online 2020-09-26). DOI `10.1093/rfs/hhaa113`. Canonical DOI landing: https://doi.org/10.1093/rfs/hhaa113 (Oxford page paywalled at read time, so no claim is sourced from it beyond the Crossref-confirmed citation).
- Freely readable preprint lineage: NBER Working Paper 24877 (August 2018), https://www.nber.org/papers/w24877 — every method and number adopted below was read verbatim in this PDF.
- Pinned data (§2, read verbatim): `Cryptocurrency price data series are from the CoinDesk website. For Bitcoin, we use data from 01/01/2011 to 05/31/2018 because there was not much liquidity and trading in earlier years.` Returns throughout are log returns (realized volatility is `the sum of daily squared log returns from the previous month`; Table A.2 reports `Log Return`).
- Pinned execution timing (§4.1, read verbatim): `Specifically, the 1-week ahead weekly return is that of buying a Bitcoin at 11:59:59 UTD Sunday and selling at 11:59:59 UTD one week later` (`UTD` is the PDF text-layer rendering of the Sunday-midnight-UTC weekly boundary; the daily leg is analogously defined off the daily 23:59:59 boundary).
- Pinned weekly regression (Table 14 Panel B, read verbatim): current-week log return predicts 1/2/3/4-week-ahead returns with coefficients `0.19*** 0.22*** 0.21*** 0.09*` (t-statistics `(3.73) (4.52) (4.26) (1.72)`, bootstrapped `[2.17] [2.73] [2.47] [1.40]`, R-squared `0.03 0.05 0.05 0.01`). Footnote 10 pins the scale: `The 3.16 percent weekly return is calculated by multiplying one-standard-deviation increase of today's return (16.64 percent) and the coefficient estimate (0.19).`
- Pinned quintile sort (Table 15, read verbatim): `we estimate the time-series momentum by grouping weekly returns into quintiles and evaluating their performance going forward. We find that the top quintiles outperform the bottom quintiles at 1-4 week ahead horizons.` Headline 1-week-horizon cells: rank-5 formation `27.44` → `Rt+1 11.22*** (3.95) [Sharpe] 0.45`; rank-1 formation `-14.95` → `Rt+1 2.60* (1.69) 0.19`; `Difference 8.62`. The 3/4-week legs print rank-5 `10.07***` / `6.92**` against rank-1 `-0.50` / `1.73`.
- Pinned no-lookahead replication (Table 17 discussion, read verbatim): `we use the first two years of data to determine the quintile cutoffs and study the out-of-sample momentum performance, and we find strong momentum effect as well.` Its fixed-cutoff formation levels are Low `-14.97`, 2 `-2.88`, 3 `+1.77`, 4 `+8.12`, 5 `+24.14`; 1-week-horizon top `7.88** (2.70) 0.37` vs bottom `3.35* (1.82) 0.25`, `Difference 4.53`.
- Pinned robustness and heterogeneity (read verbatim, fenced where noted): Table 16 restricts to 2013 onward — `we find a strong and statistically significant momentum effect of somewhat smaller magnitude`; Table 18 — `For Ripple, the momentum effect is statistically significant at the 1-5 day horizon. For Ethereum, the momentum effect is statistically significant at the 1-day and 5-day horizons, with the 5-day horizon coefficient having a negative sign`, and the paper notes `for Ethereum, the momentum effect is less significant than for Bitcoin and Ripple`.
- Licence and rights: the RFS article is paywalled and the NBER paper is © 2018 by the authors — this record cites and normalizes the rule (short phrases and formulas only) and reproduces no figures, tables, or extended prose.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the paper's weekly time-series momentum (1-week formation, 1-week holding, Sunday-boundary turnover) ported to BTCUSDT Binance spot as a sequential weekly sign-split long-or-flat hold — not a lossless reproduction of the paper's CoinDesk-index study. Researcher-declared adaptations are exactly eight: (1) quintile-rank → zero sign split on the log weekly return (a live week has no peer distribution to rank against; the Table 17 fixed cutoffs are fenced off, never carried — the zero cut sits between that table's rank-2 `-2.88` and rank-3 `+1.77` levels by construction, declared here, never implied); (2) continuation-mapped-to-long / reversal-mapped-to-flat with the short permission explicitly unused (the paper reports both legs' forward returns; this record holds long only after up-weeks and flat after down-weeks — see Signal/Execution); (3) holding fixed at 1 week (the paper evaluates 1–4-week horizons; the headline `Rt+1` is adopted and the 2/3/4-week legs are fenced, never traded); (4) Bitcoin only (the Ripple/Ethereum legs, including Ethereum's negative 5-day coefficient, are fenced, never carried); (5) BTCUSDT Binance spot venue port (the source tape is the CoinDesk index 2011–2018; venue basis is disclosed, never equated); (6) Sunday-close decision with Monday-open fills (the paper turns over exactly at the Sunday 23:59:59 boundary; the sequential next-open fill is the declared causal port, never implied); (7) log-return formation read pinned source-faithful (the paper compounds log returns; sign(log) equals sign(simple) everywhere except the measure-zero exact-zero print, so the mapping is unaffected — disclosed, never implied); (8) the attention, price-to-dividend, volatility, and supply legs are dropped outright (Google/Twitter/wallet-user feeds have no pinned engine path and are explicitly not adopted — see Negative evidence 2).

Pre-write dedup (2026-10-13): working-tree case-insensitive filename sweeps for `liu`, `tsyvinski`, `heston`, `sadka`, `crypto-momentum`, `weekly-momentum`, `1-week`, `quintile`, `attention` return no strategy record — content hits for `momentum` are indicator records (adx/awesome-oscillator/chaikin/chande/keltner/pmo/pvo/qstick/rsi-divergence/stochastic-ott/vidya/waddah) plus the paper-family records compared line by line below. Closed-PR title scan (60 most recent) shows only #177 (Lehmann weekly REVERSAL — opposite mapping, see below), #179 (Novy-Marx 12-7), #180 (Jegadeesh-Titman 6/6), #170 (intraday half-hour) — no Liu, Tsyvinski, weekly-momentum, or quintile title. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak), #49 (Gaussian channel StochRSI breakout), #63 (SuperTrend ATR-flip), #89 (Chandelier Exit stop-flip), #92 (SSL channel reversal) — different mechanisms, indicators, and sources. Closest pool records differ in horizon, direction, or conditioning: `lehmann-1990-weekly-reversal-long-flat-btcusdt-1d-2026-10-13.md` fades the 1-week formation at the same weekly scale (opposite mapping by construction — the mirror twin this record falsifies against in F2); `jegadeesh-1990-monthly-reversal-long-flat-btcusdt-1d-2026-10-13.md` reverses a 1-month formation (4× longer window, opposite direction); `jegadeesh-titman-6m-6m-momentum-long-flat-btcusdt-1d-2026-10-13.md` and `novy-marx-12-7-intermediate-momentum-long-flat-btcusdt-1d-2026-10-13.md` trade with the past 6–12-month sign (26–52× longer formations on monthly grids — never a single-week sensor); `tsmom-12m-sign-monthly-long-btcusdt-1d-2026-10-10.md` holds a 12-month sign for one month; `debondt-thaler-36m-overreaction-long-flat-btcusdt-1d-2026-10-13.md` reverses a 36-month formation (∼156× longer, opposite direction); `george-hwang-52w-high-proximity-long-flat-btcusdt-1d-2026-10-13.md` reads a 52-week proximity level (never a weekly return sign); `bitcoin-intraday-first-last-halfhour-momentum-timing-two-sided-btcusdt-30m-2026-10-13.md` is intraday (same direction, ∼35× shorter clock); `monday-drift-weekly-calendar-hold-btcusdt-1h-2026-10-06.md` and `turn-of-month-4day-hold-long-btcusdt-1d-2026-10-10.md` are pure calendar holds with no return conditioning. No record in the pool conditions a 1-week hold on the sign of the immediately preceding single-week log return.

## Economic mechanism

### Source-reported

Crypto-native time-series continuation at short horizons: `there is a strong time-series momentum effect` in cryptocurrency returns — `significant time-series cryptocurrency momentum at the daily and weekly frequencies for all three cryptocurrencies` — with the weekly leg pinned to `the current return positively and statistically significantly predicts 1-week, 2-week, 3-week, and 4-week ahead returns` and the quintile mechanism that `the top quintiles outperform the bottom quintiles at 1-4 week ahead horizons` (`11.22 percent per week` top vs `2.60 percent per week` bottom at the 1-week horizon). The finding survives the post-2013 restriction (`somewhat smaller magnitude`) and the fixed-cutoff no-lookahead replication, and it is framed as crypto-specific: `only cryptocurrency market specific factors — momentum and the proxies for investor attention — consistently explain the variations of cryptocurrency returns` (all mechanism framing fenced to the paper's 2011–2018 CoinDesk sample, never adopted as a standing crypto claim here).

### Research interpretation

One-week clock continuation port: the single completed UTC week's log return is the whole sensor — a week that compounded above its own Sunday-midnight print earns the long book for the entire next week, a week that compounded at-or-below it earns nothing for the entire next week. There is no averaging, no second moment, no skip, no rank, and no cross-asset read anywhere: the strategy holds one posture per UTC week and the only thing that ever moves is the Sunday boundary. Unlike monthly-grid continuation (Jegadeesh-Titman 6/6, Novy-Marx 12-7, TSMOM-12m) the sensor integrates exactly one week, so a six-month-old trend is invisible — the record bets on weekly persistence, never on multi-month drift. Unlike same-scale reversal (Lehmann 1-week) the mapping is uninverted — past strength maps to long, past weakness maps to flat — so on any week where continuation and snapback disagree the two records print opposite postures by construction. Unlike level-regimes (George-Hwang 52-week proximity, Faber GTAA) or variance clocks (Moreira-Muir) the reference is the asset's own one-week compounding sign, never a moving average, never a high-water mark, never a second moment, never a calendar season. The bet, as derived, is purely on the paper's `top quintiles outperform the bottom quintiles` surviving the port to BTCUSDT at sequential weekly cadence with the up-week leg mapped to long and the down-week leg mapped to flat, never on an attention, supply, dividend, volatility, seasonal, band, oscillator, or funding anchor.

## Signal

Exact rule as pinned (1-week log return from Sunday closes, zero-threshold sign split with tie to flat, sequential non-overlapping UTC weeks — any other value is a different, unpinned rule):

- Week definition: UTC calendar weeks Monday 00:00:00 through Sunday 23:59:59. Decision bar: the last completed `1d` bar dated Sunday (UTC) of week W.
- Formation return (pinned source-faithful port of the paper's 1-week formation): `Rw_W = ln(C_W / C_{W-1})` where `C_W` is the close of the decision bar and `C_{W-1}` is the close of the last completed `1d` bar dated the preceding Sunday (8 Sunday closes spanning 7 full days only at the tape start; log read pinned by record rule where the paper compounds log returns; `C > 0` on any traded tape so the logarithm needs no zero-guard branch).
- Position target for the whole next UTC week W+1, Monday 00:00:00 through Sunday 23:59:59 (pinned sign split, tie to flat): `Rw_W > 0` (up-week — continuation bid) → long; `Rw_W <= 0` → flat. The `<=` spelling pins the measure-zero exact-zero print to flat with no second rule and no float-tolerance concept; no threshold constant exists anywhere in this record — zero is the record's declared quintile-rank substitute, frozen, never re-tuned.
- Skip (pinned, not a parameter): none — the paper sorts straight 1-week returns with no skip-a-week concept, and none is added here.
- Orders (pinned): at most one order event per weekly boundary, placed for the first `1d` open of week W+1 (Monday 00:00 UTC open — the declared causal port of the paper's Sunday-23:59:59 turnover): flat→long target buys 100% equity; long→flat target closes all; unchanged target places nothing. No intra-week evaluation, no intra-week orders, no adds, no partials, no second decision inside week W+1 for any reason including large adverse excursion.
- Risk legs (pinned absence, not invented): the paper ships no stop/target/trailing concept — the sole position-closing path is the next Sunday decision mapping to flat (a 1-week time exit). The derived posture is explicitly no stop, no target, no trailing; a full-week adverse move is ridden in full by construction.
- Direction: long-or-flat, derived-and-declared (the long maps the paper's top-quintile continuation; the flat maps the bottom-quintile leg with the short permission simply unused, and a spot-only deployment expresses the identical event set).

## Required data

- Completed `1d` bars of BTCUSDT only: daily `close` (formation arithmetic and settlement) and `open` as fill price only. No `high`/`low` range read, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, Google/Twitter attention, wallet-user counts, sentiment, macro, session-template, or cross-venue state gates any order. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision grid: Sunday UTC closes. One evaluation per week on the last completed daily bar dated Sunday; fills land on the next daily bar's open (Monday 00:00 UTC). All window inputs are completed-bar values — no provisional Sunday return is ever used.
- Warmup: two full UTC weeks of `1d` bars before the first position (the formation needs Sunday closes W−1..W). Bars before the second decidable Sunday are position-free by record rule; no signal before the third calendar week's Monday open may trade. No repainting, no negative shift, no future reference, no full-sample normalization, no rolling calibration window (the Table 17 two-year cutoff apparatus is fenced off with the quintile frame).

## Execution assumptions

- Research market: BTCUSDT Binance spot (declared port — spot is chosen deliberately so no funding leg exists to model; no CoinDesk-index equivalence claimed).
- Order timing (declared causal port of the paper's Sunday-boundary turnover cadence): Sunday completed-bar decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill is claimed. At most one order exists per weekly boundary, so there is no same-bar dual-fire to sequence.
- Cash leg: flat earns nothing by record rule. No T-bill, stablecoin-lending, funding-rebate, or synthetic yield is substituted; the paper's cost-free accounting accrues no cash yield to either leg.
- Sizing/capital/costs: fixed 100%-equity single position, no adds, no leverage (1×, no margin concept), no compounding concept beyond equity. The paper reports cost-free strategy returns, so derived evaluation must carry the explicit house overlay (pinned house spot fees on each weekly-boundary delta — up to 52 turnovers a year at full toggle; no funding leg exists on spot — and this record claims no hypothetical zero funding on any venue where funding would apply). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one long position at any time; re-entry after a flat week needs only the next up-week print (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic, no overlapping sleeves (the paper's quintile sleeves are replaced by the declared sequential single sleeve — see Limitations). The unused short permission requires no margin-short modeling.

## Evidence

### Source-reported

The paper ships every adopted construction fact: the CoinDesk BTC sample (01/01/2011–05/31/2018), the log-return read, the Sunday-boundary turnover definition, the Table 14 weekly predictive regression (`0.19***/0.22***/0.21***/0.09*` across 1–4 weeks), the Table 15 weekly quintile apparatus with the `11.22***` top / `2.60*` bottom 1-week cells and the `8.62` difference, the Table 16 post-2013 replication, and the Table 17 fixed-cutoff no-lookahead replication (`7.88**` top / `3.35*` bottom, `4.53` difference). It ships zero adopted performance numbers for this record: the quintile spreads, Sharpe ratios (0.45/0.19 headline, 0.37/0.25 no-lookahead), t-statistics, and regression R-squared values all describe the paper's CoinDesk-index quintile study, never a single-asset zero-cut BTCUSDT derivative — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Quintile frame fenced: every headline spread (8.62 headline, 4.53 no-lookahead, all Sharpe ratios and t-statistics) belongs to a across-time quintile sort — a live week cannot be quintiled against itself, and the zero cut adopted here is a strictly weaker, researcher-declared substitute with no source equivalence claim.
2. Attention legs dropped: the Google-search and Twitter-count predictors (`2.3 percent` 2-week and `2.50 percent` 1-week per standard deviation) require external point-in-time feeds with no demonstrated pinned-engine path — explicitly not adopted, never smuggled in as sentiment.
3. Supply/dividend/volatility legs dropped: the price-to-wallet-user ratio, realized-volatility, and supply proxies are separate paper findings with their own data dependencies — explicitly not adopted here.
4. Cross-coin heterogeneity fenced: Ethereum's 5-day coefficient is negative and its momentum `less significant than for Bitcoin and Ripple` — no finding transfers across coins, and this record adopts the Bitcoin leg only.
5. Post-2013 attenuation disclosed: the 2013-onward replication prints `somewhat smaller magnitude` (1-week top `7.18**` vs `11.22***` full-sample) — the edge the paper documents is sample-sensitive by its own report.
6. Daily leg fenced: the daily regression's 2-day (`-0.02`) and 7-day (`-0.03`) coefficients are negative-insignificant — this record trades the weekly headline only; no daily-timing claim is carried.
7. Mid-quintile weakness disclosed: the paper's rank-3 weeks (formation `+1.77`) earn an insignificant `1.15 (0.87)` 1-week forward — yet the zero cut maps every such small-up week to long. The flat-book edge, if any, concentrates in the tails the sign split cannot see; the dilution is declared, not hidden.
8. Cost silence fenced: the paper reports cost-free returns with no transaction-cost leg — at up to 52 boundary turnovers a year the derived evaluation must carry the full house spot-fee load, and this record reports no net performance of any kind.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 1-week log formation / zero sign split with tie to flat / sequential non-overlapping UTC weeks / Sunday-close decision / Monday-open fills / single-position long-or-flat 1× / turnover-only changes / `1d` BTCUSDT spot are frozen.

- F1 — Horizon relevance: replacing the pinned 1-week formation with a 4-week cumulative log formation on the identical Sunday grid must not improve net expectancy; fail ⇒ the single-week clock carries no advantage over the monthly clock on the same tape — or the weekly sensor is arbitrary resolution in disguise.
- F2 — Direction-of-mapping relevance: the perverse twin mapping long onto `Rw_W <= 0` (the Lehmann-direction fade twin) on the identical grid must not outperform the pinned continuation mapping; fail ⇒ the weekly sensor points the wrong way and the tape rewards fading past-week strength instead.
- F3 — Threshold relevance: replacing the pinned zero cut with a high-bar cut (`Rw_W > +0.02`, same grid, same tie convention) must not improve net expectancy; fail ⇒ the zero split is doing unacknowledged work as a hidden participation filter — or the tail-concentration story the source actually tells was flattened away by the sign split.
- F4 — Participation relevance: replacing the pinned long-or-flat posture with fixed full-size always-long buy-and-hold on the identical grid must not improve net expectancy while also not lowering realized volatility; fail on either clause ⇒ the up-week/flat gate is decoration — or flat weeks are the only thing working.

## Crypto portability

Pinned to BTCUSDT Binance spot (decision grid Sunday UTC closes on `1d` bars; log-return arithmetic with no venue-specific read). The arithmetic ports across spot venues without structural change — and the source asset is Bitcoin itself, so no cross-asset port is asserted beyond the CoinDesk-index→Binance-venue basis disclosed in Negative evidence 8 and Limitations. No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session template, no cross-venue state. The 24/7 crypto market has no closes/sessions for the rule to read (week membership is the UTC calendar date of the daily bar — deterministic on any continuously traded tape; the paper's own Sunday 23:59:59 boundary is itself a 24/7-tape convention). Extension to other house-universe assets, to the paper's 2/3/4-week holding legs, to the daily-formation leg, to a quintile-calibrated cut, or to the attention/supply/volatility legs would each be a different, unpinned claim.

## Limitations

- Single-sleeve port: the paper's evidence is a across-time quintile sort with fixed historical cutoffs in its no-lookahead leg; the live zero-cut single sleeve is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Cut substitution: the source's quintile membership is replaced by a single-asset sign split at zero; any distributional property tied to tail membership is lost by declared derivation, and replication disputes are decided against this record's pin, never patched silently.
- Researcher cut: the zero threshold, the 1-week/1-week windows, the Sunday grid, and the two-week warmup are record rules — the windows are source-pinned (1-week formation, `Rt+1` headline holding) but the cut, grid port, and warmup are declared choices, frozen, falsifiable, never re-tuned.
- Weekly posture: each UTC week holds one posture for its whole length; the flat-week opportunity cost and the long-week drawdown absorption are the record's principal risks, disclosed, not patched.
- Winner short abandoned: the source's bottom-quintile leg is mapped to flat, so any continuation-spread contribution from shorting down-weeks is deliberately left behind.
- Timing mismatch: the paper turns over exactly at Sunday 23:59:59 while this record fills at Monday 00:00 open — on gapping week boundaries the two fills differ, and the difference is a declared derivation boundary.
- No price stop, no intra-week exit: adverse excursion inside the holding week has no guardrail; the next decision is up to seven days away by construction. This is the source-faithful posture, disclosed as risk, not patched.
- Sample age: the source sample ends 05/31/2018 on the CoinDesk index; post-2018 microstructure, liquidity, and participant mix are outside every claim the paper makes — pinned, not recovered.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- https://doi.org/10.1093/rfs/hhaa113
- https://www.nber.org/papers/w24877
