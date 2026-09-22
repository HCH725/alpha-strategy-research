---
schema: strategy-research-record-v1
title: "OrderFusion+ Side-Specific Probabilistic Buy–Sell Price Trajectory Forecasting from Intraday Electricity Orderbooks with Dynamic Window/Neighbor Masking"
created: 2026-09-22
updated: 2026-09-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - electricity
  - intraday-markets
  - orderbook
  - microstructure
  - probabilistic-forecasting
  - deep-learning
  - quantile-forecasting
status: research-only
confidence: medium
source_as_of: 2026-09-20
sources:
  - "https://arxiv.org/abs/2609.23598"
  - "https://arxiv.org/html/2609.23598v1"
  - "https://runyao-yu.com/OrderFusion/"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# OrderFusion+ Side-Specific Probabilistic Buy–Sell Price Trajectory Forecasting from Intraday Electricity Orderbooks with Dynamic Window/Neighbor Masking

## Provenance

- **Paper:** Runyao Yu and Derek W. Bunn, "OrderFusion+: Probabilistic Buy–Sell Price Trajectory Forecasting in Intraday Electricity Markets."
- **Preprint:** arXiv:2609.23598v1 [q-fin.CP] (subjects field on the landing page shows only Computational Finance, q-fin.CP), submitted Sunday, 20 September 2026, 12:33:57 UTC (v1; no later version as of capture).
- **Author affiliations (exactly as source):** Runyao Yu — ¹London Business School (London, United Kingdom), ²Delft University of Technology (Delft, Netherlands), ³Austrian Institute of Technology (Vienna, Austria); Derek W. Bunn — ¹London Business School.
- **Stable URLs:** abstract https://arxiv.org/abs/2609.23598 ; full text https://arxiv.org/html/2609.23598v1 ; canonical DOI https://doi.org/10.48550/arXiv.2609.23598 (arXiv-issued DataCite identifier only).
- **Publication status:** preprint; arXiv landing page shows Comments "10 pages, 7 figures, 5 tables" and **no journal reference** (checked 2026-09-22); not peer-reviewed as of capture. License CC BY 4.0 (stated in the HTML full text).
- **Code/forecasts:** https://runyao-yu.com/OrderFusion/ (open-source implementation and forecasts, source-reported; not independently executed in this run).
- **Data as-of:** commercial German EPEX SPOT continuous intraday orderbook; training folds start 2022.01, test windows collectively cover calendar year 2024 (Table 2).
- **Primary-source checksum (2026-09-22):** opened the arXiv landing page and the full HTML text of v1 and verified there: exact author list/order and affiliations; version/date (v1, 20 Sep 2026 12:33:57 UTC); Comments field; no journal-ref; sample period and universe (German 15-minute continuous intraday products, train 2022.01–2024.04 rolling, tests 2024.01–2024.12 in three folds, Table 2); transaction-cost treatment (**none — the paper reports no trading simulation, no costs, no fills**; Sections 5–6 are forecast-accuracy evaluation only); and every performance number below with its Table/Figure/Section location. Fields not verifiable from the primary text are marked `data gap` / `not stated in source`.
- **Source-identity deduplication (2026-09-22, whole-repo ripgrep across all `*.md`):** zero prior records cite `2609.23598`, `OrderFusion`, `OrderFusion+`, `Runyao Yu`, `Derek W. Bunn`, `EPEX`, or "German intraday". The only other electricity record in the repository, `electricity-spread-thief-forecast-reconciliation-bess-arbitrage-2026-09-22.md` (Lipiecki, Kourentzes & Weron, arXiv:2609.23223), is a different source identity, a different market stage (day-ahead hourly auction vs. continuous intraday 15-minute), and a different mechanism (temporal-hierarchy forecast reconciliation of price/spread series vs. orderbook deep learning with side-specific cross-attention and dynamic input masking) — materially distinct on mechanism, signal construction, and universe/market stage.

## Economic mechanism

### Source-reported

The paper's thesis is a forecasting claim: in the continuous intraday electricity market, the *micro-level buy–sell orderbook interactions* of the target 15-minute delivery product **plus its neighboring delivery products** carry short-horizon predictive information about the remaining price path that aggregate price histories and macro-features do not capture (Sections 1–3). Specific source-reported statements:

- Buyers respond to sellers' prices/volumes and vice versa; the model therefore fuses the two sides with cross-attention so each side's representation is contextualized by the other (Section 3.1, "Buy–Sell Fusion Layer").
- Products with different delivery times trade in parallel; orders placed far from delivery reflect expectations about near-future market conditions, and BESS arbitrage/load shifting increasingly connects neighboring products (Section 2.1, citing Cao et al. 2020, Hirsch & Ziel 2024).
- Compressing the final three/two/one hours into the ID3/ID2/ID1 VWAP indices discards the intra-window price trajectory and buy–sell dynamics; forecasting side-specific 15-minute VWAP trajectories retains them (Section 2.2).
- Empirical findings (Section 6.2, Figure 6): the dynamically sampled input window and neighbor count vary by origin and side — the most frequently selected historical window is 30 minutes (63% of test samples; 65% for the second random seed, Appendix B) and the most frequently selected number of neighboring products is **zero (47%)**; as delivery approaches (origin −180 → −60 min) the modal window shortens from 30 to 15 minutes. The source interprets this as predictive information concentrating in the most recent transactions and as evidence that a static window/neighborhood assumption is insufficient.
- Source-reported benchmark context: generic pretrained foundation models (TimesFM 3.0, Chronos 2.0, TabPFN-TS, Moirai 2.0) do **not** significantly beat a simple 30-minute VWAP persistence baseline (TabPFN-TS vs Persistence-2, one-sided DM p ≥ 0.05 in AQL, Fig. 4), so domain-specific orderbook training remains necessary (Section 6.2, Section 7).

### Research interpretation

Falsifiable mechanism statement: **side-asymmetric orderbook flow at short horizons is conditionally persistent and neighbor-product order flow adds incremental information**, so a model that conditions the buy side on the sell side (and vice versa) and adaptively selects lookback/neighborhood produces better-calibrated probabilistic forecasts of the remaining pre-delivery price path than price-history persistence or domain-agnostic models. Component roles (this is a forecasting pipeline; the trading layer below is research-proposed):

```text
Regime: none required by the source (no regime filter; the dynamic mask is an input-selection mechanism, not a tradability regime gate)
Primary signal: quantile trajectories (0.1/0.5/0.9) of side-specific 15-minute VWAPs over the final 180 minutes before delivery
Confirmation (research-proposed): agreement between buy-side and sell-side trajectory direction, or persistence of the modal 15/30-minute window choice
Decision layer (research-proposed): threshold rule translating forecast trajectories into intraday buy/sell position changes — NOT specified by the source
Risk / exit (research-proposed): flat at delivery gate closure (Germany: main-market cutoff 30 min before delivery, then TSO control-area trading until 5 min before delivery)
```

The alpha claim under test is narrow: *orderbook microstructure information improves decision-relevant short-horizon trajectory forecasts in the continuous intraday market*. The source itself conducts **no trading backtest** — any P&L claim is a ported hypothesis (see Evidence and Falsification plan).

## Signal

All operational choices in this section are **source-reported** unless explicitly marked research-proposed/research-defined.

- **Formation timestamp:** forecasts are produced at origins −180, −120, and −60 minutes relative to delivery time `t_d` of a 15-minute delivery product; each origin maps to a forecast length of 180/120/60 minutes of 15-minute VWAP steps (Section 6.1). Inputs use only orders/trades observed before the origin (rolling design, Table 2 folds). `data gap`: the paper does not restate the exact exchange timestamp convention/timezone for order timestamps or state whether order arrivals exactly at the origin minute are included; German EPEX sessions are local time with DST — timezone/DST handling `not stated in source`.
- **Targets (signal construction):** side-specific 15-minute VWAP sequences `Y(+)` (buy side) and `Y(−)` (sell side) from origin to delivery; the final 15-minute interval contains trades only up to `t_d − 5 min` because no trades occur in the final 5 minutes before delivery (Section 2.2, Eqs. 2–3).
- **Lookback / inputs:** historical window and neighboring-product coverage both span up to 180 minutes (Section 6.1); input features = price, traded volume, time position, product position, plus calendar embedding (quarter-hour index, day of week, month, holiday flag, Eqs. 4–5). Candidate window set `W = {15, 30, 60, 120, 180}` minutes × candidate neighbor counts `N = {0, 1, 2, 4, 8, 12}` form a 30-mask bank (Table 4: full configuration uses 180 minutes / 12 neighbors as maximum support; the dynamic mask selects a subset per sample). Missing trade intervals are handled by a missing-value mask `B` (Eq. 12); no imputation described.
- **Model:** 2D-conv projection → side-specific cross-attention (query = own side, key/value = opposite side, two weight-sharing passes: missing-value mask, then sampled dynamic mask) → mask-normalized aggregation → concat with calendar embedding → dense head emitting `L × Q` quantiles, `Q = {0.1, 0.5, 0.9}` (Sections 3.1–3.2, Table 4). Training loss = masked Average Quantile Loss (AQL, Eqs. 19–20); training settings: 350 epochs, batch 4,096, Adam, lr 1e−3, standard scaler, best validation loss (Appendix C).
- **Sampling rule:** during training the dynamic mask is drawn from the softmax distribution over the 30-mask bank; deterministic inference uses the highest-probability candidate per side (Section 3.1, Eqs. 13–14).
- **Long entry / short entry / exit / holding period (trading layer):** `not stated in source` — the paper reports no entry, exit, holding-period, sizing, or rebalancing rule. The only timing constraints stated are market rules: continuous trading for 15-minute products opens 15:00 on the previous day (Germany), main-market cutoff `t_d − 30 min`, TSO control-area trading until `t_d − 5 min`, no trades in the final 5 minutes (Section 2.1).
  - *Research-proposed (not source-reported):* e.g., take a long intraday position when the predicted median buy-side trajectory over the remaining window rises by more than a threshold set to exceed fees + spread + expected slippage, flip/short on the mirror condition on the sell-side trajectory, and flatten at `t_d − 30 min` (or `t_d − 5 min` in the control area). Threshold, sizing, and stop rules are entirely **research-proposed** and have no source support.
- **Parameters (all source-reported):** aggregation interval 15 min; historical window 180 min max; neighbors 12 max; hidden dimension 36 (selected from {18, 36, 72}); cross-attention heads 2 (from {1, 2, 4}); activation Swish (from {ReLU, Swish}); 30 dynamic masks; quantiles {0.1, 0.5, 0.9} (Tables 4–5). Baseline hyperparameters per Table 5; fully trained models: 350-epoch budget, lowest-validation-loss checkpoint.
- **Reconstruction status:** the *forecasting* pipeline is fully specified and open-sourced; the *trading* rule is absent from the source — any strategy built on these forecasts is underspecified until its decision layer is defined and labeled research-proposed.

## Required data

- **Instrument / universe:** German (EPEX SPOT) continuous intraday electricity, 15-minute delivery products (the most volatile and "most interesting to traders", Section 6.1). Market coupling means the German orderbook also contains orders from France, Austria, the Netherlands, and Norway (Section 6.1, citing Cary & Morstyn 2026).
- **Venue / market type:** EPEX SPOT continuous intraday (physical wholesale power, continuous matching); no crypto exposure of any kind.
- **Timeframe:** 15-minute order/trade aggregation; forecast origins at −180/−120/−60 min before delivery; spans 2022.01 (training start) through 2024.12 (final test fold).
- **Fields:** per side (+/−): traded price, traded volume, time position, product position; calendar (quarter-hour, day of week, month, holiday); delivery time `t_d`. Macro-features (renewable generation, load, weather) are explicitly *not* inputs; the source notes prior evidence that they add nothing beyond orderbook-derived prices (Janke & Steinke 2019, cited in Section 1).
- **Point-in-time:** rolling three-fold train/validation/test design with expanding training windows (Table 2: fold 1 train 2022.01–2023.08 / val 2023.09–2023.12 / test 2024.01–2024.04; fold 2 train 2022.01–2023.12 / val 2024.01–2024.04 / test 2024.05–2024.08; fold 3 train 2022.01–2024.04 / val 2024.05–2024.08 / test 2024.09–2024.12); tests collectively cover full-year 2024. Inputs restricted to pre-origin observations. `data gap`: no explicit leakage audit discussion beyond the fold design.
- **Timestamp / timezone:** `not stated in source` — exchange timestamp convention, timezone, and DST handling are not restated in the paper.
- **Missing data:** missing trade intervals are masked (0 = no trade in that interval-product cell, Eq. 12); targets missing from either side are excluded from the loss numerator and denominator (Section 3.3); imputation not described.
- **Acquisition cost / availability:** the orderbook is **commercial** — German "Continuous Anonymous Orders History" from EPEX SPOT via the EEX Group webshop at **€3,900 per calendar year for internal use (€325 per month)** (Appendix A). This is a material data-access barrier and must not be read as free public data.
- **Funding/fee/spread needs:** `not stated in source` — the paper models no fees, spreads, funding, or slippage because it performs no trading simulation.

## Execution assumptions

- **Signal-to-order timing:** `not stated in source` (no trading layer exists in the paper).
- **Order type / fill model:** `not stated in source`. Market micro-facts that a replication must model: continuous matching, country cutoff (Germany 30 min before delivery), TSO control-area trading until 5 min before delivery, no trades in the final 5 minutes (Section 2.1) — these are market rules from the source, not fill assumptions.
- **Fees / spread / slippage / impact:** **none modeled — the source contains no transaction-cost, bid-ask spread, latency, or market-impact treatment anywhere in Methods/Experiments (Sections 3–6).** Do not read this as "costs are zero"; it is a forecast-accuracy study. Any claim that these forecasts are tradable net of costs is untested.
- **Capacity / liquidity:** `not stated in source`; the paper motivates the final-hour volatility/imbalance pressure (Section 1) but performs no participation or depth analysis.
- **Leverage / margin / borrow:** `not stated in source` (single-product forecast study).
- **Latency / partial fills / failures:** `not stated in source`; the model itself is real-time capable (inference < 1 second, Appendix D), but order-path behavior is unexamined.
- **Position limits / sizing:** `not stated in source`.
- Whether these forecasts survive realistic execution frictions is **not addressed by the source** and is the central open question for any adoption decision.

## Evidence

### Source-reported

All figures below are source-reported from the primary source (arXiv:2609.23598v1) and have not been independently reproduced. Each is tied to its table/figure/section. All are **forecast-accuracy metrics, not P&L**.

1. **Headline test performance, averaged over the three forecast origins (Table 3):** OrderFusion+ AQL **10.62**, AQCE 2.29%, AQCR **0.00%**, MAE **28.04**, RMSE **101.76**, R² **0.39** — best among all models in AQL, MAE, RMSE, and R², with zero quantile crossing (Section 6.2).
2. **Persistence baselines (Table 3):** Persistence-1 (15-min VWAP) AQL 12.87 / MAE 32.23 / RMSE 111.25 / R² 0.23; Persistence-2 (30-min VWAP, the strongest) AQL 12.07 / AQCE 0.33% / MAE 30.71 / RMSE 105.55 / R² 0.32; Persistence-3 (60-min) AQL 21.00 / R² −1.22; Persistence-4 (previous-day trajectory) AQL 21.95 / R² −0.59 (Table 3).
3. **Fully trained baselines (Table 3):** LQR AQL 15.85 / R² 0.26; MLP 13.93 / 0.32; LSTM 11.79 / 0.35; Transformer 11.72 / 0.34. LSTM and Transformer AQL are ≈9.4% higher than OrderFusion+ (Section 6.2), indicating that losing the product-dimension structural prior matters.
4. **Foundation-model baselines zero-shot (Table 3):** TimesFM 3.0 AQL 14.85 / AQCE 5.74% / R² 0.15; Chronos 2.0 AQL 19.05 / R² 0.33; TabPFN-TS AQL 12.05 / **AQCE 8.62%** / R² 0.36; Moirai 2.0 AQL 17.66 / R² 0.22. TabPFN-TS does not significantly beat Persistence-2 in AQL (one-sided DM p ≥ 0.05, Fig. 4) and shows large coverage error (Section 6.2).
5. **Statistical significance (Fig. 4, Section 6.2):** one-sided Diebold–Mariano tests on per-delivery AQL differentials (HAC variance, Harvey et al. 1997 small-sample correction) show OrderFusion+ significantly more accurate than **every** baseline at p < 0.05; per-origin AQL comparison confirms OrderFusion+ wins at all three origins (Figure 5).
6. **Dynamic-mask distribution (Fig. 6, Section 6.2):** modal historical window = 30 min (63% of samples), modal neighbor count = 0 (47%); window shifts 30 → 15 min as delivery approaches; masks are sampled asymmetrically across buy/sell sides. Second seed (Appendix B): modal window 30 min ≈65% of samples.
7. **Rashomon robustness (Appendix B):** a second random seed gives AQL 10.70 vs 10.62 with p > 0.05 (not significantly different) while producing a *different* mask distribution — performance replicates, mask-based "market condition" interpretation does not fully.
8. **Cost/efficiency of the model (Appendix D):** 41,124 / 38,508 / 35,892 trainable parameters for the −180/−120/−60-min origins; ~25–35 min training per model on one NVIDIA A100 (Google Colab); inference < 1 second.

### Independently reproduced

Not independently reproduced. The open-source implementation at https://runyao-yu.com/OrderFusion/ was not executed in this run; commercial orderbook data (EEX webshop, €3,900/year) was not acquired.

### Negative evidence

- **No trading evidence at all:** the source reports zero backtests, zero P&L, zero Sharpe/win-rate/drawdown, and zero transaction-cost modeling (Sections 5–6 are forecast metrics only). Any "this beats costs" claim would be fabricated — the tradability question is completely open.
- **Persistence is uncomfortably close:** Persistence-2 (a 30-minute VWAP) reaches AQL 12.07 vs 10.62 and even beats OrderFusion+ on AQCE (0.33% vs 2.29%) (Table 3). The economic margin of the deep model over the simplest baseline is modest in absolute terms, and the source's own dynamic-mask analysis shows the model itself usually selects a 30-minute window and **zero** neighbors (63% / 47%, Fig. 6) — i.e., the two headline innovations (neighbor products, long histories) are frequently *not* used.
- **Foundation models fail the efficiency test:** none of TimesFM 3.0 / Chronos 2.0 / TabPFN-TS / Moirai 2.0 significantly beats Persistence-2 (Fig. 4) — negative evidence for the "zero-shot foundation model replaces domain training" thesis in this domain (source-reported).
- **Interpretability instability:** the Rashomon result (Appendix B) shows mask distributions — the paper's window into "dynamic market conditions" — differ across seeds with indistinguishable AQL. Do not build regime claims on mask frequencies without seed-robustness checks.
- **Coverage calibration gap:** OrderFusion+ AQCE (2.29%) is worse than all persistence baselines (0.33–0.70%) (Table 3) — better scores but worse interval coverage than naive baselines, which matters if a trading rule consumes the 0.1/0.9 quantile bands.
- **Single-market, single-year test:** Germany only, 15-minute products, test year 2024 (Section 7 explicitly flags generalization to other markets as future work); no regime breakdown (e.g., negative-price hours, Dunkelflaute episodes) is reported — `data gap`.
- **Data-access barrier:** commercial orderbook at €3,900/year (Appendix A) limits independent replication and excludes the public-data replication path common to most records here.
- No independent replication or contrary published study on OrderFusion+ was found in this run; absence is not evidence of no negative result.

## Falsification plan

Each threshold below is **research-defined** (not from the source) unless noted.

1. **Forecast-layer replication (source's own design):** re-run the three-fold 2024 protocol with the open-source code on the same commercial data. Failure rule (research-defined): OrderFusion+ fails to beat Persistence-2 by ≥5% relative AQL in the majority of folds → core claim weakened.
2. **Decision-layer backtest (research-proposed, the missing link):** attach the pre-declared threshold rule from the Signal section (research-proposed) and backtest intraday position changes, filling at next 15-minute interval VWAP with fees + spread + slippage charged. Failure rule (research-defined): net Sharpe ≤ 0 over the 2024 test year, or net edge indistinguishable from the Persistence-2-driven rule → forecasts have no tradable value beyond the naive baseline.
3. **Ablation:** (a) full OrderFusion+, (b) price-history only (mask neighbor count fixed at 0), (c) single-side attention (no buy–sell fusion), (d) shuffled-side placebo (pair buy side of product A with sell side of a random other product). Failure rule (research-defined): if (a) does not outperform (d), the "buy–sell interaction" mechanism is not load-bearing — gains come from generic smoothing.
4. **Foundation-model challenge:** add newer zero-shot models beyond the four tested. Failure rule (research-defined): any zero-shot model significantly beats OrderFusion+ in AQL (DM p < 0.05) → domain-specific orderbook training claim fails.
5. **Cost/latency stress (research-proposed):** escalate assumed round-trip cost from 0 to levels observed in wholesale power intraday markets; sweep signal-to-order delay 0–15 minutes. Failure rule (research-defined): net edge of the decision layer hits zero before a 5-minute delay → not implementable.
6. **Cross-market generalization (source-flagged limitation):** repeat on a second EPEX market (e.g., France or Netherlands) and on hourly products. Failure rule (research-defined): OrderFusion+ loses to Persistence-2 in >50% of market-product cells → Germany-2024 artifact.
7. **Calibration-first falsification:** if a trading rule consumes the 0.1/0.9 bands, first test empirical coverage per hour-to-delivery bucket. Failure rule (research-defined): coverage deviation worse than persistence in any bucket → band-based entry rules are invalid regardless of AQL.
8. **Regime breakdown:** report metrics separately for negative-price hours and high-net-load-ramp hours (research-proposed slices; the source reports none). Failure rule (research-defined): the AQL advantage vanishes in the economically most valuable hours → selection-value claim weakened.
Action on failure: retain the record as research-only; do not advance to implementation candidates; record negative evidence in this record rather than retuning thresholds post hoc.

## Crypto portability

**adapted** — the source demonstrates the mechanism only in German wholesale electricity; it contains no crypto evidence, so this is a ported hypothesis, not crypto empirical evidence.

- **What ports:** the general claim — side/order-flow-conditioned probabilistic short-horizon trajectory forecasting from full orderbook micro-features beats price-history persistence — is venue-agnostic in form and could be tested on crypto perpetual orderbooks (15-minute horizon, buy/sell imbalance conditioning, neighbor-contract information such as quarterly futures or BTC-vs-ETH lead). The repo already contains crypto LOB/queue-imbalance records that study adjacent mechanisms (see Related records).
- **What does not port directly:** electricity's delivery-convergence economics — prices and uncertainty mechanically tighten toward `t_d` because the physical product must balance; there is no delivery countdown anchor in 24/7 crypto perps, so the "window shortens as delivery approaches" dynamic (Fig. 6) has no counterpart and must be re-derived. Parallel neighboring-product structure maps imperfectly: crypto has expiries (quarterlies) but they are far less liquid intra-day than adjacent electricity delivery products.
- **Crypto-specific risks:** 24/7 sessions and candle-boundary conventions (no auction/cutoff cascade), venue fragmentation and per-venue orderbook asymmetry, funding payments as path-dependent carry during any holding window, mark/index vs last-price divergence, taker/maker fee tiers and liquidation mechanics, and survivorship from delisted contracts. Commercial-data availability is *better* in crypto (public L2 feeds) but microstructure is noisier (spoofing, layering) than the anonymous wholesale power book.
- No crypto backtest of this mechanism exists in our stack; portability remains unproven.

## Limitations

- **Source status:** unpublished arXiv preprint (v1, 2026-09-20); not peer-reviewed as of capture; Comments state 10 pages / 7 figures / 5 tables (concise format).
- **No trading layer:** entry/exit/sizing/costs/fills are `not stated in source` — the paper is a forecasting benchmark only; tradability is entirely open.
- **`data gap`:** timezone/DST and order-timestamp conventions, leakage-audit detail beyond fold design, regime breakdowns, and capacity/liquidity are not stated in source.
- **Universe narrowness:** German market, 15-minute products, test year 2024; no cross-market or cross-product generalization (author-acknowledged, Section 7).
- **Mask-bank empiricism:** candidate grid `W × N` is empirical (author-acknowledged, Section 7); finer grids might change results; mask-based market-condition readings are seed-unstable (Appendix B).
- **Weather/macro features unresolved:** whether weather-forecast information is already fully reflected in prices is explicitly left unclear by the authors (Section 7).
- **Commercial-data dependency:** €3,900/year German orderbook (Appendix A) — replication requires paid data.
- **Not independently reproduced;** all performance figures are third-party source-reported forecast metrics.
- **Publication-bias / framing:** the paper benchmarks its own model against its own baseline suite; the persistence baseline is close (AQL 12.07 vs 10.62) and beats it on coverage — treat headline "outperforms all baselines" accordingly.
- **Crypto porting is `adapted`, not `direct`.**

## Implementation status

`not-implemented`. No implementation, backtest, prototype, paper trading, or validation exists in our research stack. Nothing in Qlib, Paper, Testnet, or Live has been touched by this record; the source's own code at https://runyao-yu.com/OrderFusion/ was not run here.

## Adoption boundary

This record is research material only. Its presence in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading.

## Related Wiki records

- No Hermes Wiki Brain record for electricity price forecasting, intraday power markets, EPEX orderbooks, or OrderFusion was found on a full-tree search of `~/.hermes/wiki` (2026-09-22); no Wiki link is asserted rather than fabricate one.
- Repo-adjacent records (same repository, different sources and mechanisms):
  - `electricity-spread-thief-forecast-reconciliation-bess-arbitrage-2026-09-22` — arXiv:2609.23223; day-ahead hourly **auction** market, temporal-hierarchy forecast reconciliation for battery arbitrage. Same asset class, different market stage and mechanism.
  - `btc-usdt-l2-queue-imbalance-short-horizon-ic-economics-gap-2026-09-19` — crypto L2 queue-imbalance short-horizon predictive IC with thin execution economics; the closest crypto analog of the orderbook-microstructure→short-horizon-forecast mechanism.
  - `crypto-short-horizon-15min-mean-reversion-taker-flow-2026-09-01` — 15-minute-horizon crypto mean reversion conditioned on taker flow (side-conditioned short-horizon signal in a different market).
  - `edgeflow-composite-lob-microstructure-alpha-binance-spot-2026-09-09` — composite LOB microstructure alpha on Binance spot (orderbook-feature ML family, crypto).
  - `multi-horizon-esn-intraday-return-prediction-2026-09-06` — intraday return prediction across horizons via reservoir computing (forecasting-model family, equities).
  None of these share this source identity, and none studies side-specific buy–sell trajectory forecasting with dynamic input masking in a delivery-driven market.

## Sources

1. Yu, R., & Bunn, D. W. (2026). "OrderFusion+: Probabilistic Buy–Sell Price Trajectory Forecasting in Intraday Electricity Markets." arXiv:2609.23598v1 [q-fin.CP], submitted 20 September 2026. https://arxiv.org/abs/2609.23598 (full text: https://arxiv.org/html/2609.23598v1; DOI: https://doi.org/10.48550/arXiv.2609.23598). All quantitative claims above trace to Tables 1–5, Figures 1–7, Sections 1–7, and Appendices A–D of that preprint; all are labeled source-reported.
2. Implementation and forecasts referenced by the primary paper (used by it, not directly by us): https://runyao-yu.com/OrderFusion/.
3. Data vendor referenced by the primary paper (used by it, not directly by us): EPEX SPOT "Continuous Anonymous Orders History" via the EEX Group webshop, €3,900/calendar year internal use (Appendix A of the primary paper).
