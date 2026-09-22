---
schema: strategy-research-record-v1
title: "Spread THieF Forecast Reconciliation of Hourly Prices and Pairwise Intraday Spreads for Battery Arbitrage in Day-Ahead Electricity Markets"
created: 2026-09-22
updated: 2026-09-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - electricity
  - forecasting
  - forecast-reconciliation
  - temporal-hierarchy
  - battery-storage
  - arbitrage
  - decision-focused-forecasting
status: research-only
confidence: medium
source_as_of: 2026-09-19
sources:
  - "https://arxiv.org/abs/2609.23223"
  - "https://arxiv.org/html/2609.23223v1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Spread THieF Forecast Reconciliation of Hourly Prices and Pairwise Intraday Spreads for Battery Arbitrage in Day-Ahead Electricity Markets

## Provenance

- **Paper:** Arkadiusz Lipiecki, Nikolaos Kourentzes, and Rafal Weron, "Stealing profits: Spread-based temporal hierarchy forecasting for day-ahead electricity markets."
- **Preprint:** arXiv:2609.23223v1 [q-fin.ST] (cross-listed cs.LG, econ.EM), submitted 19 September 2026 (v1; no later version as of capture).
- **Stable URLs:** https://arxiv.org/abs/2609.23223 ; full text https://arxiv.org/html/2609.23223v1
- **Publication status:** preprint; no journal reference, comments, or DOI beyond the arXiv-issued identifier is stated on the arXiv landing page (checked 2026-09-22).
- **Acknowledged funding:** National Science Center (NCN, Poland) grant no. 2025/57/B/HS4/02413 (Acknowledgments).
- **Data as-of:** datasets "publicly available data downloaded in July 2026" (Section 3); sample window 05.01.2018–31.12.2025, test period 01.01.2021–31.12.2025.
- **Primary-source checksum (2026-09-22):** opened the arXiv landing page and the full HTML text of v1 and verified there: exact author list/order (Lipiecki, Kourentzes, Weron); version/date (v1, 19 Sep 2026); sample period and universe (EPEX-DE Germany and OMIE Spain day-ahead hourly, 2018–2025, five-year test); cost/efficiency treatment (Sections 5.3–5.4: 1 MWh battery, round-trip operating cost C = 25 EUR, η ∈ {1, 0.95, 0.9}); and every performance number below with its Table/Figure/Section location. Fields not verifiable from the primary text are marked `data gap` / `not stated in source`.

## Economic mechanism

### Source-reported

The paper's thesis is decision-focused forecasting: for a battery energy storage system (BESS) operator, the economic value of a day-ahead electricity price forecast depends on the *relative* ordering of hours (the buy–sell spread, adjusted for efficiency and operating cost), not on the absolute accuracy of each hourly price. Accurate hourly forecasts do not automatically imply accurate spread forecasts because errors at two hours can reinforce or cancel. The authors extend temporal hierarchy forecasting (THieF) with a "Spread THieF" hierarchy that stacks 24 hourly prices with all 276 pairwise intraday price spreads (C(24,2)) and reconciles base forecasts across this 300×24 summing structure (Sections 1, 2.2–2.4). Source-reported results: reconciliation improves forecast accuracy across ARX, NARX, and TabPFN-2 architectures and translates into higher stylized BESS arbitrage profits and lower relative opportunity cost versus unreconciled and block-reconciled forecasts (Sections 6.1–6.2).

### Research interpretation

Falsifiable mechanism statement: **coherence-constrained combination of forecasts of economically linked targets (price levels plus their pairwise differences) reduces decision-relevant ranking error**, so a spread-capture decision rule built on reconciled forecasts beats the same rule on unreconciled forecasts. Component roles (hybrid structure preserved):

```text
Regime: none required by the source (fixed rolling estimation window; no explicit regime filter)
Primary signal: reconciled forecast of each pairwise intraday spread (and efficiency-adjusted price pairs)
Decision rule: daily one-cycle charge/discharge selection with no-trade option (Sections 5.3, Eq. 26–29)
Risk / exit: single same-day discharge; fixed round-trip operating cost C acts as a break-even filter, not an alpha source
```

The alpha claim under test is narrow and incremental: *the reconciliation layer* adds decision value over the same base model — not that electricity price forecasting itself is a free lunch (the Oracle/perfect-foresight benchmark bounds attainable profit).

## Signal

All operational choices in this section are **source-reported** unless explicitly marked research-proposed/research-defined.

- **Formation timestamp:** For delivery day `d`, each of the 336 series (24 hourly prices, 36 block prices, 276 pairwise spreads) is forecast with models estimated on a 3-year rolling window that is rolled forward one day after each forecast; features use lags through `d-7`, previous-day min/max, day-ahead load and renewable-generation forecasts for day `d`, and TTF gas / API2 coal closes at `d-2` (Section 4, Eqs. 17–18). `data gap`: the exact clock time of forecast publication versus the day-ahead auction gate closure (e.g., 12:00 CET) is not stated in source; ENTSO-E day-ahead load/renewable forecast availability timestamps are also not stated.
- **Lookback:** 3-year rolling estimation window = 1092 days initial window to 31.12.2020 → 1085 usable points after the 7-day price lags; window re-rolled daily (+24 h). Covariance matrix for reconciliation re-estimated daily on the same 1085-day in-sample forecast errors (Section 2.4, Section 3).
- **Forecast layer (signal construction):** base forecasts per series from one of three architectures — ARX (OLS with 14 features, inverse-hyperbolic-sine preprocessing), NARX (one hidden layer, 5 tanh neurons, Levenberg–Marquardt with 10% validation early stopping, committee average of 10 networks), TabPFN-2 (zero-shot in-context learning, 8-estimator ensemble) (Sections 4.1–4.3). Reconciliation: `ỹ = S G ŷ` with `G = (Sᵀ W⁻¹ S)⁻¹ Sᵀ W⁻¹`, `W` shrunk to a diagonal target (Schäfer–Strimmer, main spec; Ledoit–Wolf constant-correlation as robustness) (Section 2.3–2.4, Eq. 15–16).
- **Long entry (charge):** choose the pair `1 ≤ i < j ≤ 24` maximizing the predicted net profit `η·p̂_d,j − (1/η)·p̂_d,i − C`; buy electricity and charge at `h1 = i`.
- **Short entry (discharge/sell):** hour `h2 = j > h1`, discharge and sell at `h2`.
- **No-trade rule:** if the maximum predicted net profit is ≤ 0, do not operate the battery that day (Eq. 27).
- **Exit:** discharge completes within the same delivery day; no overnight or multi-day position (Sections 5.3).
- **Holding period:** strictly intraday (buy hour < sell hour, same day), at most one cycle per day; initial state of charge 0 MWh.
- **Parameters (all source-reported):** battery capacity 1 MWh; charge efficiency = discharge efficiency = η with round-trip η²; η ∈ {1, 0.95, 0.9}; fixed round-trip operating cost C = 25 EUR covering investment expenditure, fixed/variable O&M, and battery degradation (following Lindberg et al., 2024; similar to Maciejowska et al., 2026) (Section 5.3, Eq. 26).
- **Position sizing:** fixed 1 MWh physical battery, price-taking; no portfolio sizing layer.
- **Realized P&L:** `π_d = η·p_d,h2 − (1/η)·p_d,h1 − C` if a trade was taken, else 0 (Eq. 29), evaluated against realized day-ahead clearing prices (fill at the forecast/cleared day-ahead price — see Execution assumptions).
- **Benchmarks:** Base (unreconciled hourly), Base-spreads (unreconciled spread forecasts, only for η=1), Block THieF, seasonal Naive, and Oracle (perfect foresight) (Sections 5.3–5.4).
- **Reconstruction status:** fully specified for the stylized application — an independent researcher can reconstruct the decision rule, reconciliation, and evaluation metrics from Sections 2–5; the base-forecasting layer is reproducible in structure but `data gap` on exact feature vintages (ENTSO-E revised historical data; the paper notes its data differs from earlier studies, particularly German 2024 prices, Section 3).

## Required data

- **Instrument / universe:** day-ahead hourly electricity prices for two markets: EPEX-DE (Germany) and OMIE (Spain); no individual "asset" universe — the traded instrument is the hourly delivery product plus the physical battery.
- **Venue / market type:** EPEX SPOT German day-ahead and OMIE Spanish day-ahead (wholesale power, day-ahead auction); market type = physical electricity day-ahead market.
- **Timeframe:** hourly prices (24 per day); daily-resolution exogenous series; eight-year span 05.01.2018–31.12.2025.
- **Fields:** day-ahead prices `p_d,h`; day-ahead load forecast `L̂_d,h` and renewable generation forecast `R̂_d,h` (onshore wind + offshore wind + solar) from the ENTSO-E Transparency Platform (https://transparency.entsoe.eu); TTF natural-gas nearest-to-delivery futures close and API2 coal nearest-to-delivery futures close at `d-2` from Investing.com; day-of-week categorical (Section 3).
- **Point-in-time:** predictors are lagged or day-ahead-available in the source design (lags to `d-7`, commodity closes at `d-2`, day-ahead load/renewable forecasts for `d`); train/test boundary fixed at 31.12.2020 / 01.01.2021 with daily rolling re-estimation (no future leakage claimed in source). `data gap`: precise publication timestamps of the day-ahead load/renewable forecasts are not stated.
- **Timestamp / timezone:** `data gap` — the paper does not restate the delivery-session timezone convention (German/Spanish day-ahead sessions are local time with DST handling); not stated in source.
- **Missing data / revisions:** ENTSO-E past-data revisions mean this study's German 2024 prices differ from datasets used in Serafin & Weron (2025), Lipiecki et al. (2026), and Maciejowska et al. (2026) (Section 3); imputation not described → treat as not specified.
- **Funding/fee/spread needs:** round-trip physical cost C = 25 EUR and efficiency η are modeled; wholesale bid/offer spreads, imbalance fees, grid tariffs, taxes, and balancing penalties are `not stated in source` (see Execution assumptions).

## Execution assumptions

- **Signal-to-order timing:** forecasts for delivery day `d` are produced before delivery (daily rolling procedure, Section 4); the exact order-entry/gate-closure timing is `data gap` / not stated in source.
- **Order type / fill model:** the stylized strategy assumes the battery clears the day-ahead market at the same hourly prices being forecast and is later evaluated at realized day-ahead clearing prices; auction bid strategy, partial clearing, and ramp/volume constraints are not modeled (`not stated in source`).
- **Fees / spread / slippage / impact:** price-taking behavior explicitly assumed (Section 7); no market impact, no order-book spread, no latency model. The only modeled frictions are battery round-trip efficiency η² and the fixed round-trip cost C = 25 EUR (investment + O&M + degradation). Imbalance/balancing costs for deviating from the schedule, ancillary-service obligations, and any tax/tariff layer: `not stated in source` — do not read as "zero".
- **Capacity:** 1 MWh battery, single daily cycle, initial state of charge 0; no capacity scaling analysis → `data gap`.
- **Leverage / margin / borrow:** not applicable to the physical-battery formulation as stated; not discussed.
- **Latency / partial fills / failures:** `not stated in source`.
- Whether results survive realistic operational constraints is explicitly flagged as future work by the authors (Section 7).

## Evidence

### Source-reported

All figures below are source-reported from the primary source (arXiv:2609.23223v1) and have not been independently reproduced. Each is tied to its table/section.

1. **Forecast accuracy, Germany, 5-year test (Table 1):** Spread THieF vs corresponding Base — hourly measures improve 1.8%–16.4%, daily-average measures 5.4%–19.7% (Section 6.1). Example cell: Germany ARX Base RMSE 35.92 / MAE 23.65 vs Spread THieF RMSE 30.49 (SS_RMSE 15.1%), SS_dMAE 19.7% (Table 1, Germany block). Even the most accurate backbone improves: TabPFN hourly RMSE −5.9%, dRMSE −7.3% (Table 1).
2. **Forecast accuracy, Spain, 5-year test (Table 1):** hourly measures improve 2.9%–10.7%, daily-average 4.1%–11.1% vs Base (Section 6.1).
3. **Significance (Section 6.1):** multivariate conditional predictive ability tests (Giacomini–White, 24-dimensional daily aggregation, MAE and MSE losses) reject equal predictive ability in favor of Spread THieF vs both Base and Block THieF at the 1% level for every model and both markets (Table 1 caption and Section 6.1).
4. **Total BESS profits, 5-year test (Table 2):** Germany η=1 — Base (hours) NARX 148,743 EUR vs Spread THieF NARX 154,265 EUR; Oracle 166,424 EUR; Naive 132,684 EUR. Spain η=1 — Base (hours) NARX 77,552 EUR vs Spread THieF NARX 81,859 EUR; Oracle 95,336 EUR; Naive 71,072 EUR (Table 2).
5. **Profit gains vs unreconciled hourly forecasts:** "up to 10.4%" (Abstract); consistent with the Table 2 cell Spain, η=0.9, NARX: 47,746 vs 43,261 EUR (+10.4%, computed against Table 2 values). Relative to Block THieF, profit gains range ≈1.1%–9.7% (Section 6.2).
6. **Opportunity cost (Section 6.2):** Spread THieF foregoes ≈7.3%–11.1% of Oracle profit in Germany and 14.1%–22.7% in Spain across models/efficiency levels; vs Block THieF it reduces relative opportunity cost by ≈0.9–6.9 percentage points.
7. **Ranking reversal (Section 6.2):** TabPFN has the best statistical accuracy, yet NARX + Spread THieF yields the highest profit / lowest opportunity cost in all six market-efficiency combinations — better statistical forecasts do not imply better economic decisions (also stated in Abstract and Section 7).
8. **Tail case (Figure 5, Section 6.2):** on 2 July 2023 (German day-ahead minimum −500 EUR/MWh at hour 15, daily average −53.9 EUR/MWh), Base TabPFN sells in hour 15 and loses >300 EUR for the 1 MWh battery; Spread THieF avoids that decision and profits instead.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Not every reconciliation helps:** conventional Block THieF *degrades* TabPFN accuracy in both markets (Germany skill scores −1.1% to −2.0%; Spain −0.1% to −0.8%, Table 1) — the benefit is specific to including spread rows, not to reconciliation per se; a partial-failure datapoint for the broader "hierarchical reconciliation" family.
- **Economic/statistical mismatch:** the statistically best model (TabPFN) is not the most profitable, and rolling ROC diverges from rolling RMSE (Sections 6.1–6.2) — accuracy gains are not a reliable proxy for P&L.
- **Modest and heterogeneous gains:** in some cells the improvement is small (Table 2: Spain η=1, TabPFN 81,000 vs Base 80,410 EUR, ≈+0.7%), while Spain's overall foregone share of Oracle profit reaches 22.7% (Section 6.2).
- **Single-decision tail risk:** one bad hour selection cost Base TabPFN >300 EUR in a single day for a 1 MWh battery (Figure 5) — decision-layer blowups are fat-tailed relative to daily profit.
- **Data-revision sensitivity:** results are not comparable line-for-line with prior THieF/spread papers because ENTSO-E revised historical series (notably German 2024 prices) (Section 3) — replication on a different data vintage can move numbers.
- **Author-flagged limits (Section 7):** price-taking, one cycle per day, fixed round-trip cost; gains under realistic operational constraints are untested.
- No independent replication or contrary published study was found in this run; absence is not evidence of no negative result.

## Falsification plan

Each threshold below is **research-defined** (not from the source) unless noted.

1. **Out-of-sample / regime replication (source's own design):** re-run the rolling 2021–2025 protocol on a fresh period and on a third market (e.g., France/Nordics). Failure rule (research-defined): Spread THieF fails to beat Base on profit in >50% of market-year cells → decision-value claim materially weakened.
2. **Ablation of the spread rows:** compare (a) full Spread THieF, (b) price rows only (Block THieF), (c) shuffled/spread placebo rows with scrambled hour pairs. Failure rule (research-defined): if (a) does not outperform (c), the gain comes from generic combination/regularization, not spread-coherence information.
3. **Backbone robustness:** repeat with at least one additional backbone beyond ARX/NARX/TabPFN-2 (source reports three; research adds a fourth). Failure rule (research-defined): gains < 0 profit delta for the majority of new backbones → architecture-specific artifact.
4. **Cost stress:** vary C (25 EUR) ±50%, add imbalance/balancing penalties and day-ahead bid-ask/curtailment costs, and impose multi-cycle/degradation constraints (source explicitly defers these). Failure rule (research-defined): the Base-vs-Spread profit gap disappears or inverts under realistic cost add-ons → not tradable value.
5. **Data-vintage audit:** rebuild on a fresh ENTSO-E download and on an independent vendor. Failure rule (research-defined): sign flip of the profit delta between vintages → fragile to data revision.
6. **Oracle-relative floor:** track ROC (source's own metric, Eq. 32). Failure rule (research-defined): Spread THieF's ROC advantage vs Base < 1 percentage point averaged over the new sample → economically immaterial.
7. **Capacity/impact:** irrelevant at 1 MWh price-taking scale in the source; must be re-decided (research-proposed) before any scaled deployment.
Action on failure: retain the record as research-only; do not advance to implementation candidates; record negative evidence in this record rather than retuning.

## Crypto portability

**adapted** — the source demonstrates the mechanism only in European day-ahead electricity; it contains no crypto evidence, so this is a ported hypothesis, not crypto empirical evidence.

- **What ports:** the general claim — jointly reconciling forecasts of price levels and pairwise intra-period spreads improves spread-capture *decisions* — maps naturally to crypto structures with explicit spread/basis economics: perpetual-vs-spot basis capture, cross-exchange funding/basis carry, intra-day range (high–low) capture for volatility-selling or inventory timing. Crypto analog of C (round-trip physical cost) = fees + spread + slippage + funding paid during the holding window; analog of η² = round-trip friction factor.
- **What does not port directly:** physical one-cycle-per-day battery constraint; ENTSO-E load/renewable features; day-ahead auction gate timing.
- **Crypto-specific risks:** 24/7 sessions and candle-boundary conventions (no auction close), venue fragmentation and per-venue settlement times, funding payments as a path-dependent carry cost, index/mark vs last-price divergence, and much higher data-vintage/virtual-asset revision risk (delistings, relisted contracts, survivorship).
- No crypto backtest of this reconciliation layer exists anywhere in our stack; portability remains unproven.

## Limitations

- **Source status:** unpublished arXiv preprint (v1, 2026-09-19); not peer-reviewed as of capture.
- **Stylized strategy:** price-taking, single daily cycle, fixed C, 1 MWh; explicitly acknowledged by the authors (Section 7). Execution realism (imbalance costs, bid strategy, ramps) is `not stated in source`.
- **`data gap`:** publication/availability timestamps (forecast vs gate closure), delivery-timezone/DST convention, and missing-data treatment are not stated in source.
- **Universe narrowness:** two European markets, wholesale day-ahead only; no options/forward hedging layer.
- **Not independently reproduced**; ENTSO-E revisions make exact numeric replication vintage-dependent.
- **Publication-bias / framing:** the paper compares its own method against its own baselines; the Oracle bound shows large residual foregone profit (up to 22.7% in Spain).
- **Incremental scope:** the claim is about the reconciliation layer's decision value, not about electricity trading being generally profitable.
- **Crypto porting is `adapted`, not `direct`.**

## Implementation status

`not-implemented`. No implementation, backtest, prototype, paper trading, or validation exists in our research stack; nothing in Qlib, Paper, Testnet, or Live has been touched by this record.

## Adoption boundary

This record is research material only. Its presence in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading.

## Related Wiki records

- No Hermes Wiki Brain record for electricity price forecasting, THieF/forecast reconciliation, or battery arbitrage was found on a full-tree search of `~/.hermes/wiki` (2026-09-22); no such Wiki link is asserted rather than fabricate one.
- `[[quant/crude-oil-crack-spread-seasonally-adjusted-mean-reversion-stop-lockout-2026-09-12]]` — related family: commodity spread (crack spread) capture with seasonality adjustment; distinct mechanism and universe.
- Repo-adjacent records (same repository, different sources): `commodity-soybean-crush-spread-cointegration-stat-arb-2026-09-12` (spread-based commodity arbitrage), `forecast-to-fill-gold-futures-friction-adjusted-kelly-alpha-2026-09-02` (forecast→fill decision value with frictions), `coffee-commodity-weather-stress-lagged-overlay-2026-09-12` (physical-driver overlay on a commodity). None of these share this source identity or the spread-reconciliation mechanism.

## Sources

1. Lipiecki, A., Kourentzes, N., & Weron, R. (2026). "Stealing profits: Spread-based temporal hierarchy forecasting for day-ahead electricity markets." arXiv:2609.23223v1 [q-fin.ST], submitted 19 September 2026. https://arxiv.org/abs/2609.23223 (full text: https://arxiv.org/html/2609.23223v1). All quantitative claims above trace to Table 1, Table 2, Figures 3–5, Sections 2–7 of that preprint; all are labeled source-reported.
2. Data sources cited by the primary paper (used by it, not directly by us): ENTSO-E Transparency Platform (https://transparency.entsoe.eu) and Investing.com — referenced for provenance of the paper's inputs only.
