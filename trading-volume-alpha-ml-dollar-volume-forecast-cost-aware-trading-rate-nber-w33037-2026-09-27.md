---
schema: strategy-research-record-v1
title: "Trading Volume Alpha: ML dollar-volume forecasting as a cost-aware trading-rate controller for US equity portfolios (NBER WP 33037)"
created: 2026-09-27
updated: 2026-09-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - us-equities
  - trading-volume
  - volume-forecasting
  - transaction-costs
  - price-impact
  - portfolio-implementation
  - decision-focused-learning
  - machine-learning
  - neural-network
  - nber
  - working-paper
status: research-only
confidence: medium
source_as_of: 2026-09-27
sources:
  - "https://www.nber.org/papers/w33037"
  - "https://doi.org/10.3386/w33037"
  - "https://www.nber.org/system/files/working_papers/w33037/w33037.pdf"
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4978835"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions:
  - "Source-internal: §6.2 prose reports the $1b AUM headline as '6.47% to 8.98%', but Table 3 Panel A gives rnn.econall at $1b = 8.95% (nn.econall = 8.87%, oracle = 9.89%). This record uses the Table 3 value."
  - "Source-internal: §1 claims that for a $1b fund the improvement 'can be as much as double in terms of expected returns or Sharpe ratio'; Table 3 shows mean return 6.47% -> 8.95% (+38%) and Sharpe 2.21 -> 4.53 (>2x), so only the Sharpe half of the claim is supported by the printed table."
  - "Source-internal / metadata: the SSRN landing for abstract_id=4978835 shows 'Last revised: 9 Apr 2026' and a suggested-citation field that lists Moskowitz twice, yet the PDF SSRN serves (nber_w33037.pdf) is byte-identical to the NBER October 2024 file (same 1,175,371 bytes and SHA-256), and the NBER landing carries no revision date. Version metadata, not the document, is inconsistent."
---

# Trading Volume Alpha: ML dollar-volume forecasting as a cost-aware trading-rate controller for US equity portfolios (NBER WP 33037)

## Provenance

- **Primary source (pinned, checksummed, text-extracted and read end to end):** Goyenko, Ruslan; Kelly, Bryan T.; Moskowitz, Tobias J.; Su, Yinan; Zhang, Chao, *"Trading Volume Alpha"*, **NBER Working Paper No. 33037**, October 2024, DOI **10.3386/w33037**. JEL C45, C53, C55, G00, G11, G12, G17.
- **Complete author list exactly as printed on the PDF title block (p.2) and in the NBER `citation_author` meta tags, in the same order:** Ruslan Goyenko (McGill University, Faculty of Management); Bryan T. Kelly (Yale School of Management, and NBER); Tobias J. Moskowitz (Yale School of Management, and NBER); Yinan Su (Johns Hopkins University, Carey Business School); Chao Zhang (Hong Kong University of Science and Technology (HKUST); correspondence address printed as `chao.zhang94@outlook.com`). No other authors. The SSRN landing adds "AQR Capital Management, LLC" to Kelly and "Yale University, Yale SOM; AQR Capital" to Moskowitz, affiliations that do **not** appear in the pinned PDF's address block → recorded as landing-page metadata, `data gap` for the pinned version.
- **Pinned PDF:** `https://www.nber.org/system/files/working_papers/w33037/w33037.pdf`, **1,175,371 bytes**, **53 pages**, **SHA-256 `0d34e7545c767a6d08899aac16f2b31f5fab783f3b603f00d8463f6cf0c95325`**, downloaded **2026-09-27**, text layer extracted with pypdf to 118,628 characters and read across all 53 pages.
- **Mirror-identity check (2026-09-27):** the SSRN delivery URL `https://papers.ssrn.com/sol3/Delivery.cfm/nber_w33037.pdf?abstractid=4978835&mirid=1` was fetched inside a browser session and hashed in-page: **1,175,371 bytes, SHA-256 `0d34e7545c767a6d08899aac16f2b31f5fab783f3b603f00d8463f6cf0c95325`** — byte-identical to the NBER copy, so one pinned version covers both mirrors.
- **Version / date:** PDF cover "NBER WORKING PAPER SERIES … October 2024"; PDF metadata `/CreationDate D:20240731221817Z`, `/ModDate D:20241002082816-04'00'`, producer `pdfTeX-1.4.25 / LaTeX with hyperref`, empty `/Title` and `/Author`. NBER landing (fetched 2026-09-27, HTTP 200): `citation_publication_date = 2024/10/07`, `citation_technical_report_number = w33037`, `Issue Date` block with `<time datetime="2024-10-04">October 2024</time>` and a second timestamp `2024-10-15`, **no revision-date field**. SSRN landing (read 2026-09-27 after clearing the Cloudflare challenge): `53 Pages`, `Posted: 8 Oct 2024`, `Last revised: 9 Apr 2026`, `Date Written: October 2024`, "There are 2 versions of this paper" (NBER + SSRN), 83 downloads / 2,142 abstract views / 1 citation / 39 references, license "The copyright holder has granted SSRN a license. All rights reserved. No reuse allowed without permission."
- **Publication / peer-review status (source's own words, PDF p.1):** "NBER working papers are circulated for discussion and comment purposes. They have not been peer-reviewed or been subject to the review by the NBER Board of Directors that accompanies official NBER publications." → **working paper, not peer reviewed**. No journal, venue, DOI other than the NBER DOI, acknowledgement of peer review, or conference acceptance is printed in the pinned PDF.
- **Disclosures as printed (p.1):** acknowledgments to the Columbia & RFS AI in Finance Conference, discussant Dmitriy Muravyev, and seminar participants at Cornell, Syracuse, CityU Hong Kong and George Mason, plus Martin Lettau, Lu Lu, Andrew Patton and Annette Vissing-Jorgensen; research assistance thanked (Zhongji Wei, Andy Yang). "AQR Capital Management is a global investment management firm, which may or may not apply similar investment techniques or methods of analysis as described herein. Moskowitz is a member of the NBER, has an academic consulting relationship with AQR Capital, and sits on the board of Commonfund. The views expressed here are those of the authors and not necessarily those of AQR or the National Bureau of Economic Research."
- **Code / data / replication:** a full-text scan of the pinned PDF for `github`, `replication`, `data availability`, `available from`, `upon request`, `open source`, `we release` returned **one** hit, and it is a reference title (*"Is there a replication crisis in finance?"*) → **no code repository, no replication package and no data-availability statement anywhere in the pinned PDF**; every availability field is `not stated in source`.
- **Sections read line-by-line for this record:** title block, Abstract (p.2); §1 Introduction (pp.3–8); §2.1 Motivation, §2.2 Data, §2.3 Prediction objects, §2.4 Predictors (pp.8–13); §3.1 Prediction methods, §3.2 Prediction results (pp.13–17); §4.1 Tracking-error optimization, §4.2 Normalized trading rate, §4.3 Optimal policy (pp.17–21); §5.1 Statistical vs economic tasks, §5.2 Transfer learning, §5.3 Results (pp.21–31); §6.1 Experiment design, §6.2 Simulated quantitative strategy, §6.3 Factor-zoo portfolios (pp.30–37); §7 Conclusion (pp.37–39); References (pp.39–42); Internet Appendix A.1 (pp.42–45), B.1–B.4 (pp.44–50), C.1–C.2 (pp.50–53). Tables **1**, **2**, **3**, **A.1**, **C.2** re-extracted cell by cell from the text layer; Figures **1–7** and **A.1, B.2, C.3, C.4** are read through their printed captions and the surrounding prose only (numeric series inside figures are `data gap`).
- **Dedup (pre-write, whole repository):** `rg -uu` over **every file in the checkout** including hidden trees `.mimo-worktrees/`, `.agents/`, `.hermes/`, plus `coverage_manifest.csv`, for `w33037`, `10.3386/w33037`, `4978835`, `ssrn.4978835`, `abstract_id=4978835`, `Trading Volume Alpha` (case-insensitive), `Goyenko` → **zero hits for every exact-identity pattern before this file was written.** The only non-zero result was `Yinan Su` / `Trading Volume Alpha` appearing **as cited literature inside** `limt-hierarchical-multitask-liquidity-aware-ashare-cross-sectional-apo-2026-09-23.md` (a different source identity, §I reference [25]) — a citation, not a record built on this paper. Broader mechanism-pattern scans (`net-of-cost alpha`, `volume prediction`, `Frazzini, Israel`, `economic loss function`) returned only unrelated records. `git log --oneline -20` was inspected as a convenience glance only and does not by itself satisfy dedup.
- **Four-axis distinction from the nearest repository neighbours (all different source identities):**
  - `reviving-anomalies-expected-net-return-double-sort-1n-implementable-2026-09-23` (Beckmeyer/Berg/Wiedemann/Wortmann, SSRN 6468806) — also uses the 153 JKP characteristics and a scale-dependent price impact, but its **signal is predicted net return** used to *select* anomalies; here the **signal is predicted dollar volume** used to *pace trading* toward a target that is exogenously given, and no return forecast exists anywhere in the model. Axis: mechanism + signal construction.
  - `limt-hierarchical-multitask-liquidity-aware-ashare-cross-sectional-apo-2026-09-23` — liquidity/volume is auxiliary supervision for **return/vol forecasting** on CSI300/CSI500 with a participation cap; here volume is the **only** prediction target and the output is a trading rate, on US equities. Axis: signal construction + universe + data dependency.
  - `equity-order-flow-kyle-lambda-cross-sectional-liquidity-premium-2026-09-03` — Kyle's lambda used as a **cross-sectional return predictor**; here the Kyle-style impact term is a **cost** inside a tracking-error objective, with no return prediction. Axis: mechanism.
  - `forecast-to-fill-gold-futures-friction-adjusted-kelly-alpha-2026-09-02` — friction-adjusted sizing for a real alpha in gold futures; here there is no alpha to size, only implementation of externally supplied targets. Axis: mechanism + universe.

## Economic mechanism

### Source-reported

The authors' stated rationale (§1, §2.1, §4, §7):

- Implementation cost is a first-class determinant of portfolio performance, yet "forecasting trading costs has received no attention". Cost prediction at stock level is hard because the dominant component, price impact, depends on trade size **and** trader identity (Frazzini, Israel & Moskowitz, 2018).
- The paper therefore predicts only the one cost input that is **generic to every trader and exogenous to any single trader's trade size**: total dollar trading volume. Participation rate `= $Traded / $Volume` (§2.1), and price impact is an increasing, modelled-linear function of participation (Kyle, 1985; empirically supported by Frazzini, Israel & Moskowitz, 2018). Holding trade size fixed, lower volume ⇒ higher impact.
- Because impact is linear in participation but **non-linear in volume** (`λ̃ = 0.2/Ṽ`, so impact → ∞ as V → 0 and → 0 as V → ∞), forecast errors are asymmetric: overestimating volume (trading hard into thin liquidity) is far costlier than underestimating it (forgone tracking). The optimizer is therefore pushed toward **conservative** trading — a stated, novel implication for limits to arbitrage (§1, footnote 7).
- The economic value of a better volume forecast is measured inside a mean–variance objective that penalizes (i) quadratic **tracking error** to a pre-cost optimal target and (ii) quadratic **trading cost**; the two are endogenously negatively related. Translating volume predictability into net-of-cost performance is what the paper names **"trading volume alpha"** (Abstract, §4).
- The authors explicitly disclaim any claim to the best cost or volume model: "our aim is not to provide the 'best' or most reliable trading cost model or forecast … our simple objective is to provide a forecast of trading costs that any trader could use" (§1).

### Research interpretation

Falsifiable hypothesis as we normalize it: **an out-of-sample, ML-based forecast of next-day dollar volume, fed into a participation-based cost model, produces measurable net-of-cost improvement over a naive lagged-volume baseline when implementing an externally specified target portfolio — i.e. there is an *implementation-layer* alpha that does not require any return prediction.**

Component roles (per README hybrid structure):

```text
Cost model (regime):     lambda_tilde = 0.2 / V_tilde   (linear Kyle-style impact,
                                                          Frazzini/Israel/Moskowitz 2018)
Primary signal:          ML forecast of log dollar volume v_tilde_{i,t} (or, equivalently,
                          a directly learned trading rate z_{i,t}) from 175 predictors
Controller:              sigmoid policy s(v; mu) = 1/(1+exp(-v + log0.2 - log mu))
                          -> trade partially toward the target (Garleanu-Pedersen 2013 form)
Target (exogenous):      (a) a simulated 1%-signal long-short strategy, or
                          (b) monthly-rebalanced equal-weighted JKP factor sorts
Risk / exit:             none — no stops, no exits; the tracking-error penalty (mu)
                          plays the risk-control role; positions are re-targeted daily
```

Important boundary: **there is no return forecast anywhere in this system.** Returns enter only through the exogenous target `x*` and through realized P&L accounting. If the target itself has no alpha, the mechanism can at best *save* cost, not create return — which is exactly why the paper benchmarks against a naive volume baseline rather than against buy-and-hold.

## Signal

- **Formation timestamp:** predictors `X_{i,t}` are "observed by day t−1"; the prediction target `Ṽ_{i,t}` is "observed until the end of day t" (§2.2). The position `x_{i,t}` is chosen "at the start of day t" (§4.1). So the forecast horizon is *same-day (day-t) dollar volume, conditioned on information through t−1*, and the trade is placed at the start of day t. **Timezone, session convention, and the trade price (open vs. first-tick vs. VWAP) are `not stated in source`.**
- **Prediction target:** `ṽ = log(dollar volume)`; primary object is the shock `η̃_{i,t} = ṽ_{i,t} − (1/5)(ṽ_{i,t−1}+…+ṽ_{i,t−5})` (§2.3, Figure 1 caption), i.e. log volume minus its 5-day moving average. Predicting `η̃` is stated to be equivalent to predicting `ṽ` via a residual connection.
- **Lookback / predictors (175 total, added cumulatively, §2.4):**
  1. `tech` (8): lagged moving averages of returns and of log dollar volume over 1, 5, 22 and 252 days.
  2. `fund-1` (6): market equity, standardized earnings surprise, book leverage, book-to-market equity, Dimson beta, firm age.
  3. `fund-2` (147): the remaining JKP characteristics, merged/transformed identically; monthly values forward-filled (source asserts they remain "always ex-ante available"), cross-sectionally rank-standardized each day to a uniform on [−1, +1] (footnote 11).
  4. `calendar` (4 hard-coded binaries): early-closing days (Jul 3, Black Friday, Christmas Eve, New Year's Eve), triple-witching days, double-witching days, Russell reconstitution (fourth Friday of June).
  5. `earnings` (10 one-hot bins): days-to-next-scheduled-earnings binned ≤−4, −3, −2, −1, 0, 1, 2, 3, 4, ≥5, from the **Capital IQ Key Developments** dataset.
- **Models (all fixed, not tuned — §3.1, Internet Appendix A.1):** baseline `ma5` (`η̂ = 0`); `ols`; `nn` = 3 fully-connected ReLU layers of 32/16/8 with one linear output; `rnn` = same network with the bottom layer upgraded to an LSTM (32 hidden/cell states), "many-to-one" pipeline over a sequence of **10** lagged inputs (`X_{i,t−9}…X_{i,t}`, zero-padded at series starts; sequence 50 gave "minimum improvements"). Adam optimizer with default learning rate and parameters, batch size 1024, **50 epochs**, **no early stopping, no dropout, no cross-validation/hyperparameter tuning**, implemented in PyTorch. Each reported R² is the average of **five independent runs with different random seeds** (Table 1 note; §3.1).
- **Two learning approaches (§5.1):**
  - *Statistical*: fit volume by least squares, then plug `v̂` into the policy `s(v̂; µ)`.
  - *Economic*: parameterize `z` as the network and minimize `loss_econ(ṽ, z; µ) = λ̃ z² + µ(1−z)²` directly on the **same training sample** (transfer learning: pre-train statistically, then fine-tune on the economic loss — §5.2, Figure 4). Proposition 1 states least-squares prediction is **not** the economic optimum (the economic loss is outside the Bregman class, Appendix B.3).
- **Policy / entry rule:** `z = s(v̂; µ) = 1 / (1 + exp(−v̂ + log 0.2 − log µ))`, then `x = x⁰ + z·(x* − x⁰)`, with the starting position carried recursively `x⁰_{i,t} = x_{i,t−1} · R^raw_{i,t}` where `R^raw = 1 + r_{f,t−1} + r_{i,t}`; initialization `x⁰ = 0` on a stock's first sample day (§6.1, footnote 27).
- **µ (aggressiveness) handling — source-reported but tuned:** µ is *not* calibrated from risk coefficients; it is a hyperparameter. Table 2 header gives µ = 1.2e-9 / 6.3e-8 / 4.7e-7 / 9.4e-6 corresponding to AUM $10b / $1b / $100m / $10m with average trading rate `avg z` = 0.13 / 0.57 / 0.78 / 0.95 (these AUM rows are backed out from µ-tuning **under method ma5**, footnote 28). Table 3 reports each method at **the µ that maximizes the in-sample mean return (or Sharpe)** over a grid, applied out of sample (§6.2, footnote 28). For the 153 factor targets, a **single fixed µ** is used, chosen to optimize the average gain across all factors (§6.3) — its numeric value is `not stated in source`.
- **Holding period / cadence:** daily re-targeting of every stock; no maximum holding period, no exit trigger, no stop, no re-entry rule beyond the daily recursion. The simulated target's *forecast* horizon is five days, but positions are re-evaluated daily — the interaction between the 5-day signal and daily re-targeting is `underspecified`.
- **Position sizing:** dollar positions scale linearly with AUM; the simulated and factor targets are equal-weighted long–short with each leg summing to 50% of AUM (so 100% gross, **no leverage** in the factor experiments: $5b long + $5b short = $10b AUM, §6.3).
- **Turnover definition (source, Eq. 15):** annualized one-way turnover `= (1/(2T)) Σ_{i,t} |w_{i,t} − w⁰_{i,t}| × 252`, stated to be scale-invariant. Realized turnover per configuration is only **plotted** (Figures 5–7), never printed in a table → `data gap`.
- **Fully specified / underspecified:** the forecast, the policy, the cost functional form, the recursion and the turnover formula are fully specified. The trade price, timezone, universe-construction rules, suspended/halted-name handling, minimum lot, the µ grid, and the numeric µ used in §6.3 are `underspecified`.

## Required data

- **Instrument / universe:** daily stock-level **US equity** cross-section. The panel "covers around 4,700 stocks, with an average of 3,500 stocks per day" (§2.2); size groups are defined by **NYSE market-cap percentile breakpoints** (mega >80th, large 50–80, small 20–50, micro 1–20, nano <1st — Internet Appendix C.1, footnote 30), and the calendar features include Russell 1000/2000/3000 reconstitution. The exchange list, listing screen, and point-in-time membership rules are **`not stated in source`** (no CRSP/vendor name appears anywhere in the pinned PDF).
- **Sample period:** **2018 to 2022, or 1,258 days**, split into a **3-year training sample and a 2-year testing sample** (§2.2); models are trained once on the training sample and evaluated out of sample, with **no cross-validation and no rolling-window re-estimation** (explicitly stated, §2.2). The exact calendar dates of the train/test boundary are **`not stated in source`** (the 3+2 split over 2018–2022 implies 2018–2020 / 2021–2022, but the paper never prints them → recorded as `underspecified`, not asserted).
- **Observation count:** ~4,400,000 stock-day observations; Table C.2 gives training obs 2,522,619 and testing obs 1,893,067 (joint), with per-size-group splits printed.
- **Fields required:** end-of-day **dollar trading volume** (log-transformed) for every stock-day; daily returns and a risk-free rate `r_f` (source of `r_f` `not stated in source`); 175 predictors as enumerated above (technical moving averages, JKP firm characteristics, hard-coded calendar dummies, Capital IQ earnings-schedule dummies).
- **Point-in-time / availability:** `X_{i,t}` observed by day t−1; monthly characteristics forward-filled but asserted "always ex-ante available"; the earnings feature uses the "next **known scheduled** release" (forward-looking, point-in-time by construction). Whether Capital IQ's *scheduled* release dates were themselves known without hindsight is not analysed → `data gap`.
- **Missing-data assumptions:** `not stated in source` for prices/volume; the only stated treatment is zero-filling missing lag vectors at the start of a stock's observed period (Internet Appendix A.1). Staleness, halts, suspensions, delistings and survivorship handling are all `data gap` (no mention of delisting returns, share-code screens, or survivorship adjustment appears in the pinned PDF).
- **Funding / fee / spread needs:** the cost model needs only **dollar volume**; commissions, fee schedules, bid-ask spread, borrow rates, financing and funding are neither observed nor modelled (see Execution assumptions).

## Execution assumptions

- **Cost model actually used (source-reported, §4.1 equations 3–4):**
  - `TradingCost_{i,t} = ½ · λ̃_{i,t} · (x_{i,t} − x⁰_{i,t})²` with **`λ̃ = 0.2 / Ṽ = 0.2·exp(−ṽ)`**, "following Frazzini, Israel, and Moskowitz (2018)".
  - Equivalent micro-foundation stated in the same passage: **`PriceImpact = 0.1 · (x − x⁰)/Ṽ`** (linear in participation rate, Kyle 1985) and `TradingCost = PriceImpact · (x − x⁰)`; the worked example is "buying (or selling) 10% of the daily volume would move the price by 1% (or −1%)".
  - Footnote 17 records an alternative quadratic specification `λ̃ = 0.2/√Ṽ` (also from Frazzini/Israel/Moskowitz) under which "all the analyses carry through but `v` will be twice as large"; the paper keeps the linear-in-participation form.
  - Footnote 17 also states cross-impact from related stocks and other determinants of `λ̃` are assumed away.
- **What is NOT modelled — every item below is `data gap`, never zero:**
  - **Commissions / exchange + regulatory fees:** zero occurrences of `commission` or `fee(s)` in a word-boundary scan of the pinned PDF → not modelled.
  - **Bid-ask spread:** explicitly deferred — §6.2: "For more realistic considerations, future research could consider per-unit trading costs such as bid-ask spread in addition to price impacts, which tend to show up as dollar trade sizes shrink." → **the source itself states the current cost model is incomplete.**
  - **Slippage beyond the impact term, market-impact model misspecification, participation/ADV caps, capacity:** no participation cap, no ADV constraint and no capacity analysis anywhere → `data gap`.
  - **Borrow / short availability / stock-loan fee:** all factor and simulated targets are long–short; no borrow cost or locate constraint is modelled → `data gap`.
  - **Leverage / margin:** gross exposure equals AUM in the experiments; no margin, financing or leverage cost → `data gap`.
  - **Funding, latency, order type (market vs limit), fill model, partial fills / failed trades:** zero occurrences of `latency`, `fill model`, `order type`; `fill` appears only as "forward fill" and "fill in with zero vectors" → `data gap`.
- **Signal-to-order timing:** position chosen at start of day t from information through t−1; **execution price convention is `not stated in source`**, so next-bar-vs-same-bar behaviour cannot be determined from the paper.
- **Gross vs. net:** reported returns and Sharpe ratios in Table 3 and the §6.3 gains are stated as **after price-impact trading cost** ("mean return after tcost", Eq. 14) — i.e. **net of modelled impact only**. They are *not* net of commissions, spread, borrow or any per-unit fee. Any use of these numbers as "net of costs" must be read with that qualifier.
- **Distinguish source vs. Scout:** everything above is the source's own specification. No Scout-added execution assumption is used anywhere in this record; where an operational choice was needed for falsification (cost ladders, participation caps, thresholds) it is labelled **research-proposed / research-defined** in the Falsification plan.

## Evidence

### Source-reported

All figures below are third-party results reported by Goyenko, Kelly, Moskowitz, Su & Zhang, NBER WP 33037 (pinned PDF read 2026-09-27), and have **not** been independently reproduced. Each block names its table/section.

**A. Statistical volume predictability — Table 1, "Prediction accuracy" (out-of-sample, training 3y → testing 2y, average of five seeds):**

| method | tech (8) | +fund-1 (14) | +fund-2 (161) | +calendar (165) | +earnings (175) |
|---|---|---|---|---|---|
| `ma5` (Panel B, R² on `ṽ`) | 93.68 | — | — | — | — |
| `ols` R² on `η̃` (Panel A) | 12.09 | 12.26 | 12.27 | 14.85 | **15.99** |
| `nn` R² on `η̃` | 14.31 | 14.90 | 14.42 | 17.13 | **18.45** |
| `rnn` R² on `η̃` | 15.80 | 16.25 | 15.47 | 18.12 | **19.86** |
| `ols` R² on `ṽ` (Panel B) | 94.44 | 94.45 | 94.45 | 94.62 | **94.69** |
| `nn` R² on `ṽ` | 94.58 | 94.62 | 94.59 | 94.76 | **94.85** |
| `rnn` R² on `ṽ` | 94.68 | 94.69 | 94.64 | 94.86 | **94.93** |

Panel C parameter counts (tech → all): `ols` 9 → 176; `nn` 961 → 6,305; `rnn` 6,049 → 27,425. §2.3 additionally reports baseline persistence R² on `ṽ`: one-day lag 92.53%, **ma5 93.68%**, ma22 92.60%, ma252 86.12%. §3.2: "The most sophisticated model using all predictors can predict nearly 20% of future variation in daily trading volume changes."

**B. Economic vs. statistical loss — Table 2 (mean economic loss, MEL, ×10⁻⁸; A′ = % reduction in MEL relative to `ma5` = 0% and `oracle` = 100%):**

Columns are AUM $10b / $1b / $100m / $10m, with µ = 1.2e-9 / 6.3e-8 / 4.7e-7 / 9.4e-6 and `avg z` = 0.13 / 0.57 / 0.78 / 0.95.

| method | $10b | $1b | $100m | $10m |
|---|---|---|---|---|
| `ma5` MEL | 0.1046 | 3.163 | 15.41 | 93.0 |
| `ma5` A′ | 0.0 | 0.0 | 0.0 | 0.0 |
| `rnnall` MEL / A′ | 0.1040 / 34.8 | 3.012 / 29.5 | 14.78 / 11.7 | 109.8 / **−32.1** |
| `nn.econall` MEL / A′ | 0.1039 / 39.6 | 2.810 / 69.2 | 11.56 / 70.9 | 61.9 / 59.6 |
| `rnn.econall` MEL / A′ | 0.1038 / **43.7** | 2.812 / **68.8** | 11.60 / **70.3** | 66.4 / **51.0** |
| `oracle` MEL / A′ | 0.1029 / 100 | 2.653 / 100 | 9.99 / 100 | 40.8 / 100 |

Panel B′ (R² relative to `ma5`) for the economically fine-tuned models: `nn.econall` 10.0 / −26.8 / −34.9 / **−352.5**; `rnn.econall` 13.9 / −0.6 / −9.0 / **−79.5**. §5.3 summary: fine-tuned networks "reach an OOS economic performance that is about 43%∼70% of the unattainable oracle benchmark at various AUM scales", while "the statistical accuracy retreats after fine-tuning, often to levels even worse than the ma5 baseline resulting in negative R²".

**C. Trading experiments on the simulated quantitative strategy — Table 3, "Investment performance in trading experiments" (out-of-sample, at the in-sample-tuned µ; mean return in % annualized, Panel A; annualized Sharpe, Panel B):**

| method | ret $10b | $1b | $100m | $10m | Sharpe $10b | $1b | $100m | $10m |
|---|---|---|---|---|---|---|---|---|
| `ma5` | 3.88 | 6.47 | 11.19 | 13.20 | 2.00 | 2.21 | 5.47 | 6.55 |
| `olstech` | 3.82 | 7.60 | 11.28 | 13.14 | 2.16 | 3.32 | 5.59 | 6.59 |
| `nntech` | 3.76 | 7.30 | 11.32 | 13.13 | 2.14 | 2.79 | 5.63 | 6.59 |
| `rnntech` | 3.74 | 7.84 | 11.33 | 13.13 | 2.18 | 3.58 | 5.64 | 6.59 |
| `nn.econtech` | 4.60 | 7.20 | 11.29 | 13.22 | 2.13 | 2.57 | 5.59 | 6.63 |
| `rnn.econtech` | 4.67 | 8.69 | 11.59 | 13.30 | 2.50 | 4.32 | 5.73 | 6.66 |
| `olsall` | 3.82 | 7.60 | 11.28 | 13.14 | 2.17 | 3.35 | 5.60 | 6.59 |
| `nnall` | 3.86 | 7.44 | 11.28 | 13.13 | 2.19 | 3.09 | 5.60 | 6.58 |
| `rnnall` | 3.79 | 7.55 | 11.25 | 13.09 | 2.18 | 3.26 | 5.59 | 6.56 |
| `nn.econall` | 4.64 | 8.87 | 11.61 | 13.29 | 2.18 | 4.24 | 5.74 | 6.66 |
| **`rnn.econall`** | **4.68** | **8.95** | **11.77** | **13.30** | **2.50** | **4.53** | **5.85** | **6.68** |
| `oracle` | 6.47 | 9.89 | 12.54 | 13.56 | 3.05 | 4.97 | 6.28 | 6.80 |

§6.2 prose: at $10b, "the average annual return increases from 3.88% … to 4.68%"; at $1b "from 6.47% to 8.98%" (**contradicts Table 3's 8.95 — see frontmatter**) and "more than doubling the Sharpe ratio from 2.21 to 4.53". Design facts behind these numbers (§6.1–6.2): the target is a **simulated** equal-weighted long–short strategy whose signal "with 1% chance, perfectly forecasts whether a stock goes up or down over the next five days", independent across stock-days, legs summing to 50% of AUM each, with a stated **before-cost out-of-sample Sharpe ratio of around 7**; AUM up to $10 billion; turnover is plotted (Figures 5–6, x-axis ≈ 0.5–1.5 annualized) but not printed.

**D. Factor-zoo implementation — §6.3 and Figure 7 (153 JKP characteristics, AUM fixed at $10b = $5b per leg, monthly start-of-month formation, 50th-quantile split into equal-weighted long–short, single fixed µ across all factors):**

- Average gain in **mean after-cost return** from `rnn.econall` vs `ma5` volume forecasting: **0.44% per year across factors**, "Almost all of the 153 factors have positive gains"; at $10b this is stated as "**an additional $44m per year** in implementation cost-saving".
- Gain by turnover: high-turnover factors (up to ~600%/yr, e.g. short-term reversal) gain "**around 0.5% to 1.0%**"; low-turnover factors gain "**0.2% to 0.6% per year**".
- §1 restates the range as "20 bps to 100 bps above using a moving average of lagged volume".
- Appendix C.2 / Figure C.4: Sharpe-ratio gains for high-turnover factors reach "**around 0.3 to 0.4 per year**"; Figure C.3 shows the gain is "independently distributed around a positive center" versus the baseline's own realized return.
- No table of factor-level numbers, no dispersion, no significance is printed for these gains → the figure-level claims are `source-reported (figure)`.

**E. Size heterogeneity and mixture-of-experts — Internet Appendix Table C.2 (OOS R² in %, pooled models from Table 1):**

| size group (joint / nano / micro / small / large / mega) | `olsall` | `nnall` | `rnnall` |
|---|---|---|---|
| pooled training | 15.99 / 13.32 / 12.60 / 20.90 / 25.49 / 26.16 | 18.45 / 15.80 / 14.86 / 23.71 / 27.76 / 29.12 | **19.86 / 16.63 / 16.14 / 26.00 / 30.50 / 32.02** |
| per-group "expert" (mixture) | 16.34 / 13.68 / 12.73 / 21.43 / 25.93 / 27.47 | 17.78 / 15.29 / 14.43 / 22.69 / 26.57 / 27.71 | 18.26 / 15.24 / 14.71 / 24.76 / 29.02 / 30.99 |

Training/testing obs by group are printed in the same table (joint 2,522,619 / 1,893,067).

**F. Compute cost — Internet Appendix Table A.1 (single seed):** `nnall` 0.48 h training, 10.87 GB CPU / 1.22 GB GPU; `rnnall` 0.63 h, 144.98 GB CPU / 1.48 GB GPU; hardware "Nvidia A100 GPU with 40 GB …, AMD EPYC 7713 … 128 cores, 1.0TB of RAM, Ubuntu 20.04.4 LTS".

### Independently reproduced

not independently reproduced

### Negative evidence

1. **The cost model is impact-only, by the source's own admission.** Commissions and fees have zero occurrences in the pinned PDF; bid-ask spread is explicitly deferred to "future research" (§6.2); slippage, participation caps, capacity, borrow, financing, margin, funding, latency, order type and fill/failure handling are all absent → `data gap`, never zero. Every "after-cost" number above is therefore net of **modelled price impact only**.
2. **No statistical inference anywhere.** A word scan finds **zero** occurrences of `t-stat`, `p-value`, `standard error`, `Newey`, or `statistically significant` in an inferential context. No confidence interval, placebo, bootstrap or multiplicity control accompanies any return/Sharpe improvement in Table 3 or §6.3.
3. **µ is selected on the in-sample peak and then reported out of sample** (Table 3, §6.2): "We choose the µ value that maximizes the in-sample expected return (or Sharpe ratio) … We expect the in-sample and OOS curves to peak at relatively close µ ranges" — an expectation, not a test. This is per-method, per-AUM selection (12 methods × 4 AUM × 2 objectives).
4. **Single split, explicitly non-rolling.** One 3-year train / 2-year test partition of 2018–2022, "We avoid re-sampling methods such as cross-validation and rolling-window re-estimations" (§2.2). There is no walk-forward protocol, no frozen forward window, no sub-period decomposition of any gain, and no regime breakdown.
5. **The headline economics rest on an artificial target.** The §6.2 strategy is a simulation whose signal is *defined* to be right 1% of the time with perfect directional knowledge of a 5-day move, and whose before-cost Sharpe is ~7. The $10b/$1b improvements are therefore the cost of implementing a hypothetical, unachievable target — the paper calls it "an unachievable target" (§1).
6. **Better statistical forecasts can be economically worse than the naive baseline.** Table 2 Panel A′ at $10m: `nntech` −12.8, `rnntech` −17.7, `nnall` −25.9, `rnnall` **−32.1** — i.e. all non-fine-tuned ML forecasts *lose* to `ma5` at small AUM, and even `olstech`/`olsall` are ≈ 0 to negative (−0.3, −3.3).
7. **Fine-tuning buys economics by sacrificing accuracy.** Table 2 Panel B′ shows negative R² for the economically fine-tuned models (e.g. `nn.econall` −352.5 and `rnn.econall` −79.5 at $10m; −34.9 and −9.0 at $100m). The "alpha" is thus not better volume measurement but a deliberate, loss-function-driven bias — valuable only if the assumed cost functional form is right (see item 1 and F7).
8. **Adding the 147 fundamental predictors makes models slightly worse** (Table 1: `nn` 14.90 → 14.42; `rnn` 16.25 → 15.47 when `fund-2` enters), which the source attributes to overfitting "when the number of features increases and where we do not use regularization techniques" (§3.2). Lasso/ridge were tried and gave no significant improvement (footnote 15).
9. **Mixture-of-experts fails for the neural models** (Table C.2: `nn+moe` 17.78 < `nn` 18.45; `rnn+moe` 18.26 < `rnn` 19.86 jointly; only `ols+moe` improves) — heterogeneity across size groups is not solved by splitting the sample.
10. **The least predictable names are the costliest ones.** Nano-group R² is 16.63 vs mega 32.02 for `rnnall` (Table C.2), and the source concludes tiny firms are "not only costly to trade in general, but their costs are less predictable" — precisely where the impact term is steepest.
11. **The economic benefit collapses as AUM falls.** Table 3 at $10m: 13.20% → 13.30% return and 6.55 → 6.68 Sharpe (`rnn.econall` vs `ma5`), i.e. a ~0.1pp improvement — and the source concedes that at small trade sizes "per-unit trading costs such as bid-ask spread" would dominate, which its model omits.
12. **The benchmark for the factor experiment is deliberately naive.** Gains are measured against `ma5` volume forecasting, not against a realistic execution benchmark (VWAP-scheduled rebalance, participation-capped algorithm, or a standard transaction-cost-aware optimizer). The counterfactual "no volume model at all" is not implemented.
13. **In-sample selection at the portfolio level too.** For the 153 factors a single µ is picked to "optimize the average gain across all factors" — chosen on the same factor set on which the average gain is then reported (§6.3).
14. **No turnover or capacity is printed for any reported configuration** (Eq. 15 defines it; Figures 5–7 only plot it), and there is no ADV, participation or dollar-capacity constraint anywhere — so none of the reported Sharpe values can be checked against a realistic sizing limit.
15. **Long–short targets with no borrow/shorting cost or availability model**, though every factor and simulated target shorts 50% of AUM.
16. **Source-internal inconsistency (headline number):** §6.2 prose "8.98%" vs Table 3 `rnn.econall` $1b "8.95%" (recorded in frontmatter `contradictions`).
17. **Source-internal inconsistency (magnitude claim):** §1 says the $1b improvement "can be as much as double in terms of expected returns or Sharpe ratio"; Table 3 supports >2× only for Sharpe (2.21 → 4.53) and shows +38% for mean return (6.47 → 8.95) (recorded in frontmatter `contradictions`).
18. **Version metadata is unreliable:** SSRN advertises a 9 Apr 2026 revision and duplicates Moskowitz in its suggested citation, while serving a file byte-identical to the NBER October 2024 PDF (frontmatter `contradictions`). A reader following "last revised" cannot obtain a different document.
19. **Reproducibility:** no code, no replication package, no data-availability statement (full-text scan), proprietary inputs (JKP characteristics dataset, Capital IQ Key Developments), and no vendor/exchange named for the price-volume panel.
20. **Regime coverage is unexamined.** 2018–2022 spans the COVID volume surge and the 2022 bear market, yet no gain is ever decomposed by year or regime; volume dynamics are precisely what changed most in 2020.
21. **Not peer reviewed** (NBER cover statement), with a disclosed AQR consulting relationship for one co-author.

## Falsification plan

Every threshold below is a **research-defined falsification threshold** and every construction choice is **research-proposed**; none of them is specified by the source. Each test has a pre-declared failure rule that cannot be rescued by unconstrained retuning.

- **F1 — Frozen forward replication on a real target.** Re-run the §6.1 recursion over a point-in-time US universe with a *realistic* target (the JKP monthly sorts), fixing µ **before** the window opens (no in-sample peak search), on a ≥ 12-month window ending after 2026-12. **Pass:** `rnn.econall` beats `ma5` by ≥ 1.0%/yr mean return **and** ≥ 0.30 Sharpe, with a stationary-block-bootstrap 95% CI on both differences excluding 0. **Fail:** either point estimate ≤ 0 or either CI includes 0.
- **F2 — Full cost ladder (per-unit costs added to impact).** Add commission + spread of 0 / 1 / 2 / 5 / 10 / 20 bp per side on top of the paper's impact term, plus a 25 bp/yr stock-loan rate on the short leg. **Fail** if the F1 gain is ≤ 0 at 5 bp per side, or if >50% of the gain is erased at 10 bp per side. (Cost grid is `research-proposed`; the source has no per-unit cost at all.)
- **F3 — Decisive mechanism test (sham forecast).** Replace the volume forecast with (a) a circularly shifted volume series, (b) a random `z` matched to the method's average trading rate, and (c) `ma5`, holding µ fixed. **Fail** if `rnn.econall` does not beat the matched-rate sham (b) with a bootstrap CI excluding 0 — that would show the gain comes from trading *less*, not from volume *information*.
- **F4 — Equal-aggressiveness control.** Re-tune µ separately for every method so all share the identical `avg z` (0.13/0.57/0.78/0.95), then re-compare. **Fail** if the method ranking disappears (all pairwise gaps within ±0.2%/yr) — the reported ordering would be a µ artefact.
- **F5 — Permutation null.** 1,000 draws shifting each stock's `η̃` series by independent random offsets, rebuilding forecasts and portfolios each time. **Fail** if the observed gain does not exceed the 95th percentile of the placebo distribution.
- **F6 — Monotone-benefit gate across AUM.** Require `rnn.econall` ≥ `ma5` in **all four** AUM cells of Table 2 Panel A′ (Table 2 currently shows −32.1% at $10m for `rnnall` and 51.0% for `rnn.econall`). **Fail** if any economically fine-tuned cell is negative vs the `ma5` baseline.
- **F7 — Cost-functional-form robustness (decisive for the "economic loss" claim).** Re-run with (i) the linear-in-participation form 0.1·participation (paper), (ii) the paper's own footnote-17 form `λ̃ = 0.2/√V`, (iii) a square-root impact law, and (iv) an empirically estimated Kyle λ from realized data. **Fail** if the sign of the gain flips in any of (ii)–(iv) — the entire fine-tuning result is conditional on one assumed cost shape.
- **F8 — Multiplicity audit.** Benjamini–Hochberg at q < 0.10 over the reported grid (12 methods × 4 AUM × 2 objectives, plus the 153-factor panel). **Fail** if the headline $1b Sharpe improvement does not survive.
- **F9 — Sub-period stability.** Require positive gain in ≥ 3 of 4 sub-periods (2018–2019, 2020, 2021–2022, and the frozen F1 window). **Fail** if all of the benefit sits in 2020's volume regime.
- **F10 — Capacity / participation audit.** Cap every trade at 10% and 20% of trailing-20-day dollar ADV. **Fail** if the gain at 10% ADV is ≤ 0 (the model contains no participation cap, so this is untested by the source).
- **F11 — Execution-benchmark horse race.** Compare against a VWAP-scheduled, participation-capped rebalance of the same target (not against `ma5`). **Fail** if the ML volume model adds ≤ 0.2%/yr over that realistic baseline — the practical value would then be subsumed by ordinary execution scheduling.
- **F12 — Forecast-quality floor.** Require positive out-of-sample volume-shock R² (`η̃`, Table 1 Panel A definition) for the deployed model in the F1 window. **Fail** if R² ≤ 0, since the economic loss assumes the forecast carries information about future liquidity.

Action on failure: mark the mechanism `falsified-in-our-tests` for the failing axis only, keep the record `research-only`, and do not promote it to the candidate pool.

## Crypto portability

**adapted** (empirical crypto validity: `unproven`).

The mechanism is venue-agnostic in *form* — forecast next-period dollar volume, convert to a participation-based impact cost, and pace trades toward a target — and dollar volume is published by every crypto venue for every pair, so the signal can be reconstructed without conceptual change. It is **not** `direct`: the source contains **zero** crypto evidence, and its calibration (the 0.1 impact coefficient, the 0.2 in `λ̃ = 0.2/Ṽ`), its universe definition and all of its performance numbers come from 2018–2022 US equities.

Crypto-specific porting risks, none addressed by the source:

- **24/7 sessions and candle boundaries:** "day t" volume in equities is one regular session; crypto has no closing auction, so volume is window-dependent and the "start of day t" trade instant must be defined by convention (`research-proposed`: UTC 00:00 boundary, stated explicitly).
- **Funding and carry:** perpetual-funding payments every 8 hours are a real holding cost that the paper's cost term cannot represent at all — `data gap`.
- **Mark / index price, liquidation, leverage:** absent from the source; any margined implementation needs a liquidation and maintenance-margin model before the impact-only cost ladder means anything.
- **Venue fragmentation and thin books:** dollar volume is per-venue; aggregating across venues changes the denominator of the participation rate, and impact in a thin book is not linear in participation over wide ranges — the paper's own footnote 17 admits alternative functional forms.
- **Candle/timestamp conventions, weekend liquidity, and stablecoin quote currencies** all change the volume series and are unexamined.
- **Borrow / short availability** on crypto differs materially and is unmodelled.

Until an F1-style frozen-forward test exists on a crypto universe with funding and per-unit fees included, portability stays `adapted` with `unproven` performance.

## Limitations

Markers used: `underspecified`, `data gap`, `not independently reproduced`, `unproven`, `ex-post selection`.

- **`data gap` — execution layer:** no commissions, fees, spread (explicitly deferred to future work), slippage beyond the impact term, participation cap, capacity, borrow, financing, margin, funding, latency, order type or fill model anywhere in the pinned PDF.
- **`data gap` — universe construction:** no exchange, data vendor, listing screen, delisting/survivorship treatment or point-in-time membership rule is printed; only NYSE size breakpoints and a ~4,700-stock cross-section are stated.
- **`data gap` — turnover and capacity:** defined in Eq. 15 but never tabulated; only figure axes are available.
- **`data gap` — inference:** no t-statistics, p-values, standard errors, confidence intervals, placebo or multiple-testing control anywhere.
- **`data gap` — reproducibility:** no code, no replication package, no data-availability statement; proprietary inputs (JKP characteristics, Capital IQ Key Developments).
- **`underspecified` — train/test boundary dates** within 2018–2022 (only "3-year training, 2-year testing" is printed).
- **`underspecified` — execution price and timezone** for the "start of day t" trade, and treatment of halts/suspensions/missing bars.
- **`underspecified` — µ grid and the numeric µ used in the 153-factor experiment**; per-method µ is selected on the in-sample peak.
- **`underspecified` — the 5-day simulated signal vs. daily re-targeting** interaction.
- **Model dependence:** the whole result is conditional on one linear-in-participation cost shape with a hard-coded 0.2/0.1 coefficient borrowed from another paper's empirical estimate, with cross-impact and all other cost determinants assumed away (§4.1 footnote 17).
- **Target dependence:** §6.2 economics rest on a simulated, unachievable target; §6.3 rests on a naive `ma5` counterfactual rather than a realistic execution benchmark.
- **Regime coverage:** one 2018–2022 window with no sub-period decomposition, in a period containing an unprecedented volume surge.
- **`not independently reproduced`** for every number in the Evidence section.
- **`unproven`** for crypto performance and for any period after 2022-12.
- **Not peer reviewed**; NBER working-paper status with a disclosed AQR consulting relationship for one co-author and unreliable SSRN revision metadata.

## Implementation status

`implementation_status: not-implemented`.

No implementation exists in our research stack. No volume-forecasting model has been trained, no cost model has been calibrated, no portfolio has been simulated, and no Paper, Testnet or Live verification of any kind has occurred. This record is a normalised research capture of a third-party working paper only.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

The presence of this record in this repository does **not** mean it passed Research Intake Review, entered Hermes Wiki Brain, entered the production candidate pool, completed Qlib full-backtest validation, became a frozen survivor or leaderboard entry, is profitable, is validated alpha, is approved for implementation, paper trading, testnet, or live trading. None of those steps has happened. Note also that the source's own contribution is an *implementation* improvement, not a return signal: adopting it could only reduce modelled cost, never generate return on its own.

## Related Wiki records

Pre-write `kb_search` in Hermes Wiki Brain (canonical spec re-read this run: `quant/strategy-research-record-spec-v1.md`, 10289 bytes, sha256 `4561578a2a991aaa8252b31a8b6fd0a46b98c853ef77599521436ee6ff2fcaa7`; `quant/strategy-research-record-spec-v2.md` → file not found, so **v1 remains canonical**) on `trading cost prediction volume implementation portfolio optimization participation rate` returned 6 pages, of which one is materially adjacent; a second search on `market impact trading cost liquidity prediction execution capacity backtest` returned 10 pages, of which three are mechanism-adjacent. Verified existing pages only:

- `quant/smart-predict-then-optimize-spo-plus-robust-portfolio-2026-09-05.md` — decision-focused learning that optimizes a decision under turnover costs; same "economic loss instead of statistical loss" family, different source and different object (portfolio weights vs. trading rate).
- `quant/order-flow-imbalance-predictive-decoupling-cost-falsification-2026-09-12.md` — microstructure taker-cost falsification; different source, different mechanism (order-flow signal vs. volume-forecast pacing).
- `quant/crypto-funding-carry-fade-turnover-cost-dissipation-falsification-2026-09-12.md` — turnover-cost dissipation as the falsifier; different source and universe.
- `quant/chronos-foundation-transformer-statistical-arbitrage-factor-residuals-2026-09-12.md` — turnover-cost fragility of a learned signal; different source and mechanism.

**No Wiki Brain page covers volume forecasting as a cost input, participation-rate pacing, or this source identity**; nothing was written to Wiki Brain by this run, and no existing record was updated.

Repository neighbours cited for dedup/distinction only (not Wiki links): `reviving-anomalies-expected-net-return-double-sort-1n-implementable-2026-09-23.md`, `limt-hierarchical-multitask-liquidity-aware-ashare-cross-sectional-apo-2026-09-23.md`, `equity-order-flow-kyle-lambda-cross-sectional-liquidity-premium-2026-09-03.md`, `forecast-to-fill-gold-futures-friction-adjusted-kelly-alpha-2026-09-02.md`, `moving-average-distance-cross-sectional-anchoring-us-equity-ssrn-3111334-2026-09-26.md`.

## Sources

- Goyenko, R., Kelly, B. T., Moskowitz, T. J., Su, Y., & Zhang, C. (2024). *Trading Volume Alpha*. NBER Working Paper No. 33037. DOI: https://doi.org/10.3386/w33037 — landing page https://www.nber.org/papers/w33037 (fetched 2026-09-27, HTTP 200; `citation_publication_date 2024/10/07`, issue date "October 2024", no revision date).
- **Pinned full text:** https://www.nber.org/system/files/working_papers/w33037/w33037.pdf — **1,175,371 bytes, 53 pages, SHA-256 `0d34e7545c767a6d08899aac16f2b31f5fab783f3b603f00d8463f6cf0c95325`**, downloaded and read end to end 2026-09-27. All quantitative claims above trace to this file: Abstract (p.2); §1 (pp.3–8, including the 20–100 bps factor range and the $1b double-claim); §2.1–2.4 (pp.8–13, participation-rate definition, 2018–2022 sample, 175 predictors); §3.1–3.2 (pp.13–17, Table 1); §4.1–4.3 (pp.17–21, equations 1–9, `λ̃ = 0.2/Ṽ`, `PriceImpact = 0.1·Δx/Ṽ`, footnotes 16–20); §5.1–5.3 (pp.21–31, Propositions 1, Table 2, Figures 2–4); §6.1–6.3 (pp.30–37, equations 13–15, Table 3, Figure 7, the bid-ask deferral sentence in §6.2); §7 (pp.37–39); References (pp.39–42); Internet Appendix A.1 (pp.42–45, Table A.1, Figure A.1); B.1–B.4 (pp.44–50, Propositions 2–4, equations 16–32); C.1–C.2 (pp.50–53, Table C.2, Figures C.3–C.4).
- https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4978835 — SSRN mirror landing, read 2026-09-27 in a browser after clearing the Cloudflare challenge, for `53 Pages`, `Posted: 8 Oct 2024`, `Last revised: 9 Apr 2026`, `Date Written: October 2024`, the 2-versions marker, the copyright line ("No reuse allowed without permission"), the statistics block (83 downloads / 2,142 abstract views / 1 citation / 39 references) and the duplicated-Moskowitz suggested citation.
- https://papers.ssrn.com/sol3/Delivery.cfm/nber_w33037.pdf?abstractid=4978835&mirid=1 — SSRN copy of the PDF, fetched in-session 2026-09-27 and hashed: **1,175,371 bytes, SHA-256 `0d34e7545c767a6d08899aac16f2b31f5fab783f3b603f00d8463f6cf0c95325`**, byte-identical to the NBER pin.
- Cited by the source and used only for mechanism framing (not as independent evidence here): Kyle, A. S. (1985), *Econometrica*; Frazzini, A., Israel, R., & Moskowitz, T. J. (2018), *Trading Costs*, DOI 10.2139/ssrn.3229719; Gärlänu, N., & Pedersen, L. H. (2013), *Journal of Finance* 68:2309–40; Jensen, T. I., Kelly, B., & Pedersen, L. H. (2022), *Journal of Finance*; Gu, S., Kelly, B., & Xiu, D. (2020), *RFS* 33:2223–73; DeMiguel, V., Martin-Utrera, A., Nogales, F. J., & Uppal, R. (2020), *RFS* 33:2180–222; Novy-Marx, R., & Velikov, M. (2016), *RFS* 29:104–47; Harvey, C. R., Liu, Y., & Zhu, H. (2016), *RFS* 29:5–68.
