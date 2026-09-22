---
schema: strategy-research-record-v1
title: Kalshi temperature-ladder market-implied forecast vs the public weather-forecast stack (information-lead / parity capture)
created: 2026-09-22
updated: 2026-09-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-08-12
sources:
  - https://arxiv.org/abs/2609.23969
  - https://arxiv.org/html/2609.23969v1
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Kalshi temperature-ladder market-implied forecast beats the public weather-forecast stack (information-lead / parity capture)

## Provenance

- **Primary source:** Alexander W. Crosier, 〈Prediction Markets Beat the Weather Forecast on Tomorrow's High Temperature〉, arXiv:2609.23969 [q-fin.GN (primary), econ.EM cross-list per landing taxonomy shown as General Finance q-fin.GN], **v1 submitted 2026-09-21** (manuscript dated September 20, 2026).
- Landing: `https://arxiv.org/abs/2609.23969`; full text read: `https://arxiv.org/html/2609.23969v1` (LaTeXML HTML, document created 2026-09-20). Read on 2026-09-22: abstract, §1 Introduction (Main findings / Related work), §2 The setting (2.1–2.4), §3 Results (3.1–3.2), §4 Cities and seasons, §5 Does the market jump on forecast updates?, §6 Conclusion, Appendix A (A.1–A.3, liquidity screens, bias correction), Appendix B (B.1 tests, B.2 robustness), Table 1/2/3 and Figure 1–5 captions.
- **Author list:** single author, exactly `Alexander W. Crosier` (citation meta `Crosier, Alexander W.`).
- **Publication status:** preprint only. The landing page shows **no journal-ref, no DOI, no comments field** as of 2026-09-22. Not peer reviewed.
- **Concurrent work cited by the source (not the source of any number in this record):** Brown (2026), 〈Improvement of daily temperature forecasts from a prediction market〉, working paper, Trend Analytics LLC, version of 18 September 2026 (ForecastEx exchange, 20 locations, seven months of 2026).
- **Sample / data as-of:** panel of **7,590 city-days**, last market **2026-08-12** (Table 1 + footnote 2). Dedup: full-repo `rg` for `2609.23969`, `Crosier`, `National Blend`, `market-implied forecast`, `temperature.*Kalshi`, `weather forecast` returned **0 hits** across all `*.md`, and `~/.hermes/wiki` returned 0 hits (see Related Wiki records).

## Economic mechanism

### Source-reported

- Kalshi lists a daily **ladder of mutually exclusive rungs** on tomorrow's high temperature (e.g. `81°F or lower`, `82–83°F`, …, `90°F or higher`); each rung pays $1 if the settled high lands in its interval. The paper reads the rung prices as a conditional distribution, `π_i = Pr(T ∈ I_i | I_M)` (Eq. 1), and takes its mean `μ_M = Σ π_i c_i` as the market-implied forecast (Eq. 2).
- Author's stated rationale: traders can read every public forecast before betting, so their information set `I_M` contains the published stack plus whatever they add; because the price is a conditional mean and any public forecast `F` is measurable w.r.t. `I_M`, `E[(T − μ_M)²] ≤ E[(T − F)²]` (Eq. 3). The measured gap is how much the public system left on the table at that moment (§2.1).
- Direction-of-revision claim (§5, Table 3): between NBM postings the public blend moves toward the existing market roughly **four times** as far as the market moves toward the NBM, and prices show **no jump** when the National Weather Service publishes — i.e. the source frames the market as publishing information the official system later catches up to, not reacting to it.
- Author's economic motivation (§1, §6): next-day temperature forecasts drive airline, food-processing and utility scheduling; Figure 5 (ComEd zone, 2021–2026) shows each additional degree of daily high above 75°F adds roughly **340–480 MW** of evening-peak demand, so the ~⅓ °F error the market removes from the best public product is argued to be worth >100 MW of scheduling error per summer day. This is an illustrative economic mapping in the source, **not a backtested P&L**.

### Research interpretation

- Mechanism class: **information aggregation vs institutional publication lag** (a measurement/forecast-superiority claim), *not* a demonstrated return-generating rule. The source contains **no trade rule, no positions, no costs and no P&L**.
- Falsifiable hypotheses, separated by provenance:
  - **H1 (source-reported, measured):** from the first trading hour, the Kalshi ladder-implied mean has lower squared error for the settled station high than the best single public product (NBM) and than an out-of-sample combination of the public stack.
  - **H2 (research-proposed, not in source):** on days where the rung containing `μ_M` differs from the rung implied by the public forecast, taking the **market's side of that rung disagreement** settles with lower expected squared error *and* with positive expectancy after fees/spread — the second clause is **entirely untested by the source** and is the only part that would make this a trade.
  - **H3 (research-proposed, not in source):** the ladder-implied mean can be used as an early exogenous feature for weather-exposed instruments (power/energy, ag, weather-sensitive equities), i.e. read the market before the official stack updates. The source motivates this economically (ComEd example) but never tests any cross-asset return.
- Hybrid component roles (labels matter): *signal* = market-implied mean vs public-forecast disagreement at a fixed anchor hour; *filter* = the source's liquidity screens (≥3 quoted rungs, bid–ask spread ≤ 50¢, rung midpoints summing within ±30% of 1) — these are **source-reported data screens**, not alpha; *entry/exit/sizing* = **research-proposed**, absent from the source.

## Signal

**Source-specified elements (reconstructable):**

- **Listing / formation timestamp:** each contract lists at **10:00 AM Eastern on day d−1**; the market is read continuously, with three evaluation anchors: **11:00 ET** (end of the market's first trading hour), **19:00 local time on d−1** (evening), and **13:00 UTC on the target day** (the NBM's final max-temperature bulletin posts 08:40 ET / 12:40 UTC; the study ends at 13:00 UTC) (§2.2, §3.2).
- **Construction:** at each snapshot, take the **bid–ask midpoint** of every quoted rung as its probability mass, spread mass uniformly inside closed intervals; open tails get geometrically decaying mass with ratio **τ = 0.55** over the next 15 integers (95% of tail mass in the nearest five degrees); market forecast = mean of that distribution; the implied **median** is reported as a tail-invariant robustness check (Appendix A.1, B.2).
- **Liquidity screens (source-reported):** ≥3 quoted intervals; bid–ask spread ≤ **50 cents**; midpoint probabilities sum within **±30% of 1**; retains **86%** of observations at the three anchors (Appendix A.1).
- **Settlement:** NWS **daily climate report** for a named station, maximum over the full calendar day; the seven cities/stations and day counts (Table 1): New York/Central Park 1,684; Chicago/Midway 1,684; Miami Intl 1,189; Austin–Bergstrom 1,186; Philadelphia Intl 631; Denver Intl 631; Los Angeles Intl 585; **total 7,590**, listings from Jan 2022 (NY, Chicago), May 2023 (Miami, Austin), Nov 2024 (Philadelphia, Denver), Jan 2025 (Los Angeles).
- **Public benchmarks:** six products — NDFD, NBM, LAMP, GFS MOS, HRRR, ECMWF — with publication timestamps; HRRR/ECMWF/LAMP de-biased with a rolling mean error estimated on the **365 days before** each forecast date; NBM/NDFD/GFS MOS use their own daily-max field, completed with LAMP night hours plus observed max where the high falls outside the daytime window (4.6% of days) (§2.4, Appendix A.2–A.3).
- **Evaluation statistic:** RMSE in °F of market vs product; percentage advantage `gap_F = 100·(RMSE_F − RMSE_mkt)/RMSE_F` (Eq. 5); significance via Diebold–Mariano t-test on the daily pooled squared-error difference with Newey–West standard errors; Figure 2 band from a moving-block bootstrap of 10 consecutive dates (Appendix B.1).

**Not in source (⇒ research-proposed, do not read as source-reported):**

- Entry trigger: `research-proposed` — first anchor hour (11:00 ET on d−1) at which rung(`μ_M`) ≠ rung(public forecast), both sides passing the source's liquidity screens, buy the market-side rung **at the ask**.
- Exit / holding: `research-proposed` — hold to settlement (binary payout); no stop, no intraday re-entry; one position per city-day, at most seven concurrent.
- Sizing: `research-proposed` — flat contract count per city-day (no Kelly, no vol targeting; the source specifies none).
- Order type, fill model, fees, slippage, spread cost, latency, capacity: **not stated in source** (see Execution assumptions).
- Falsification thresholds below are `research-defined`.

Signal is therefore **partially specified**: the measurement side is reproducible from the source; the trading side is underspecified and must not be presented as reproducible evidence.

## Required data

- Kalshi daily temperature ladders for the seven cities: per-rung **bid/ask quotes and timestamps** at least at the three anchors (hourly snapshots implied by the paper's hour-by-hour construction), plus settlement source and station.
- NWS/NOAA archives with publication timestamps: NBM station bulletins and NDFD transmissions (NOAA Open Data Dissemination buckets), GFS MOS and LAMP (Iowa Environmental Mesonet — **only 00/06/12/18 UTC cycles retained**, so the freshest LAMP is 2 h old at the opening hour and 4 h in the evening), HRRR (NOAA GSL archive), ECMWF open-data archive.
- Station daily climate reports (settlement truth) for each of the seven stations.
- Point-in-time requirements: publication timestamps of every product; rolling 365-day bias-correction window estimated only on past data; combination weights refit daily, city by city, on days before d (Eq. 6, out-of-sample by construction).
- Timezone/alignment: Eastern local time for market anchors, UTC for NBM final bulletin and study end; calendar-day max vs daytime-max mismatch handled as in Appendix A.2.
- Missing/stale data: liquidity screens (they remove 14% of observations, mostly 2022–2024); quotes not passing screens are dropped, not imputed; results without screens are reported in Appendix B.2.
- **Structural break:** after **2026-08-12** Kalshi changed its settlement source from the NWS to **The Weather Company** (footnote 2); the study deliberately stops there. Any extension needs a new settlement definition — flagged as a `data gap` for out-of-sample work.

## Execution assumptions

- **Source:** quotes are read at the **bid–ask midpoint**; the paper models **no orders, no fills, no fees, no slippage, no bid-ask cost at execution, no funding, no leverage, no sizing, no latency, no capacity or market-impact, and no P&L**. Every one of these is `not stated in source` — and per contract must **not** be inferred to be zero. The spread is used only as a **screen (≤50¢)**, never as a cost.
- The midpoint is a measurement device, **not an executable price**: a buyer crossing the ladder pays the ask, so any H2-style rule must be re-costed from top-of-book data the source does not provide.
- **Scout assumptions (research-proposed, for the falsification plan only):** taker fill at the ask of the target rung at the 11:00 ET anchor; settlement redemption at $1/$0; fee and slippage charged per contract (magnitudes declared as research-defined stress levels below, not as source assumptions).

## Evidence

### Source-reported

All figures below are `source-reported`, each with its location in arXiv:2609.23969v1; none independently verified.

- **Table 2 (three anchors; RMSE °F, `gap %` = market's advantage; every gap significant at 1% except ‡ which is 10% only):** Market **2.44 / 2.21 / 1.88** (opening hour / evening / final bulletin). NBM **2.70 (+9.8) / 2.45 (+10.0) / 2.12 (+11.4)**; LAMP de-biased 2.83 (+13.9) / 2.63 (+16.3) / 2.19 (+14.2); NDFD 2.83 (+13.9) / 2.66 (+17.0) / 2.33 (+19.3); GFS MOS 3.17 (+23.0) / 2.95 (+25.2) / 2.69 (+30.2); HRRR de-biased 3.32 (+26.6) / 3.07 (+28.1) / 2.63 (+28.6); ECMWF de-biased 3.31 (+26.4) / 3.16 (+30.3) / 2.68 (+30.6); **Combination (out-of-sample) 2.45 (+3.1) / 2.25 (+4.3) / 1.90 (+3.0)‡**. §3.2 text adds that on the (fewer) days the combination exists, the market's own RMSE is 2.38 / 2.16 / 1.84.
- **Figure 2 (seven cities pooled):** NBM error falls 2.7 °F → 2.1 °F from opening hour to target morning; market 2.4 °F → 1.9 °F; market advantage **10% at the first hour, 11% at the final bulletin**, with a 95% block-bootstrap band (10-day blocks).
- **Table 1:** city/station panel, listings and day counts above; **7,590 city-days**, last market 2026-08-12; footnote 2 records the settlement-source change to The Weather Company thereafter.
- **§4 Cities and seasons:** market beats NBM in every city and anchor **except Miami** (NBM RMSE 1.6 °F there vs 2.6–3.5 °F in the other six); Nov–Jun (NBM preceding-day error ≥3 °F) advantage **10–16%**, Jul–Oct only **1–4%**; each additional degree of NBM error adds ≈**6 percentage points** of market advantage (**R² = 0.22**); at the opening hour Miami traders stay within 2 °F of NBM on 98% of days vs Chicago straying ≥2 °F on 20% of days.
- **§5 Table 3 (revision regressions, Eq. 7):** pooled `β_ant = 0.042 (t = 15.9)`, `γ_react = 0.037 (t = 11.9)`, `β_gap = 0.153 (t = 13.7)`, **n = 112,491**; per-city rows: Austin 0.058/0.036/0.225 (n = 17,784), Chicago 0.035/0.043/0.124 (22,241), Denver 0.052/0.014/0.144 (11,205), Los Angeles 0.042/0.061/0.191 (10,362), Miami 0.079/0.032/0.248 (17,371), New York 0.037/0.048/0.129 (22,315), Philadelphia 0.035/0.026/0.155 (11,213). Text: a one-s.d. disagreement of **1.49 °F** moves the NBM **0.063 °F**; a typical revision of **0.43 °F** moves the market **0.016 °F** (≈4×); Chicago illustration — where NBM revised 1 °F, the market had moved 0.011 °F in the prior 45 minutes and 0.007 °F after, ≈2% of the revision, "no jump at the time of publication."
- **Appendix B.2 robustness:** without liquidity screens the market's advantage over NBM is **8.0 / 9.0 / 8.0%** (vs 9.8 / 10.0 / 11.4%), still significant at 1%; against the public combination it becomes **1.9 / 3.2 / 0.7%** with the final anchor **not significant**; NBM's RMSE on discarded days 2.53 °F vs 2.45 °F on kept days. Implied-median construction reproduces every headline (agreement within 0.05 °F pooled, gaps move <2%). Equal-weighted public average beats the fitted combination at the opening hour (2.43 vs 2.45 °F) and shrinks the market's opening margin to **2.1%**.
- **§6 / Figure 5:** ComEd evening-peak demand rises ~**340–480 MW** per degree above 75 °F (2021–2026); the source argues the market's ~⅓ °F improvement implies >100 MW less scheduling error per summer day — an illustrative mapping, **not a backtest**.

### Independently reproduced

not independently reproduced

### Negative evidence

- **No trading evidence at all:** the source contains zero order/fill/fee/slippage/sizing/P&L treatment; forecast-accuracy superiority does not imply an executable positive-expectancy rule once the ask, fees and the ladder's spread are paid.
- **Miami fails outright** — the market does not beat NBM there (§4); where public forecasts are already accurate (NBM 1.6 °F), the market adds nothing.
- **Margin collapses in easy seasons:** Jul–Oct advantage only **1–4%**, i.e. the same order of magnitude as plausible per-contract frictions (frictions themselves are unstated, so this is a concern, not a computed result).
- **Against the strongest public benchmark the edge is thin:** out-of-sample combination gaps only **3.1 / 4.3 / 3.0%**, with the final anchor significant at 10% only; **without liquidity screens the final-bulletin gap is not significant at all** and the combination gaps fall to 1.9 / 3.2 / 0.7%; against an equal-weighted public average the opening margin is **2.1%** (B.2).
- **Selection/survivorship concern:** liquidity screens discard **14%** of observations, almost all from 2022–2024 (Appendix A.1) — i.e. the studied period is the more liquid, more recent regime.
- **Construction sensitivity:** the market mean depends on the open-tail model (τ = 0.55, 15 rungs); only the median check is reported as invariant (B.2).
- **Structural break:** settlement source changes from NWS to The Weather Company after **2026-08-12** (footnote 2); results may not carry forward.
- **Concurrent replication is weaker:** the source itself reports that Brown (2026) on ForecastEx finds the market ahead of individual products and ahead of a de-biased combination **"by a much smaller margin"** (§1 Related work) — independent, but tempering.
- **LAMP data constraint:** the Mesonet retains only four LAMP cycles per day, so the public stack is compared partly against stale LAMP at two anchors (Appendix A.3) — a data-quality caveat that flatters the market relative to a fully refreshed stack.
- **Publication status:** single-author, non-peer-reviewed v1 preprint dated 2026-09-20/21.
- No contrary study on this exact claim was found in the reviewed sources; absence is not evidence of no negative result.

## Falsification plan

Thresholds below are `research-defined` unless marked `research-proposed` (operational rules) or `source-reported` (methods inherited from the paper).

1. **H1 out-of-sample replication (source-reported method).** Data: Kalshi ladders + NBM + station climate reports, all city-days with listing after **2026-08-12** (new settlement source explicitly flagged). Metric: daily pooled squared-error differential (market − NBM) at the three anchors, Diebold–Mariano t-test with Newey–West SEs (Appendix B.1). **Failure rule:** rolling 12-month market advantage ≤ 0, or a 95% interval containing 0 for six consecutive months → reject H1 for the new settlement regime. Action: mark the record's information-superiority claim stale; no retuning of anchors or screens to rescue it.
2. **H2 executable wedge (research-proposed rule).** Entry: `research-proposed` — 11:00 ET anchor, rung(μ_M) ≠ rung(public forecast), both passing the source's liquidity screens, buy the market-side rung at the ask; exit: hold to settlement. Sample: ≥500 settled city-day positions across ≥3 cities and ≥2 seasons. **Cost stress (research-defined):** repeat at fee+slippage ∈ {0, 1 tick, 2 ticks} per contract. **Failure rule:** net expectancy ≤ 0 in the baseline cost run, or a 95% moving-block-bootstrap interval including 0, → H2 rejected even if H1 survives; action: record stays research-only with `tradability: falsified-at-current-costs`.
3. **Stack ablation (source-reported sensitivity).** Refit the public combination without LAMP (source reports gaps then become 3.3 / 4.7 / 6.4%). If the market's advantage over the five-product stack is not significant at the opening hour, the claim "the market contains information the whole public stack lacks" is weakened; action: downgrade confidence and restate the result as "market ≈ best refreshed public product".
4. **Placebo (research-defined).** Re-run step 1 after shifting market quotes by ±1 day and after permuting city-day pairings. **Failure rule:** a placebo gap of the same sign and magnitude as the headline gap → the measurement pipeline is contaminated; discard the capture.
5. **Competing-explanation audit (source-reported precedent).** Repeat without liquidity screens and against the equal-weighted public average (source's own numbers: 8.0/9.0/8.0% and 2.1%). If the advantage disappears under either choice, attribute it to screening/combination choice, not information.
6. **Cross-domain claim (H3, research-proposed).** Only if steps 1–2 pass: test the ladder-implied mean as a pre-release feature for a weather-exposed instrument (e.g. next-day power/energy proxies), point-in-time, with the official forecast stack as control. **Failure rule (research-defined):** no significant incremental predictive power (|t| < 2 with HAC SEs) out-of-sample over ≥12 months → drop H3, keep H1/H2 conclusions separate.
7. **Capacity:** not assessed anywhere in the source; any adoption review must treat capacity as unknown (data gap), not as unlimited.

## Crypto portability

`adapted` — the *method* (read a binary ladder as a distribution, race it against an institutional/model forecast, test the revision direction) ports to recurring crypto binary markets such as daily BTC threshold contracts on Polymarket/Kalshi; the *source provides zero crypto evidence* and must not be cited as crypto validation.

Crypto-specific risks: no daily station-style settlement oracle analog (crypto contracts settle on exchange/index prints with their own index methodology); 24/7 sessions remove the fixed listing/anchor-hour structure; ladders are often far thinner and wider than the ≤50¢ screen tolerates, so the liquidity-screen regime differs sharply; venue/oracle fragmentation and settlement-source changes (the source itself hits one after 2026-08-12) are a first-order risk; there is no canonical "public forecast stack" for crypto returns, so H1's benchmark must be rebuilt (options-implied or model forecasts), which changes the hypothesis. Adjacent existing captures cover crypto-side threshold mispricing and prediction-market microstructure (see Related). Crypto portability is not authorization to trade.

## Limitations

- **underspecified** — trading layer entirely absent (entry/exit/sizing/order type/fill/fees/slippage/capacity all `not stated in source`).
- **not independently reproduced** — every number is source-reported from a single non-peer-reviewed v1.
- **data gap** — settlement-source change after 2026-08-12; LAMP archived at four cycles/day; daytime-max vs calendar-day-max completion for three products; open-tail modeling of the ladder mean; 14% of observations screened out (mostly 2022–2024).
- **data gap** — no order-book depth, no executable prices at the anchors, no capacity analysis.
- Sample is unbalanced across cities (LA 585 days from Jan 2025 vs NY/Chicago 1,684 from Jan 2022); pooled results are dominated by the two oldest, largest cities.
- Miami is a documented failure case; seasonal margins of 1–4% may be inside realistic per-contract frictions (frictions themselves unstated ⇒ cannot be computed from the source).
- Publication-bias and single-author risk; concurrent Brown (2026) reports a smaller margin against the de-biased combination and has not been independently read for this record (its numbers are **not** used here).

## Implementation status

`implementation_status: not-implemented`. Nothing has been implemented in our research stack: no Kalshi ladder ingestion, no forecast-archive pipeline, no RMSE/DM replication, no wedge backtest, no order routing, and no Wiki/candidate-pool/Qlib/Paper/Testnet/Live activity. This document is a normalized research capture only.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet, or live trading. Any adoption decision must be explicit, separately reviewed, and based on this record plus current sources.

## Related Wiki records

Full-repo and Wiki-wide searches for `2609.23969`, `Crosier`, `National Blend`, `market-implied forecast`, `temperature.*Kalshi` and `weather forecast` found **no existing record of this source or of the weather-temperature-market information-lead mechanism**; this is a new capture, not an update.

Related (mechanism-distinct) Wiki pages, linked as retrieval hooks only:

- [[quant/prediction-market-structural-volatility-wright-fisher-glosten-milgrom-2026-09-02]] — structural variance decomposition of binary Kalshi/Polymarket contracts (its Kalshi panel mentions weather categories); different mechanism, no forecast-race content.
- [[quant/prediction-market-llm-confidence-weighted-value-bet-2026-09-04]] — Polymarket LLM value-betting; different universe, signal and evidence.
- [[quant/defi-prediction-market-uniform-loss-amm-lvr-dynamic-liquidity-2026-09-02]] — AMM/LVR theory for binary prediction markets; market-making, not information-vs-official-forecast.

Adjacent records in this repository (same venue family, materially different mechanisms): `polymarket-favorite-longshot-bias-crypto-politics-2026-09-14.md`, `kalshi-btc-event-contract-spot-hedge-2026-09-15.md`, `kalshi-prediction-market-pricing-wedge-executable-spread-falsification-2026-09-13.md`, `crypto-cross-platform-binary-threshold-mispricing-polymarket-binance-2026-09-01.md`, `league-of-legends-pregame-paired-comparison-polymarket-parity-2026-09-22.md` (esports parity capture — different universe and mechanism), `coffee-commodity-weather-stress-lagged-overlay-2026-09-12.md` (weather as a commodity overlay, not a prediction market).

## Sources

- Alexander W. Crosier, 〈Prediction Markets Beat the Weather Forecast on Tomorrow's High Temperature〉, arXiv:2609.23969v1 [q-fin.GN], submitted 2026-09-21 — landing `https://arxiv.org/abs/2609.23969` (primary source; author list, version/date, sample, universe, statistics and caveats verified there and in the full text).
- Full text HTML v1, read 2026-09-22: `https://arxiv.org/html/2609.23969v1` — provenance for Table 1/2/3, Figures 1–5, §2–§5 and Appendices A–B.
- Method references *cited by the source* (used only to describe the source's own inference, not as independent evidence): Diebold & Mariano (1995), doi:10.1080/07350015.1995.10524599; Künsch (1989), doi:10.1214/aos/1176347265; Craven et al. (2020), doi:10.15191/nwajom.2020.0801; Ghirardelli & Glahn (2010), doi:10.1175/2010WAF2222312.1; Glahn & Lowry (1972); Gürkaynak & Wolfers (2007), doi:10.7551/mitpress/7523.0004.0011; Cowgill & Zitzewitz (2015), doi:10.1093/restud/rdv014; Ritter (2013), doi:10.21314/JEM.2013.100; Roll (1984); Smith & Wallis (2009), doi:10.1111/j.1468-0004.2008.00541.x; Brown (2026) working paper, Trend Analytics LLC, version of 2026-09-18 (referenced only as the source's own concurrent-work statement — its figures are not quoted here).
