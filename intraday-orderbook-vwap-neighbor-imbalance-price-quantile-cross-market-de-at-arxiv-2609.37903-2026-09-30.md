---
schema: strategy-research-record-v1
title: "Intraday Orderbook VWAP with Neighboring-Product Context as a Probabilistic Imbalance-Price Signal (Germany and Austria Cross-Market)"
created: 2026-09-30
updated: 2026-09-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - electricity
  - intraday-markets
  - balancing-market
  - orderbook
  - probabilistic-forecasting
  - quantile-forecasting
  - cross-market
status: research-only
confidence: medium
source_as_of: 2026-09-29
sources:
  - "https://arxiv.org/abs/2609.37903"
  - "https://arxiv.org/pdf/2609.37903"
  - "https://doi.org/10.48550/arXiv.2609.37903"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Section IV-A prose states that VWAP-Neighbor has the lowest AQL, MAE, and RMSE at every horizon in both countries, but Table IV (Austria) at horizon 15 min prints RMSE 332.64 for VWAP-Neighbor against 331.60 for LMP-Neighbor, so the literal lowest-RMSE claim fails in 1 of the 18 horizon-by-metric cells it covers; recorded as an unreconciled source-internal contradiction and the table cells are treated as truth."
---

# Intraday Orderbook VWAP with Neighboring-Product Context as a Probabilistic Imbalance-Price Signal (Germany and Austria Cross-Market)

## Provenance

- **Paper:** Runyao Yu, Jochen L. Cremer, Pierre Pinson, Jalal Kazempour, Leo Semmelmann, Takuji Matsumoto and Derek W. Bunn, "From Intraday Orderbook to Imbalance Price: Understanding Cross-Market Interaction."
- **Author list (exactly as printed on page 1 and in the PDF `/Author` metadata):** Runyao Yu; Jochen L. Cremer; Pierre Pinson; Jalal Kazempour; Leo Semmelmann; Takuji Matsumoto; Derek W. Bunn. Seven authors, identical ordering in the landing-page `citation_author` meta tags, the PDF title block and the PDF `/Author` field.
- **Affiliations (page-1 footnote, exactly as source):** 1 London Business School; 2 Delft University of Technology; 3 Austrian Institute of Technology; 4 Imperial College London; 5 Technical University of Denmark; 6 Karlsruhe Institute of Technology; 7 Institute of Science Tokyo. Superscripts: Yu 1,2,3; Cremer 2,3; Pinson 4; Kazempour 5; Semmelmann 6; Matsumoto 7; Bunn 1.
- **Preprint:** arXiv:2609.37903v1 [q-fin.CP]; submission history shows `[v1] Tue, 29 Sep 2026 16:02:35 UTC (13,801 KB)`; the arXiv API returns a single entry with `published` = `updated` = `2026-09-29T16:02:35Z` (the `2026-09-30T07:01:34Z` value in the same response is the feed-level `<updated>` of the query response, not a second version), so v1 is the only version as of capture.
- **Subjects:** primary Computational Finance `q-fin.CP`, cross-list Computational Engineering, Finance, and Science `cs.CE`; no other subject.
- **Comments field:** `10 pages, 11 figures, 5 tables`.
- **Publication status:** **preprint only.** The landing-page metatable carries no Journal-reference row and no external DOI row; the arXiv API returns no `arxiv:journal_ref` and no `arxiv:doi`; the word `peer` appears 0 times in the pinned text. The DOI is the arXiv-issued DataCite value `10.48550/arXiv.2609.37903` and the landing page prints the tooltip `arXiv-issued DOI via DataCite (pending registration)`.
- **Licence:** CC BY 4.0 (landing page shows the `view license` div; PDF `/License` field carries the Creative Commons attribution URL for 4.0).
- **Stable URLs:** abstract `https://arxiv.org/abs/2609.37903`; PDF `https://arxiv.org/pdf/2609.37903`; DOI `https://doi.org/10.48550/arXiv.2609.37903`; API `https://export.arxiv.org/api/query?id_list=2609.37903`.
- **Primary-source checksum (fetched 2026-09-30):**
  - PDF: **17,211,615 bytes**, SHA-256 `99c9497fc3b27d88a7b4bf77c360015186daf0b605a9868b2d322696073ca687`, extracted with pypdf 6.16.2 into **10 pages / 50,630 characters / 1,523 lines**, read end to end covering the Abstract, Sections I-VI, Tables I-V (every printed cell), the captions of Figures 1-11, Appendices A-B (data sources and ANN hyperparameter search ranges) and the 34-item reference list. PDF `/Title` is byte-identical to the printed title, `/arXivID` is `https://arxiv.org/abs/2609.37903v1`.
  - Landing page: **44,066 bytes**, SHA-256 `4ac2a63bdced0dd34944f96a58eaf0faf7b327660c23b04e536efbc8260a5866` - used for the seven `citation_author` tags, `citation_date 2026/09/29`, the dateline, the Comments and Subjects cells, the absence of a Journal-reference cell, the DataCite-pending tooltip and the licence div.
  - API: **3,616 bytes**, SHA-256 `6a0a55aa4add7e92f02e60357df663c1b3d931b65b215c32611226587c7f525f` - single `<entry>`, `published` = `updated` = `2026-09-29T16:02:35Z`, comment `10 pages, 11 figures, 5 tables`, no `journal_ref`, no `doi`.
  - **Text-layer caveats recorded, not reconciled:** (a) PDF bold formatting is lost on extraction, so the *bold* membership of the "statistically strongest group" in Tables III-IV is **not recoverable** - only the printed `Count` column is verifiable; (b) bar values, axis ticks and per-panel labels of Figures 4-11 are only partly coherent in the text layer, so this record cites figure content only through the paper's own prose statements and never through cell values; (c) the concatenated decimal runs in Tables III-IV (for example `30.51 0.040 91.67`) were split on the AQCE-position anchors, and every row was re-checked to contain exactly 12 numbers plus its `x/12` Count.
- **Data as-of:** continuous intraday orderbook from **EPEX SPOT** (commercial; Appendix A states it is purchasable through the EEX Group Webshop under EPEX SPOT public market data products, price **not stated in source**, and available in real time through the corresponding API services); fundamental features and imbalance prices from the **ENTSO-E Transparency Platform**; Germany and Austria, **January 2022 through January 2025** (Section II); all test folds fall in calendar year 2024 (Table I).
- **Cost/slippage treatment - determined at Methods level**, by reading Sections II (Data), III (Method, including III-A models, III-B orderbook representation, III-C feature sets, III-D evaluation metrics), IV (Case study, A-C), V (Limitations), VI (Conclusion) and Appendices A-B, **plus a whole-document word census of the pinned 50,630-character text layer**: `transaction cost` 0, `transaction costs` 0, `slippage` 0, `commission` 0, `bid-ask` 0, `spread` 0, standalone `fee`/`fees` 0 (the only `fee` substring sits inside "feedforward" in reference [27]), `funding` 0, `leverage` 0, `borrow` 0, `turnover` 0, `capacity` 0, `market impact` 0 (`price impact` occurs once, as prose about traders splitting large orders), `latency` 0, `order type` 0, `maker` 0, `taker` 0, `participation` 0, `margin` 1 (only inside "marginal prices of the various reserve products"), `fill` 1 (only inside "never filled over time" describing missing-interval masking), `sharpe` 0, `cagr` 0, `drawdown` 0, `win rate` 0, `backtest` 0, `annualized` 0, `pnl` 0, `return` 0, `roi` 0, `repository` 0, `github` 0, `source code` 0, `data availability` 0, `acknowledg` 0, `competing` 0, `conflict` 0, `orcid` 0, `funding` 0, `crypto` 0, `bitcoin` 0, `perpetual` 0, `peer` 0. The word `cost` appears exactly once and only inside a cited paper title ("An opportunity cost approach"). The only forward-looking economic sentence is Section V item 4: "the economic value of orderbook-based imbalance price models in trading and storage bidding remains to be quantified." **There is therefore no transaction-cost, spread, fill, latency or market-impact model anywhere in the paper - every one of those fields is a data gap and must never be read as zero.**
- **Statistical machinery census:** `p-value` 1 (the Diebold-Mariano test definition), `significan` 9, `t-stat` 0, `benjamini` 0, `bonferroni` 0, `holm` 0, `fdr` 0, `multiple test` 0, `bootstrap` 0, `cross-valid` 0, `holdout` 0, `walk-forward` 0 (the design is instead a three-fold **rolling-origin** split, Table I), `seed`/`seeds` 4 (three random seeds per model), `baseline` 0, `naive` 0, `persistence` 0, `climatolog` 0 - i.e. **no trivial benchmark of any kind is reported**.
- **Source-identity deduplication (2026-09-30, hidden-inclusive ripgrep across the entire checkout including `.git`, `.mimo-worktrees`, `.agents`, `.hermes` and `coverage_manifest.csv`):** `2609.37903` 0 files, `From Intraday Orderbook to Imbalance Price` 0, `Orderbook to Imbalance` 0, `Cross-Market Interaction` 0, `10.48550/arXiv.2609.37903` 0, `VWAP-Neighbor` 0, `Average Quantile Coverage` 0, `imbalance price` 0 matches in `*.md`, manifest `37903` 0 hits. Author probes: `Jochen` 0, `Kazempour` 0, `Semmelmann` 0, `Pierre Pinson` 0, `Derek W. Bunn` 1 (the OrderFusion+ record below), `Runyao Yu` 1 (same record), `Matsumoto` 1 (unrelated record). `git log --oneline -20` was used as a convenience glance only.

## Economic mechanism

### Source-reported

The paper's claim is a **cross-market information-transfer conjecture**, not a return premium (Abstract and Section I):

- "We conjecture that positions remaining open after intraday trading, together with demand and supply uncertainties affecting physical participants, influence price formation in the balancing market."
- Section I: the imbalance price "is particularly volatile close to delivery, as it depends on the system operator's short-term imbalance forecast and the marginal prices of the various reserve products activated by the system operator."
- Section I states the **market convention that would make a forecast tradeable**: "Speculation on imbalance exposure is usually profitable, where it is allowed, if there is a single imbalance price and the participant can take an open position in the opposite direction to the balancing market. Thus, if the participant expects the balancing market to be net short, i.e., the system operator buying, it can deliberately go long by buying in the intraday market to be subsequently compensated for that imbalance. Similarly, if the participant expects the balancing market to be net long, it can deliberately go short." The cited enabling markets are **Belgium and the United Kingdom**, not Germany or Austria; the paper does not state whether this speculation is permitted in Germany or Austria (`data gap`).
- Section I motivation: "Accurate modeling of future imbalance prices can support power system management and increase trading revenue"; "providing the participant's optimizer with information about the future imbalance price can improve its market decisions and revenue" (both attributed to cited works [7], [8], [10], [11] - source-reported claims of *other* papers, not results of this one).
- Section IV-A explanation for the winning representation: VWAP "summarizes the volume-weighted consensus price of each interval in a single value that is robust to small orders", LMP uses only two observations, and OHLCV "multiplies the input dimension with extreme prices that are often set by small orders"; neighboring products add information because "traders split large orders both over the historical window and across neighboring products to reduce price impact. The orderbooks of neighboring products therefore carry part of the same position that is being closed for the target product."
- Section IV-B explanation (explicitly labelled as not identified): "In the small Austrian market, imbalance prices are driven more by positions left open after intraday trading, which the orderbook reflects directly, whereas in Germany the large share of wind and solar generation creates physical uncertainties after gate closure that the orderbook cannot fully price in."
- Section IV-C: electricity price distributions shift over time, with the 2022 European energy crisis as the prominent example.

### Research interpretation

Falsifiable mechanism statement: **residual unclosed positions in the continuous intraday market are a latent state variable for the subsequent imbalance price**, and a nonlinear model fed the *volume-weighted* price level of the target delivery product plus its later neighbouring delivery products can extract that state; the incremental value of physical fundamentals over the orderbook should be an increasing function of post-gate-closure physical uncertainty and a decreasing function of orderbook depth, which is why the two countries should differ. Component roles (the source supplies the first two only; the decision layer is research-proposed):

```text
Regime: none required by the source. Research-proposed (optional) regime variant: drop 2022 training rows when the target is an extreme imbalance price - source reports this ordering but explicitly refuses to generalise it (Section IV-C).
Primary signal: 0.1/0.5/0.9 quantile forecast of the imbalance price at t+H, H in {15, 60, 180} minutes, from side-specific 15-minute VWAP of the target delivery product plus its +1/+4/+12 later neighbouring products over an input window M in {15, 60, 180} minutes.
Confirmation (research-proposed, country-gated): Germany only - union with the cumulative fundamental feature block (Table II). The source reports this helps Germany and hurts Austria.
Decision layer (research-proposed - NOT specified by the source): take the intraday position opposite to the predicted balancing-market net direction when the predicted median imbalance price clears a threshold; the source gives only the qualitative convention quoted above, with no threshold, no sizing and no cost hurdle.
Risk / exit (research-proposed): flatten at delivery of the modelled product; no stop, no re-entry rule in the source.
```

The alpha claim under test is narrow and falsifiable: *real-time intraday orderbook information carries decision-relevant content about subsequent imbalance-price formation beyond what a trivial persistence/climatology rule gives, and the residual content differs by market*. **The source itself conducts no trading simulation and explicitly leaves the economic value unquantified (Section V, item 4), so any P&L statement built on this record is a ported, research-proposed hypothesis.**

## Signal

All items are **source-reported** unless explicitly marked research-proposed / research-defined / `data gap`.

- **Formation timestamp:** at modelling origin `t`, for country `c`, horizon `H` and quantile `q`, the model produces `b(q)(c, t+H) = f_theta(F(c, t-M:t), F(c, t:t+H|t))`, where the first argument is the historical input window and the second is *lead* information issued and available at `t`; "only information available at the origin `t` is used" (Section III, Eq. 1). `data gap`: no exchange timestamp convention, timezone or DST handling is stated for order timestamps or for ENTSO-E publication times.
- **Targets:** the imbalance price `y(c, t+H)` for delivery time `t+H`, quantiles `Q = {0.1, 0.5, 0.9}`; horizons `H in {15, 60, 180}` minutes, described as "extreme short term to short term".
- **Orderbook representation:** the orderbook is resampled into 15-minute intervals per delivery product; for each side (buy/sell) the source defines side-specific OHLCV (Eq. 2, open/close = first/last observation in the interval, high/low = extremes over the interval), side-specific VWAP (Eq. 3, executed-trade volume weighted), and LMP = mean of the latest buy and sell closes (Eq. 4). The three representations are evaluated as alternatives and "are not used jointly". **Missing intervals are masked with zeros and "never filled over time or replaced with future information"**; the source does not describe a separate missingness channel that the learner receives (`underspecified`).
- **Feature sets (Eq. 5):** `Self` = orderbook of the product delivered at `t_d = t + H` over `K(t, M)`; `Neighbor` = Self plus the same historical window for the next `n in {1, 4, 12}` delivery products (e.g. `+4` = the four later products); `Country` = Self for country `c` union Self for the neighbouring country `c'` at the same delivery time. `n` is selected on validation data (`data gap`: the selected `n` per country and fold is never printed).
- **Fundamental feature sets (Table II, cumulative):** F1 = solar and wind day-ahead forecasts + solar and wind intraday forecasts + actual solar and wind generation; F2 = F1 + day-ahead load forecast + actual load; F3 = F2 + day-ahead price; F4 = F3 + actual and scheduled cross-border net positions + operational system imbalance. Actual values enter the historical inputs, forecasts enter the lead inputs.
- **Models (Section III-A):** ANN (Swish or ReLU activation, 2/3/4 hidden layers, 32/64/128/256 neurons per layer, learning rate 4e-4 / 1e-3 / 4e-3, 100 epochs, weights achieving the lowest validation loss retained; Table V) and Linear Quantile Regression as the linear counterpart. Stated aim: "to compare information sets and not to find the best modeling architecture." **`data gap`: Tables III and IV never state whether they report the ANN, the LQR, or an aggregation - the model identity of the headline tables is not given in the source.**
- **Training-length ablation (Section IV-C):** four training samples - latest 1 month, latest 6 months, `No 2022` (all observations after 2022), and the original expanding all-available sample, with validation and testing windows held fixed. `underspecified`: the reference point from which "the latest 1 month / 6 months" is measured is not restated.
- **Evaluation (Section III-D):** Average Quantile Loss `AQL` (Eq. 6, training objective), Average Quantile Coverage Error `AQCE` (Eq. 7, empirical coverage of the 80% interval vs nominal 0.80), MAE, RMSE, and paired two-sided Diebold-Mariano tests with `H0: E[d_i] = 0`, rejection at `p < 0.05`, stars at `p < 0.05 / 0.01 / 0.001` (Figures 6-9); in Tables III-IV significance is "conveyed by bold entries" instead. Each model is estimated with **three random seeds**; the three folds cover the full 2024 test year (rolling-origin splits, Table I).
- **Long entry / short entry / exit / holding period / sizing / re-entry (trading layer):** `not stated in source`. The only directional statement is the qualitative convention quoted under Economic mechanism (Section I), which is conditional on a single imbalance price and on the behaviour being *allowed*, and names Belgium and the United Kingdom as its examples.
  - *Research-proposed (not source-reported) operationalization, offered only so the hypothesis is testable:* at origin `t`, go long in the intraday market for delivery `t+H` when the predicted median imbalance price `b(0.5)` exceeds a threshold equal to the expected intraday execution price plus a research-defined cost hurdle, go short on the mirror condition, size a fixed fraction of modelled delivery volume (research-proposed), and flatten at `t+H`. **Threshold, hurdle, sizing, cost ladder and stop rules are entirely research-proposed and have no source support.**

## Required data

- **Instrument / universe:** the German and Austrian imbalance settlement price series and the corresponding continuous intraday delivery products (15-minute products are implied by the 15-minute orderbook resampling; the source does not restate the product granularity it models - `data gap`).
- **Venue:** EPEX SPOT continuous intraday orderbook (commercial); ENTSO-E Transparency Platform for fundamental variables and imbalance prices.
- **Market type:** physical wholesale electricity (day-ahead / intraday / balancing structure, Section I); no crypto exposure of any kind (`crypto`, `bitcoin`, `perpetual` all 0 occurrences).
- **Timeframe:** 15-minute orderbook aggregation; horizons 15 / 60 / 180 minutes; input windows 15 / 60 / 180 minutes; sample January 2022 - January 2025; folds with test quarters entirely inside 2024.
- **Fields:** per side - observed order/trade price and traded volume; fundamentals per Table II (solar and wind day-ahead and intraday forecasts and actuals, day-ahead and actual load, day-ahead price, actual and scheduled cross-border net positions, operational system imbalance); target = imbalance price.
- **Point-in-time:** "only information available at the origin `t` is used"; Appendix A states "Some fundamental variables are subject to irregular publication delays. These variables are therefore not reliably available at every modeling origin, whereas the orderbook is observed in real time." `data gap`: no leakage audit, no revision handling, no explicit availability lag table beyond the Appendix A prose.
- **Timestamp / timezone:** `not stated in source` - timezone, DST and out-of-order handling for both EPEX and ENTSO-E timestamps are not restated.
- **Missing data:** missing orderbook intervals masked with zeros, never forward- or back-filled, never replaced with future information (Section III-B); no imputation rule is given for missing fundamentals (`underspecified`).
- **Unexplained window detail:** the stated data range ends in **January 2025** while the last test fold ends in **December 2024** (Table I); no stated use of the extra month.
- **Acquisition cost / availability:** the orderbook is commercial (Appendix A); **price not stated in source** - unlike the sibling OrderFusion+ paper, this paper gives no figure. ENTSO-E access is not described beyond the platform URL.
- **Funding/fee/spread needs:** `not stated in source` - the paper models no fees, spreads, funding or slippage because it performs no trading simulation.

## Execution assumptions

- **Signal-to-order timing:** `not stated in source`.
- **Order type / fill model / latency / partial fills:** `not stated in source`.
- **Fees / spread / slippage / impact:** **none modeled. The Methods and Experimental sections (II-IV, Appendices A-B) contain no transaction-cost, bid-ask, latency or market-impact treatment whatsoever - see the census in Provenance. Do not read this as "costs are zero"; it is a forecast-accuracy study.**
- **Capacity / liquidity / participation:** `not stated in source`.
- **Leverage / margin / borrow:** `not stated in source`.
- **Position limits / sizing:** `not stated in source`.
- **Market micro-facts available from the source:** the balancing market "settles the resulting aggregate net deviations from the system operator's target at the grid level" and all participants are exposed to individual real-time deviations at the imbalance settlement price (Section I); imbalance price depends on the operator's short-term imbalance forecast and the marginal prices of activated reserve products (Section I). **Whether imbalance-exposure speculation is permitted, and whether settlement uses a single price, in Germany or Austria is `not stated in source`.**
- Whether these forecasts survive realistic execution frictions is **not addressed by the source** and is the central open question for any adoption decision.

## Evidence

### Source-reported

All figures below are source-reported from arXiv:2609.37903v1, are **forecast-accuracy metrics and not P&L**, and have not been independently reproduced. Each is tied to its table/figure/section.

**Table I - rolling-origin data splits.**

| Fold | Training | Validation | Testing |
| --- | --- | --- | --- |
| 1 | Jan. 2022 to Aug. 2023 | Sep. to Dec. 2023 | Jan. to Apr. 2024 |
| 2 | Jan. 2022 to Dec. 2023 | Jan. to Apr. 2024 | May to Aug. 2024 |
| 3 | Jan. 2022 to Apr. 2024 | May to Aug. 2024 | Sep. to Dec. 2024 |

**Table V - ANN hyperparameter search ranges:** neurons per layer {32, 64, 128, 256}; hidden layers {2, 3, 4}; activation {ReLU, Swish}; learning rate {4e-4, 1e-3, 4e-3}.

**Table III - orderbook testing performance, Germany** (columns: AQL, AQCE, MAE, RMSE at h = 15 / 60 / 180 min; `Count` = number of the 12 metric-by-horizon cells belonging to the printed bold "statistically strongest" group).

| Method | AQL-15 | AQCE-15 | MAE-15 | RMSE-15 | AQL-60 | AQCE-60 | MAE-60 | RMSE-60 | AQL-180 | AQCE-180 | MAE-180 | RMSE-180 | Count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OHLCV-Self | 30.03 | 0.026 | 91.69 | 236.96 | 31.12 | 0.022 | 94.19 | 264.61 | 34.24 | 0.019 | 100.94 | 277.89 | 3/12 |
| OHLCV-Neighbor | 28.48 | 0.042 | 85.47 | 207.95 | 32.28 | 0.052 | 96.30 | 261.21 | 33.88 | 0.047 | 97.41 | 266.68 | 2/12 |
| OHLCV-Country | 27.93 | 0.054 | 84.77 | 226.34 | 30.51 | 0.040 | 91.67 | 259.80 | 32.22 | 0.056 | 93.91 | 263.71 | 2/12 |
| LMP-Self | 28.62 | 0.049 | 85.50 | 250.31 | 30.48 | 0.067 | 87.37 | 260.43 | 31.88 | 0.070 | 89.00 | 263.45 | 2/12 |
| LMP-Neighbor | 32.57 | 0.083 | 94.95 | 249.92 | 32.95 | 0.086 | 95.31 | 269.34 | 33.64 | 0.081 | 96.44 | 266.04 | 1/12 |
| LMP-Country | 28.56 | 0.064 | 83.43 | 243.69 | 30.16 | 0.053 | 86.49 | 258.76 | 31.38 | 0.051 | 88.57 | 262.37 | 1/12 |
| VWAP-Self | 27.04 | 0.077 | 82.10 | 218.73 | 29.00 | 0.072 | 85.72 | 251.60 | 30.78 | 0.067 | 88.72 | 256.20 | 1/12 |
| VWAP-Neighbor | 25.88 | 0.056 | 77.51 | 198.01 | 28.43 | 0.054 | 84.97 | 245.92 | 29.68 | 0.060 | 86.43 | 250.32 | 11/12 |
| VWAP-Country | 26.75 | 0.053 | 81.88 | 223.60 | 28.65 | 0.056 | 85.15 | 254.87 | 30.60 | 0.051 | 88.85 | 260.17 | 3/12 |

**Table IV - orderbook testing performance, Austria.**

| Method | AQL-15 | AQCE-15 | MAE-15 | RMSE-15 | AQL-60 | AQCE-60 | MAE-60 | RMSE-60 | AQL-180 | AQCE-180 | MAE-180 | RMSE-180 | Count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OHLCV-Self | 29.40 | 0.045 | 77.60 | 347.22 | 29.97 | 0.035 | 78.71 | 354.65 | 32.01 | 0.039 | 83.13 | 359.38 | 1/12 |
| OHLCV-Neighbor | 27.50 | 0.027 | 71.87 | 333.68 | 28.63 | 0.018 | 74.80 | 349.43 | 30.05 | 0.030 | 79.07 | 356.83 | 5/12 |
| OHLCV-Country | 30.88 | 0.037 | 81.91 | 349.61 | 31.97 | 0.032 | 83.74 | 357.12 | 33.85 | 0.028 | 88.59 | 361.91 | 2/12 |
| LMP-Self | 31.80 | 0.096 | 83.30 | 346.63 | 32.60 | 0.102 | 84.97 | 358.41 | 33.36 | 0.108 | 86.80 | 362.13 | 1/12 |
| LMP-Neighbor | 27.22 | 0.058 | 70.91 | 331.60 | 28.59 | 0.053 | 74.19 | 348.85 | 29.93 | 0.052 | 78.67 | 358.83 | 3/12 |
| LMP-Country | 31.19 | 0.065 | 81.53 | 352.21 | 31.93 | 0.059 | 82.80 | 357.90 | 33.28 | 0.075 | 85.22 | 360.60 | 1/12 |
| VWAP-Self | 28.81 | 0.067 | 74.95 | 349.01 | 29.60 | 0.062 | 77.37 | 354.10 | 31.72 | 0.058 | 81.78 | 358.43 | 1/12 |
| VWAP-Neighbor | 26.85 | 0.057 | 69.12 | 332.64 | 28.15 | 0.059 | 72.98 | 347.55 | 29.43 | 0.053 | 76.93 | 355.05 | 10/12 |
| VWAP-Country | 29.06 | 0.064 | 75.62 | 348.02 | 29.82 | 0.057 | 77.49 | 354.61 | 31.92 | 0.058 | 82.36 | 358.79 | 1/12 |

**Table II - cumulative fundamental feature sets** as listed under Signal (F1 subset of F2 subset of F3 subset of F4).

**Prose-level findings (Sections IV-A to IV-C, Figures 4-11) - quoted as claims, because figure cell values are not recoverable from the text layer:**

1. Tables III-IV: "VWAP-Neighbor has the lowest AQL, MAE, and RMSE at every horizon in both countries" - **verified cell-by-cell against the printed tables and failing in 1 of 18 cells (Austria h=15 RMSE), recorded under contradictions**; "VWAP-Neighbor is consistently the strongest case in Germany and Austria, with counts of 11 and 10" (matches the printed `Count` 11/12 and 10/12).
2. "the loss of every representation increases with the horizon" - verified in both tables for all nine rows.
3. "AQCE is small for all cases, so the representations differ in accuracy rather than calibration" (Section IV-A).
4. "the neighboring country adds modest value in Germany ... but no value in Austria" (Section IV-A).
5. Figure 4/5 AQL change vs Self, averaged over three seeds and three folds: in Austria **every** added neighbouring product reduces loss for VWAP and LMP, growing with the number of products, "up to 14% for LMP with 12 products"; in Germany neighbouring products help **only** VWAP, and adding 4 or 12 products to OHLCV **increases** loss "by up to 40%", so "the amount of context has to be validated per representation."
6. Figures 6/7: "ANN has significantly lower loss in all nine Austrian cases and eight of the nine German cases. German OHLCV with Self is statistically indistinguishable"; the conclusion restates "the nonlinear ANN significantly outperformed LQR in 17 of the 18 cases", i.e. "a nonlinear model is needed". The ANN advantage is largest for the neighbouring-product cases, so "the value of the added context is only realized by a nonlinear model."
7. Figures 8/9 (fundamentals vs orderbook vs combined): "In Germany, combining VWAP with fundamentals consistently reduces testing loss relative to VWAP alone"; "In Austria, adding fundamentals to VWAP consistently increases testing loss"; renewable-generation features "play an important role in Germany, while cross-border nominations provide further value." Exact bar values: `data gap` (not in text layer).
8. Figures 10/11 (training-history ablation): "For overall performance, the strongest German and Austrian cases use all available data. For the extreme observations, excluding 2022 data gives the lowest VWAP loss in both countries." Extremes are defined in the Figure 10 caption as realised imbalance prices **above 1000 EUR/MWh and below -1000 EUR/MWh**; sample sizes `N = 690` positive and `N = 144` negative extreme sample-horizon pairs for Germany, `N = 736` positive and `N = 666` negative for Austria (text for the German pair, Figure 11 caption for the Austrian pair). The source explicitly cautions: "This ablation does not establish that energy crisis data should always be excluded for extreme price modeling."
9. Section IV-A intuition and Section IV-B/IV-C country explanations as quoted under Economic mechanism.

### Independently reproduced

not independently reproduced

### Negative evidence

1. **No trading evidence whatsoever:** the source reports no backtest, no P&L, no portfolio rule, and Section V item 4 states outright that "the economic value of orderbook-based imbalance price models in trading and storage bidding remains to be quantified."
2. **Zero cost modeling:** the Methods and Experimental sections contain no transaction-cost, spread, slippage, fill, latency, leverage, funding or market-impact treatment (census in Provenance) - a data gap, never a zero.
3. **No return or risk metric of any kind:** `sharpe`, `cagr`, `drawdown`, `win rate`, `backtest`, `annualized`, `pnl`, `turnover`, `capacity` all 0 occurrences.
4. **No trivial baseline:** `baseline` 0, `naive` 0, `persistence` 0, `climatolog` 0 - the nine compared cases are all model-based representations of the same orderbook, so nothing establishes that the orderbook beats "the last observed imbalance price" or a seasonal mean. This is the single largest evidentiary hole for the alpha claim.
5. **Model identity of the headline tables unstated:** Tables III-IV never say whether they report ANN or LQR, so the headline numbers cannot be attributed to a specific model.
6. **Predictive only, causal mechanism not identified:** Section V item 3 - "our evidence is predictive and does not identify the causal mechanism of the interaction", and the offered country explanations "are consistent with the loss comparisons but are not identified by them."
7. **Two countries only, commercial data:** Section V item 1 - Germany and Austria "as the orderbook data are commercial", with other imbalance-pricing rules, generation mixes and liquidity left to future work.
8. **Only three orderbook representations:** Section V item 2 - order-level depth features and end-to-end encoders are named as untested alternatives.
9. **Country-dependent sign flip:** combining fundamentals helps Germany and hurts Austria in every one of the four fundamental sets, so the "orderbook is sufficient" conclusion is not portable even between two coupled European markets.
10. **Non-generalisable 2022 result:** the source itself declines to recommend excluding crisis data, and the sample contains exactly one crisis year.
11. **Single test calendar year:** all three folds test 2024 quarters; there is no out-of-window test, no `holdout` (0 occurrences) and no regime breakdown by negative-price hours or Dunkelflaute episodes.
12. **Selection multiplicity without nesting:** representation, input length `M`, neighbour count `n`, ANN architecture and learning rate are all selected per fold on the same validation set, with three seeds and no reported seed variance, no nested cross-validation (`cross-valid` 0) and no seed-sensitivity table.
13. **Significance multiplicity uncontrolled:** Diebold-Mariano stars cover up to 9 cases x 4 metrics x 3 horizons x 2 countries of pairwise comparisons with `benjamini` 0, `bonferroni` 0, `holm` 0, `fdr` 0, `multiple test` 0, `bootstrap` 0.
14. **Source-internal contradiction:** Section IV-A's "lowest ... RMSE at every horizon in both countries" fails for Austria at h=15 (LMP-Neighbor 331.60 vs VWAP-Neighbor 332.64) - see frontmatter `contradictions`.
15. **Bold-group membership unverifiable from the pinned text layer:** PDF bold is lost in extraction, so only the printed `Count` column can be checked, not which cells are bold.
16. **Zero-filled missing intervals:** missing orderbook intervals become zeros with no stated separate missingness channel for the learner, so "no trade" and a numeric zero enter the same feature space - a real data-quality hazard for reproduction.
17. **Point-in-time integrity of fundamentals asserted, not audited:** Appendix A states some fundamental variables are subject to irregular publication delays and "not reliably available at every modeling origin", yet no availability lag table or leakage audit is given.
18. **No reproducibility apparatus:** `repository` 0, `github` 0, `source code` 0, `data availability` 0, `acknowledg` 0, `competing` 0, `conflict` 0, `orcid` 0, `funding` 0 - no code, no data statement, no conflict or funding disclosure.
19. **Preprint only:** no journal reference, no peer-review statement (`peer` 0), arXiv v1 dated 2026-09-29; the paper appears in no venue as of capture.
20. **The tradeability precondition is unverified:** the profitability of imbalance-exposure speculation is stated as holding only "where it is allowed", with Belgium and the United Kingdom as the examples; the source never states that it is permitted in Germany or Austria, never states whether settlement uses a single price, and never states how a participant's deviation is monetised.
21. **Underspecified per-cell configuration:** selected `M`, `n`, VWAP specification, fundamental block and ANN hyperparameters per country and fold are never printed, and "latest 1 month / 6 months" has no stated reference point; exact bar values in Figures 8-11 are not in the text layer.
22. **Unexplained data window:** sample stated through January 2025 while the last test fold ends December 2024, with no stated use of the extra month.
23. **No independent replication or contrary published study on this preprint was found in this run; absence is not evidence of no negative result.**

## Falsification plan

Every threshold below is **research-defined** (a Scout-chosen acceptance/failure cutoff) unless explicitly quoted from the source. Each gate names a fail condition and an action.

**No-retuning rule:** horizons {15, 60, 180}, input-length grid {15, 60, 180}, neighbour set {1, 4, 12}, the three orderbook representations, quantiles {0.1, 0.5, 0.9}, the three rolling-origin folds, the ANN search space (Table V), the three-seed protocol, the fundamentals sets F1-F4, and the extreme threshold +/-1000 EUR/MWh are **frozen**. Any change to these requires a new record; results from a changed configuration may not be used to rescue a failed gate.

- **F1 - printed-value reproduction.** Fail condition: any cell of Tables I-V re-extracted from the pinned PDF differs from this record. **Action:** halt, mark the record unreliable, correct or withdraw it before any further use.
- **F2 - prose-versus-table claim integrity.** Fail condition: a Section IV-A/IV-B/IV-C numerical claim does not hold in the printed tables. **Status: currently FAILING (1 of 18 cells).** Action: treat table cells as truth and the Section IV-A "lowest at every horizon" sentence as partially unreliable; no adoption decision may lean on that sentence.
- **F3 - bold-group / Count gate.** Fail condition: the printed `Count` column cannot be reconciled with the bold formatting of the pinned PDF (requires a rendering-based read, not text extraction). **Status: currently open (data gap).** Action: drop every "statistically strongest group" statement and cite only raw cell values.
- **F4 - model-identity gate.** Fail condition: the source does not state whether Tables III-IV report ANN or LQR. **Status: currently FAILING as printed.** Action: describe the tables as a representation comparison with an unnamed backbone; never attribute them to the ANN.
- **F5 - naive-baseline gate (research-defined, the core alpha test).** Fail condition: with the source's own folds, `VWAP-Neighbor` fails to beat a persistence baseline (last observed imbalance-price median) **or** a 2022-2023 climatological mean by at least 5% relative AQL in both countries at h = 15/60/180 in at least 2 of 3 folds. **Action:** the "orderbook carries information about imbalance-price formation" mechanism is rejected; record stays research-only.
- **F6 - neighbour-product ablation gate.** Fail condition: `VWAP-Neighbor` does not beat `VWAP-Self` in at least 9 of the 12 cells per country. **Action:** the neighbouring-product mechanism is rejected; fall back to `VWAP-Self` only, and record the ablation failure.
- **F7 - fundamentals-increment gate.** Fail condition: in Germany the combined model fails to beat `VWAP` alone for any of F1-F4, **or** in Austria the combined model beats `VWAP` alone for any of F1-F4. **Action:** the country-dependent mechanism statement is rejected as stated and must be restated or withdrawn.
- **F8 - training-history gate.** Fail condition: on refit, the all-data sample is not the best overall, or `No 2022` is not the lowest-loss sample for +/-1000 EUR/MWh extremes in both countries. **Action:** drop the crisis-regime claim entirely rather than adjusting the 2022 boundary.
- **F9 - seed-stability gate (research-defined).** Fail condition: over 10 seeds, the sign of `VWAP-Neighbor` minus `VWAP-Self` AQL flips in more than 30% of seeds in either country. **Action:** treat the representation ranking as noise and withdraw F6/F7 results.
- **F10 - multiplicity gate (research-defined).** Fail condition: fewer than half of the DM pairs the paper marks significant survive Benjamini-Hochberg at q < 0.10 over the full family (9 cases x 4 metrics x 3 horizons x 2 countries). **Action:** withdraw all significance language; retain only effect sizes.
- **F11 - economic-value gate (research-proposed decision layer).** Fail condition: attaching the research-proposed threshold rule from `Signal` and charging a research-defined cost ladder of {0, 0.5, 1, 2, 5} EUR/MWh per position change plus a research-defined signal-to-order delay sweep of {0, 5, 15, 30} minutes produces non-positive expected value in either country. **Action:** record remains `research-only` permanently; no implementation candidate may be advanced on forecast-accuracy evidence alone.
- **F12 - permissibility and settlement gate.** Fail condition: imbalance-exposure speculation is not permitted for the target participant, **or** settlement is not a single imbalance price, in Germany or Austria. **Action:** the strategy layer is not applicable; mark the record not-applicable for trading and keep only the forecasting claim.
- **F13 - out-of-window replication gate (frozen).** Fail condition: refitting the frozen configuration on data extending past January 2025 yields `Count` below 8/12 for `VWAP-Neighbor` in either country. **Action:** treat the 2024 result as a single-year artefact.
- **F14 - data-availability gate.** Fail condition: the EPEX commercial orderbook or the ENTSO-E imbalance/fundamentals series cannot be obtained with point-in-time integrity. **Action:** the record stays `research-only` permanently; no replication claim and no adoption may proceed.

Action on failure for every gate: retain the record as research-only, record the failure in this record's negative evidence, and do not retune the frozen configuration post hoc.

## Crypto portability

**adapted** - the source demonstrates the mechanism only in German and Austrian wholesale electricity and contains zero occurrences of `crypto`, `bitcoin` or `perpetual`, so this is a ported hypothesis and not crypto empirical evidence.

- **What ports:** the abstract cross-market claim - *a continuously observed orderbook aggregates information about a subsequently determined settlement/fixing price, and a nonlinear neighbour-instrument representation of that orderbook improves quantile forecasts of the settlement price*. Candidate crypto analogues for the "later settling price" leg: the funding-rate determination window of perpetual swaps, an exchange index price at a scheduled fix, and the mark price that drives liquidation. The representation recipe (side-specific VWAP over 15-minute bins, self plus neighbouring instruments, 15/60/180-minute horizons, quantile loss) is instrument-agnostic in form.
- **What does not port:** the physical balancing leg has **no crypto counterpart** - there is no system operator, no reserve-product marginal price, no imbalance settlement and no gate closure, so the economic channel that makes the electricity imbalance price explosive near delivery must be re-derived before any port is meaningful; the country-dependent "physical uncertainty vs open positions" split has no direct analogue either; the neighbour-product structure maps only weakly onto crypto expiries and onto BTC-vs-ETH lead-lag, since adjacent electricity delivery products trade in parallel while crypto neighbouring instruments do not share a delivery countdown.
- **Crypto-specific risks:** 24/7 sessions with no delivery countdown or cutoff cascade; venue fragmentation and per-venue book asymmetry; funding as path-dependent carry during any holding window; mark/index vs last-price divergence; maker/taker fee tiers, liquidation mechanics and partial fills; survivorship from delisted contracts. Public L2 data availability is *better* than the commercial EPEX book, but the settlement leg is far less regular.
- No crypto backtest of this mechanism exists in our stack; portability remains unproven. It is not authorization to trade.

## Limitations

- **Source status:** arXiv preprint v1 (2026-09-29), 10 pages / 11 figures / 5 tables, not peer-reviewed, no journal reference, no code or data-availability statement.
- **No trading layer:** entry, exit, sizing, holding period, order type, fill model and all costs are `not stated in source`; the paper is a forecast-comparison study and says so itself (Section V item 4).
- **`data gap`:** timezone/DST conventions, publication-lag tables, leakage audit beyond the Appendix A prose, exact per-fold hyperparameters and neighbour counts, which model Tables III-IV report, bar values in Figures 8-11, and the extra January 2025 month.
- **`underspecified`:** zero-missing-interval masking without a stated missingness channel; the reference point for "the latest 1 month / 6 months" training samples.
- **One recorded source-internal contradiction** (frontmatter `contested: true`), plus bold-group membership that is unrecoverable from the pinned text layer.
- **Universe narrowness:** two coupled markets, one crisis year, one test calendar year, three orderbook representations, no regime breakdown, no capacity or liquidity analysis.
- **Evidence is predictive, not causal** (author-acknowledged, Section V item 3).
- **No naive/persistence/climatology baseline anywhere in the paper**, so the incremental value of the orderbook over trivial rules is untested by the source.
- **Commercial-data dependency:** EPEX SPOT orderbook via the EEX Group Webshop, price not stated in source - independent replication requires paid data; ENTSO-E fundamentals carry irregular publication delays.
- **Tradeability precondition unverified:** permission and settlement rules for imbalance-exposure speculation in DE/AT are `not stated in source`.
- **Not independently reproduced;** every performance figure above is third-party source-reported and is a forecast metric, not a return.
- **Crypto porting is `adapted`, not `direct`.**

## Implementation status

`not-implemented`. No implementation, backtest, prototype, paper trading or validation exists in our research stack. Nothing in Qlib, Paper, Testnet or Live has been touched by this record. The source ships no code and names no repository, so there was nothing to run.

## Adoption boundary

This record is research material only. Its presence in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading.

## Related Wiki records

- Read-only Wiki Brain resolution on 2026-09-30: `quant/strategy-research-record-spec-v2.md` returned **file not found**, so this run failed closed onto `quant/strategy-research-record-spec-v1.md` (canonical, 10,289 bytes, SHA-256 `4561578a2a991aaa8252b31a8b6fd0a46b98c853ef77599521436ee6ff2fcaa7`).
- Five read-only `kb_search` queries were run (`electricity imbalance price forecasting intraday orderbook` 0 pages; `electricity market trading` 2 pages, both unrelated commodities/crypto; `orderbook microstructure forecast` 2 pages; `day-ahead energy storage arbitrage` 0 pages; `cross-market information transfer lead-lag predictability` 0 pages). **No Wiki Brain page exists for electricity imbalance prices, balancing markets, EPEX orderbooks or cross-market orderbook-to-settlement information transfer**, so no such link is asserted. **Zero pages were written.**
- One verified adjacent page was returned and is linked for the shared concept of orderbook aggregation predicting a subsequent price plus a friction barrier, with the mechanism difference stated: [[quant/hawkes-order-flow-imbalance-self-excitation-microstructure-2026-09-12]] - crypto order-flow imbalance and trade-arrival self-excitation with a transaction-cost friction barrier, i.e. same-venue microstructure predictability at seconds-to-minutes horizons, whereas this record is cross-market and settlement-price driven at 15-180 minutes in physical power.
- Repository-adjacent records (same checkout, different source identities and materially distinct mechanisms):
  - `orderfusion-plus-intraday-electricity-buy-sell-price-trajectory-orderbook-dynamic-mask-2026-09-22` - arXiv:2609.23598 (Yu & Bunn), **cited by this paper as reference [22]**. **Five-axis distinction:** (1) *source identity* different (2609.37903, seven authors, vs 2609.23598, two authors); (2) *mechanism* different - cross-market transfer from intraday residual positions to a **balancing-market settlement price** vs within-market side-specific buy-sell **trajectory** dynamics of the delivery product itself; (3) *signal construction* different - static side-specific VWAP of self + +1/+4/+12 later products over an M-minute window feeding a quantile regressor vs a dynamically masked 30-candidate window x neighbourhood bank with cross-attention emitting 180-minute VWAP trajectories; (4) *universe/market stage* different - continuous intraday **plus balancing/imbalance settlement** in Germany **and Austria** vs continuous intraday delivery products in Germany only; (5) *data dependency* different - adds ENTSO-E fundamentals and ENTSO-E imbalance prices to the EPEX book vs EPEX orderbook only. Materially distinct on all five axes.
  - `electricity-spread-thief-forecast-reconciliation-bess-arbitrage-2026-09-22` - arXiv:2609.23223; day-ahead hourly auction, temporal-hierarchy forecast reconciliation of prices/spreads for battery arbitrage. Different market stage, target and mechanism.
  - `eex-peak-baseload-forward-spread-risk-premium-matrix-har-rcv-2026-09-24` - arXiv:2606.05991; forward peak-vs-baseload spread risk premia via realized covariation. Different horizon, target (a traded spread premium rather than a settlement price) and mechanism.
  - `european-cross-border-day-ahead-power-spread-mean-reversion-2026-09-23` - GitHub `CodingxFaisal/power-spread-trader` pinned at `c8205b932c085ab0469a6f86594a6d5a6774c058`; cross-zonal day-ahead price-spread mean reversion with hysteresis. Different market stage and an explicitly mean-reversion trading rule.
  - `bess-day-ahead-ms-ave-probabilistic-profit-ensemble-stopping-rule-2026-09-30` and `day-ahead-battery-profit-evaluation-qbts-overdispersion-gaming-low-discriminatory-power-2026-09-30` - day-ahead probabilistic-forecast profit evaluation for storage; both operate on day-ahead prices and battery dispatch, not on imbalance settlement.
  - `multi-horizon-esn-intraday-return-prediction-2026-09-06` - reservoir-computing intraday return prediction; forecasting-model family only, no balancing-market or cross-market settlement channel.
  - None of these shares this source identity, and none studies orderbook-derived quantile forecasts of a subsequent **imbalance settlement price** with a country-dependent fundamentals increment.

## Sources

1. Yu, R., Cremer, J. L., Pinson, P., Kazempour, J., Semmelmann, L., Matsumoto, T., & Bunn, D. W. (2026). "From Intraday Orderbook to Imbalance Price: Understanding Cross-Market Interaction." arXiv:2609.37903v1 [q-fin.CP], submitted 29 September 2026. Abstract: `https://arxiv.org/abs/2609.37903`; PDF (pinned, 17,211,615 bytes, SHA-256 `99c9497fc3b27d88a7b4bf77c360015186daf0b605a9868b2d322696073ca687`): `https://arxiv.org/pdf/2609.37903`; DOI: `https://doi.org/10.48550/arXiv.2609.37903`. All quantitative claims above trace to Tables I-V, Figures 1-11 (via the paper's own prose), Sections I-VI and Appendices A-B of that preprint; all are labelled source-reported.
2. arXiv API record used only for version/date/publication-status verification: `https://export.arxiv.org/api/query?id_list=2609.37903` (3,616 bytes, SHA-256 `6a0a55aa4add7e92f02e60357df663c1b3d931b65b215c32611226587c7f525f`).
3. Data vendors referenced by the primary paper (used by it, not directly by us): EPEX SPOT public market data products via the EEX Group Webshop (commercial, price not stated in source) and the ENTSO-E Transparency Platform, `https://transparency.entsoe.eu/`.
