---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Caporale-Plastun one-day abnormal-return day-momentum Strategy 1 two-sided on BTCUSDT 1h bars
created: 2026-10-16
updated: 2026-10-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2020-05-27
sources:
  - https://doi.org/10.1007/s11408-020-00357-1
  - https://bura.brunel.ac.uk/bitstream/2438/20686/6/FullText.pdf
  - https://www.econstor.eu/bitstream/10419/175075/1/1013722922.pdf
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Caporale-Plastun one-day abnormal-return day-momentum Strategy 1 two-sided on BTCUSDT 1h bars

## Provenance

Primary sources read end to end during this cycle (2026-10-16), pinned:

- Journal paper (open access, CC-BY 4.0, Brunel repository copy fetched live this cycle, 291978 bytes, SHA-256 `31b92c06a3137606db91e355427063ae7dcd23ee88348a20be701e40cfcbe863`, 16 PDF pages / 8 journal pages, read end to end): `Caporale, Guglielmo Maria & Plastun, Alex (2020)`, `Momentum effects in the cryptocurrency market after one-day abnormal returns`, `Financial Markets and Portfolio Management 34:251–266`, DOI `10.1007/s11408-020-00357-1`, published online `2020-05-27` (record `source_as_of` is that publication date, never the fetch date). Sample per Abstract and §3: `BTCUSD, ETHUSD and LTCUSD` over `01.01.2015–01.09.2019`, daily plus hourly data from `CoinMarketCap`, `Gemini` and `Bitstamp`. Method (§3, journal p.255): returns `Ri = (Closei/Openi − 1) × 100%` as eq. (1) (`In order to avoid the distortions caused by price gaps`), abnormal-day triggers `Ri > (R̄n + k × δn)` as eq. (2) and `Ri < (R̄n − k × δn)` as eq. (3), `where k is the number of standard deviations used to identify the abnormal returns (k = 2 for BTCUSD and k = 1.5 for ETHUSD and LTCUSD, k being chosen on the basis of the sample size to generate in each case a sufficient number of detected abnormal returns)`; `R̄n` is `the average size of daily returns for period n` as eq. (4) and `δn` is `the standard deviation of daily returns for period n` as eq. (5) with the population `1/n` divisor. `A day consists of 24 h` (§3, p.256). Trading simulation `does not incorporate transaction costs such as spreads, broker or bank fees and swaps and therefore is only a proxy for actual trading` (§3, pp.256–257). Detection timing (§4, p.259): `abnormal returns are detected not at the end of the day, but during the day (the size of current daily return exceeds the abnormal returns benchmark)`, and `traders have sufficient time to exploit these patterns by opening a position in the direction of the abnormal returns immediately after this is detected`. Average CAR detection timings for BTCUSD: positive after `18:00`, negative after `16:00` (Tables 2–3, pp.259–260; §4 text: `positive abnormal return are detected after 6 pm and negative ones after 4 pm`). Strategy rule (§4, p.260, verbatim): `Strategy 1 When it becomes clear that the current day is an abnormal returns day (see the timing of abnormal returns in Tables 2 and 3), a position in the direction of abnormal returns should be opened. This position should then be closed at the end of the day.` Source-reported Strategy 1 BTCUSD simulation (Table 4, p.261, positive: `49` trades / `42` successful / `86%` / total `143.11%` / per-year `28.62%` / per-trade `2.92%` / t `6.62` / null `Rejected`; Table 5, p.262, negative: `46` / `42` / `91%` / `202.41%` / `40.48%` / `4.40%` / t `8.21` / null `Rejected`).
- Companion lineage paper (same authors, same dynamic-trigger family; read §4 plus Table 1 this cycle via the open EconStor copy of DIW Berlin Discussion Paper No. 1718, fetched live, 939439 bytes, SHA-256 `5aa8e1f952c7e0c71fffde03818b22b6cb0d14797f53a9a4cc1b72f060356d09`): `Caporale & Plastun (2018)`, `Price overreactions in the cryptocurrency market` (journal version `Journal of Economic Studies 46(5):1137–1155`, DOI `10.1108/jes-09-2018-0310`, cited in the 2020 paper's references). §4 tests averaging periods `5, 10, 20, 30, 40 and 50`; Table 1 usable-day counts print `1600 / 1595 / 1585 / 1575 / 1565 / 1555` (falling by exactly the window increment — consistent with a trailing window that excludes the evaluated day); text conclusion: `The results provide evidence in favour of 30 as an appropriate value for the averaging period`. This 30-calibration was produced under a contrarian next-day test with high/low-amplitude returns and `k = 1` — fenced as supporting evidence for the research freeze, never claimed as the 2020 paper's print (see Negative evidence 1).

Licence and rights: the 2020 article is CC-BY 4.0 open access. This record cites and normalizes the rule (short quoted declarations only for gate evidence) and reproduces no source block beyond single-line facts.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the paper's simulation. The paper prints the trigger formulas, `k = 2` for BTCUSD, the direction mapping, and the end-of-day exit, but never mechanizes the intraday detection clock, never states the averaging window `n` numerically, never names a venue/timeframe/fill convention, and carries no risk leg. Researcher-declared adaptations are exactly seven: (1) research market `BTCUSDT` Binance USDT-M perpetual `1h` (the paper studies BTCUSD spot — venue/frame pin disclosed, never a source claim; perpetual is required because the short leg needs margin); (2) averaging window frozen at `n = 30` completed UTC days (the 2020 paper prints no numeral; the freeze follows the companion calibration above — disclosed, never paper text); (3) the `becomes clear` detection discretized as first completed-`1h`-bar breach of the band with next-bar-open fills (the paper detects `during the day` when `the size of current daily return exceeds the abnormal returns benchmark` but ships no executable clock — deviation class identical to the admitted holmberg-orb record's continuous→bar-touch port, disclosed, never an advantage claim); (4) trading day = UTC day with exit decided at the `23:00–00:00 UTC` bar close and filled at the `00:00 UTC` open (the paper closes `at the end of the day` with no fill convention); (5) final-bar void — a first breach occurring only on the `23:00–00:00 UTC` bar yields no entry (no bar remains for a non-degenerate hold); (6) explicit single-unit pin with repeat same-day signals as no-ops and no stop/target/trailing/time leg beyond the day-end exit (the paper's algorithm contains no risk leg — carried over exactly, never upgraded); (7) house sizing/costs with modeled funding while held (the paper's cost-free accounting is recorded as absent portable economics, never as evidence; funding is never zero-claimed). The open-to-close return definition, the population-`1/n` band estimator, the `k = 2` BTCUSD threshold, the directional-momentum mapping, and the day-end exit are source-pinned.

Pre-write dedup (2026-10-16): working-tree case-insensitive searches for `caporale`, `plastun`, `abnormal-return-day`, `abnormal day momentum`, `closei/openi` return zero strategy records using this source, sample, or trailing-mean±kσ daily-return-band construction (`abnormal` hits elsewhere are fencing prose inside otherwise-named records — Jegadeesh/Lehmann decile-spread framing, TSMOM abnormal-return accounting, P-Signal parameter sensitivity, pre-holiday abstract corroboration — never order-gating lines; `open-to-close` hits are the holmberg day-anchor, IMI/QStick background prose; `mean±sigma` hits are price-level bands — GKV-VWMA, linreg channel — never a return-space event band). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Closest pool record `holmberg-orb-normal-tail` (merged 2026-10-16, verified this run) trades fixed full-sample rails `±1.1996%/±1.1621%` around the day open on high/low touch with a first-touch book — different trigger object (price-level touch vs return-space band breach), different calibration (ex-post constants vs trailing estimator), different source and sample (see Negative evidence 8). This is a new family, not a parameter variant: no pool record computes a trailing daily-return mean±kσ band or trades its intraday breach.

## Economic mechanism

### Source-reported

Same-day abnormal-return momentum: on days when the running open-to-close return escapes its trailing normal range, prices `tend to move in the direction of the abnormal returns till the end of the day` (§4, p.259), and the anomaly `can usually be detected before the day ends` (Abstract) — the average BTCUSD detection lands mid-evening (18:00 positive / 16:00 negative), leaving a tradable tail into the close. The authors frame this as a momentum effect *on* the abnormal day (H2, not rejected), distinct from the next-day effect (H3, Strategy 2 — fenced, never ported). No behavioural, structural, or risk-premium mechanism ships beyond the momentum finding itself.

### Research interpretation

Adaptive-band intraday-expansion day trade, two-sided first-breach. Unlike the holmberg ORB (volatility-blind fixed rails from a 1983–2011 crude-oil tail, high/low touch), the rails here breathe: a 30-day trailing mean±2σ estimator in *return space* re-centers every UTC day, so quiet-regime drifts do not fire the machine and volatile regimes do not starve it. Unlike every price-level band record (Bollinger/STARC/EHMA — multi-day holds off level rails) the trigger is the day's own running open-to-close return crossing its statistical abnormality boundary, and the book always goes flat at day-end instead of holding the breakout. Unlike the calendar-hold records (turn-of-month, Monday drift, 21:00-seasonality shape) there is no clock predicate anywhere — firing days are data-chosen, roughly ~95 events over the paper's 4.7-year sample. The failure mode is made plain: the band is backward-looking, so a regime-volatility jump prints late entries into already-extended moves, and a mid-day reversal after entry pays the full excursion into the midnight exit with no guardrail — the day-end close is an exit guillotine, not risk control.

## Signal

Exact rule as pinned (any other `n`, `k`, estimator, frame, fill, book, or void treatment is a different, unpinned rule):

- Day frame: UTC day `D`. `O[D]` = open of the `00:00–01:00 UTC` `1h` bar. Daily return of day `d`: `R[d] = (C[d]/O[d] − 1) × 100%` with `C[d]` = close of the `23:00–00:00 UTC` bar (source eq. (1), open-to-close by paper rule).
- Band (trailing, causal): over the 30 completed UTC days `D−30 … D−1`, `R̄[D] = (1/30)·ΣR[d]` (source eq. (4)) and `δ[D] = sqrt((1/30)·Σ(R[d] − R̄)²)` (source eq. (5), population `1/n` divisor by paper rule). Upper `U[D] = R̄[D] + 2·δ[D]`, lower `L[D] = R̄[D] − 2·δ[D]` (`k = 2` source-pinned for BTCUSD; the window length `n = 30` is the researcher freeze per the Provenance declaration).
- Entry scan (completed `1h` bars only, chronological, bars `00:00–23:00 UTC`): running return `r(D,t) = (close[t]/O[D] − 1) × 100%`. The first bar `t` of day `D` with `r(D,t) > U[D]` → long signal; with `r(D,t) < L[D]` → short signal. The entry fills at the next bar's open, one single unit, only if flat (see position rule). No tie-break exists or is needed: `r(D,t)` is a single scalar and `L[D] < U[D]` always (strict unless `δ = 0` exactly — measure-zero on live tape; record rule: a `δ = 0` day is flat, disclosed convention).
- Final-bar void (pinned researcher rule): a first breach occurring only on the `23:00–00:00 UTC` bar yields no entry. Days with no breach stay flat (the paper likewise holds no position on no-trigger days).
- Exit to flat: the full unit closes with the fill at the `00:00 UTC` open (decision at the `23:00–00:00 UTC` bar close — `closed at the end of the day` by paper rule, one-bar causal fill by record rule).
- Risk posture: no stop-loss, no take-profit, no trailing, no time exit before the day-end close (the paper's algorithm contains no risk leg — carried over exactly, disclosed in Provenance adaptation (6), never upgraded into a source claim).
- Direction: two-sided first-breach (long leg and short leg are both native; at most one fires per day). Shorts are native to USDT-M margin (no uptick rule, no borrow desk).
- Position rule (predeclared researcher pin): single-unit; the day's first breach takes the single unit and every later same-day breach print is a no-op (no pyramiding, no averaging, no flip — including an opposite-band breach later the same day while the unit is open). Re-entry re-arms on the next UTC day (no cooldown specified — explicitly none, not invented). Pre-first-signal bars are flat.

## Required data

- Completed `1h` bars of BTCUSDT: `open` (day anchor `O[D]` plus fills), `high`/`low` unused by any order-gating line, `close` (running-return scan, daily-return aggregation, tie convention). No `volume`, no funding-signal, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar-table, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1h` (no multi-timeframe call, no cross-sectional ranking — one asset, one frame; the UTC-day aggregation is a deterministic fold of the same `1h` series, never a second feed or a `request.security`-class call).
- Warmup: 30 complete UTC days (720 `1h` bars) — the band's deepest read is day `D−30`; pre-warmup bars are flat by record rule. A UTC day missing its `00:00 UTC` open, or with fewer than 30 complete trailing UTC days, is flat by record rule; missing intraday bars are skipped on available completed bars only — prices are never fabricated. No repainting (band fixed from completed days before `O[D]`; scan reads completed bars only), no negative shift, no future reference, no full-sample normalization (Table 1 arithmetic in the companion paper is consistent with trailing-only estimation — cited as consistency, never as an extra claim).

## Execution assumptions

- Research market: BTCUSDT Binance USDT-M perpetual under the house overlay (researcher choice — the paper studies BTCUSD spot, and no source-market equivalence is claimed; perpetual is the minimal realistic venue because the short leg needs margin).
- Order timing (predeclared derivation): completed-bar decision with next-bar-open market fills for both entry and exit — compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) on the same verified primitive as the admitted `holmberg-orb` record's entries (verified this run). This record claims no other fill convention: no perfect-threshold fill (the paper's simulation assumption is recorded as unmodellable, never adopted), no maker-touch, no intrabar-path-dependent fill.
- Stop/limit modeling: none — the derived spec carries zero stop/limit/trailing orders by record rule. No hidden Hummingbot stop-order defaults are relied upon.
- Sizing/capital/costs: the paper ships no sizing, capital, fee, or slippage concept (per-trade `% result` accounting only, cost-free by §3). The explicit house overlay (single-unit frame, pinned house taker fees both legs, modeled funding while held) applies to the derived evaluation here, never presented as source-native behavior. Funding is never zero-claimed: firing-day holds span the `08:00`/`16:00 UTC` funding stamps and the exit fill crosses the `00:00 UTC` stamp by record rule, so every firing day carries modeled funding.
- Concurrency: at most one single-asset engine position at any time; the day-end exit returns to flat in full in one step. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic, no hedge-mode requirement by construction.

## Evidence

### Source-reported

With exact provenance (DOI `10.1007/s11408-020-00357-1`, read end to end this cycle): the dynamic-trigger method choice over the static one (§3, p.255, via the 2019 companion); return definition eq. (1) with the anti-gap rationale (§3, p.255); trigger eqs. (2)–(3) with `k = 2 for BTCUSD` and the sample-size-sufficiency calibration basis (§3, p.255); mean/SD eqs. (4)–(5) with the population divisor (§3, pp.255–256); `24 h` day (§3, p.256); cost-free proxy accounting (§3, pp.256–257); during-day detection with the running-return mechanism (§4, p.259); average BTCUSD detection timings 18:00 positive / 16:00 negative (Tables 2–3, pp.259–260); Strategy 1 rule verbatim (§4, p.260); Strategy 1 BTCUSD simulation Table 4 positive (`49 / 42 / 86% / 143.11% / 28.62% / 2.92% / t 6.62 / Rejected`, p.261) and Table 5 negative (`46 / 42 / 91% / 202.41% / 40.48% / 4.40% / t 8.21 / Rejected`, p.262). It ships zero adopted performance numbers beyond these two tables; no number beyond these is carried here. The averaging-window numeral `n = 30` is NOT printed in the 2020 paper — carried only as the disclosed researcher freeze with companion lineage (see Negative evidence 1).

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Window numeral fenced, admitted plainly: the 2020 paper prints `period n` but no numeral. `n = 30` is a researcher freeze informed by the same authors' companion calibration (periods 5/10/20/30/40/50 tested, 30 selected) — and that calibration ran under a contrarian next-day test with high/low-amplitude returns and `k = 1`, a different strategy than Strategy 1. A reviewer must not cite the companion as proof the paper ran 30; the freeze stands on the derived-spec disclosure alone.
2. Return-definition lineage fenced: the companion's calibration used high/low-amplitude returns while the 2020 paper (and this record) use open-to-close — the 30-carryover crosses that definitional change, disclosed, not tuned away.
3. Table-caption erratum fenced: the descriptive paragraph printed beneath Table 4 (p.261) mislabels its case as `negative` while the table title and numbers are the positive-abnormal-returns Strategy 1 row set (BTCUSD `49/86%/143.11%`); Table 5's paragraph repeats `negative` correctly. Numbers are cited by table title, and the erratum is disclosed rather than silently repaired.
4. Sample-window discrepancy fenced: Abstract and §3 print `01.01.2015–01.09.2019` while the Conclusion (p.263) prints `01.01.2017–01.09.2019`. Neither date enters the rule (the rule consumes only trailing windows), so the discrepancy is load-bearing nowhere — adopted as stated, never resolved by invention.
5. Average timings are not entry clocks, admitted plainly: Tables 2–3 timings (BTCUSD 18:00/16:00) are CAR-analysis averages, and the paper never converts them into an entry schedule. This record enters on the first completed-bar breach whatever hour it prints — a reviewer must not graft the average timings in as fixed entry times, nor average this record's fills back into the paper's simulation.
6. Strategy 2 and every next-day leg fenced, never adopted: the day-after momentum/contrarian rules (pp.260–263, including the BTCUSD-positive-contrarian and ETHUSD-negative-contrarian exceptions) are different, unported rules — a reviewer must not graft next-day entries, timing-parameter exits (16:00/11:00-style clocks), or contrarian flips onto this record.
7. Cost silence fenced: the paper's profits are a cost-free proxy (`only a proxy for actual trading`, §3) — this record claims no net performance and no tradable-profitability conclusion; derived evaluation must carry the full house cost load including modeled funding.
8. Overlap fences, admitted plainly: pool `holmberg-orb-normal-tail` anchors fixed ex-post rails at the day open on high/low touch with a first-touch book (price-level, fixed calibration, crude-oil lineage); pool `dual-thrust-open-range` anchors rails at `open ± k·(prior-day range)` with a reversal-only book (range-adaptive rails, never flat); pool `bollinger-band-breakout-long-midline-exit`/`starc`/`ehma` trade price-level bands with multi-day holds (level bands, never return-space events); pool `alexander-fama-blume-5pct-filter` reverses on closes against a trailing extremum with multi-day holds, long-flat (trailing anchor, never open-anchored, never intraday-flat); pool `tsmom-12m`/`liu-tsyvinski-1w` trade monthly/weekly formation signs (calendar formation, never intraday detection); pool calendar holds (`turn-of-month`, `monday-drift`, `bitcoin-intraday-first-last-halfhour`) trade clock predicates (time predicates, never data-triggered bands). Shared `open`/`band`/`momentum` vocabulary is not shared signal.
9. No hidden variants admitted: any other `n`, any other `k`, any re-estimated or full-sample band, any fixed entry clock, any stop/target/filter/cooldown, any other frame, fill, venue, or book is a different, unpinned rule. A reviewer must not pick among these to rescue or reshape the record.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: open-to-close returns / trailing-30-day population mean±2σ band / `k = 2` / first-breach single side / `δ = 0`-day flat convention / final-bar void / next-open entry and exit fills / no-stop posture / UTC-day frame / `1h` BTCUSDT perpetual are frozen.

- F1 — Momentum-mapping relevance: a fade twin (short on upper breach, long on lower breach — same band, grid, fills, and day-end exit) must not improve net expectancy; fail ⇒ the paper's directional mapping adds nothing over fading the abnormal day on this market.
- F2 — Adaptivity relevance: a fixed-rail twin (`±2%` running-return rails around the day open, no trailing estimator — same book and timing) must not improve net expectancy; fail ⇒ the 30-day trailing band adds nothing over a constant abnormality cutoff.
- F3 — Same-day-detection relevance: a next-day twin (enter at the `00:00 UTC` open in the direction of the prior day's breach flag, exit at the next `00:00 UTC` open — Strategy-2-shaped book on the identical band) must not improve net expectancy; fail ⇒ the during-day detection timing adds nothing over holding the flag into the next day.

## Crypto portability

Pinned to BTCUSDT Binance USDT-M perpetual under the house overlay (declared port of a BTCUSD spot study across CoinMarketCap/Gemini/Bitstamp). The rule reads completed hourly bars only, so no pit-session, gap, roll, or corporate-action logic ports — but the paper's 2015–2019 spot-market microstructure vs 24/7 perpetual execution is a real mismatch, fenced via the venue pin and the funding treatment. The band is scale-free (percent returns, σ-multiples), so no price-level recalibration crosses venues — yet crypto's 24/7 volatility clustering vs the paper's sample regime is unclaimed and undisguised (see Negative evidence). The rule is two-sided first-breach, so a spot-only deployment expresses only long-firing days while short-firing days stay venue-gated (never silently converted) — a spot-only variant would be a different, unpinned claim. No warmup history beyond 30 UTC days (720 `1h` bars) is consumed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- No price stop, no intraday time stop: adverse excursion after a breach entry has no guardrail before the day-end exit, by the carried-over paper design — the record's principal risk.
- Backward-looking band lag: volatility-regime jumps print late entries into already-extended moves, and mid-day reversals after entry pay the full excursion plus taker fees both legs plus funding, disclosed, not tuned away.
- Evening-concentration exposure: average detection lands late in the UTC day (paper: 16:00–18:00), so realized holds are often short windows into the close — entry-to-exit edge per firing day is thin by construction.
- Single-venue daily-port residual: sample exchanges vs Binance perpetual execution (prints, fees, funding, margin mechanics beyond the house model) is unclaimed, disclosed.
- Performance evidence is paper-sample-bound: the Table 4/5 figures describe the authors' 2015–2019 cost-free simulation of their exact sample, never this derived port — no profitability is claimed here.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior and never part of this admission — no Safety-Order/DCA event is admitted in this record's version. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Caporale, G. M. & Plastun, A. (2020), `Momentum effects in the cryptocurrency market after one-day abnormal returns`, Financial Markets and Portfolio Management 34:251–266, published online 2020-05-27 (eqs. (1)–(5) §3 pp.255–256; detection timing §4 p.259; Strategy 1 rule §4 p.260; Tables 2–5 pp.259–262 — read end to end via live fetch 2026-10-16): https://doi.org/10.1007/s11408-020-00357-1
- Brunel University repository open-access copy (CC-BY 4.0, 291978 bytes, SHA-256 `31b92c06a3137606db91e355427063ae7dcd23ee88348a20be701e40cfcbe863`): https://bura.brunel.ac.uk/bitstream/2438/20686/6/FullText.pdf
- Caporale, G. M. & Plastun, A. (2018), `Price overreactions in the cryptocurrency market`, DIW Berlin Discussion Paper No. 1718 (journal version J. Econ. Stud. 46(5):1137–1155 — averaging-period calibration §4/Table 1 only, fenced as lineage, never adopted as the 2020 paper's print): https://www.econstor.eu/bitstream/10419/175075/1/1013722922.pdf
