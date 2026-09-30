---
schema: strategy-research-record-v1
title: "On-Chain Profitability and Macro Momentum Forecast One-Day DVOL Changes Out of Sample but Fail Gross-to-Net Under a Spot-Normalised Payoff (XGBoost vs AR(1)-GARCH(1,1), SSRN 7073558)"
created: 2026-10-01
updated: 2026-10-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-01
sources:
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7073558"
  - "https://papers.ssrn.com/sol3/Delivery.cfm/7073558.pdf?abstractid=7073558&mirid=1&type=2"
  - "https://doi.org/10.2139/ssrn.7073558"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Section 3.8 and Appendix A.4 give the active-signal confidence threshold as 0.2510 and describe it in one phrase as 'set in the test period' and in the next as 'the value selected by validation', while Section 4.6 describes the swept thresholds as 0.1 to 0.4 standard deviations of the predicted distribution; the provenance (test window versus validation only) and the unit (IV points versus standard deviations) of 0.2510 are both internally inconsistent, and test-period threshold selection would be tuning inside the held-out window."
  - "Table 4.2 prints a Buy-and-Hold Sharpe ratio of 1.78 next to an annualised return of 108.19 percent, annualised volatility of 45.85 percent and a stated 2 percent risk-free rate; the standard (mu - rf) / sigma formula gives 2.32 and the log-return variant gives 1.56, so the printed Sharpe does not reconcile with the printed return and volatility under either convention and the convention itself is not stated."
  - "Table 4.2 reports a 0.00 percent daily win rate whose note attributes it to net-of-cost outcomes, and the same note states that profit factor is undefined because 'the numerator (gross profits) is zero'; gross and net are used inconsistently in a single note, and with a DVOL-change target centred at zero (mean near zero, standard deviation about 2.6 IV points per Section 4.1) over the roughly 24 active days implied by the printed 7.79 percent active ratio, exactly zero gross-positive active days is improbable."
  - "Section 3.5 reports a working panel of approximately 1,540 daily observations split into roughly 1,225 training and 308 test observations, but 1,225 + 308 = 1,533, leaving 7 observations unaccounted for; the words approximately and roughly hedge the gap but no reconciliation is given."
  - "Section 2.8 states H4 in null-versus-alternative form with no decision rule, and Section 4.5.4 then reports H4 as 'qualitatively consistent with the alternative' while conceding it is 'the hypothesis that is most difficult to test crisply'; a hypothesis is declared supported without a pre-specified test or threshold."
---

# On-Chain Profitability and Macro Momentum Forecast One-Day DVOL Changes Out of Sample but Fail Gross-to-Net Under a Spot-Normalised Payoff (XGBoost vs AR(1)-GARCH(1,1), SSRN 7073558)

## Provenance

**Primary source (single pinned version).** Anuj Pal, `Forecasting Bitcoin Implied Volatility: On-Chain Signals, Belief Formation, and Limits to Arbitrage`. Cover page: single author Anuj Pal, `MBA (Finance), (2024 - 2026)`, submitted `20 - 05 - 2026`, supervised by `DR. ALOK YADAV`, at `ARUN JAITLEY NATIONAL INSTITUTE OF FINANCIAL MANAGEMENT (Ministry of Finance, Government of India)`, labelled `Master's Dissertation`. SSRN landing page: `abstract_id=7073558`, `64 Pages Posted: 24 Jul 2026`, `Date Written: May 20, 2026`, suggested citation DOI `10.2139/ssrn.7073558`, license cell `The copyright holder has granted SSRN a license. All rights reserved. No reuse allowed without permission.`, SSRN reference and citation metadata both `0 References / 0 Citations`, paper statistics `DOWNLOADS 76 / ABSTRACT VIEWS 246` as read on 2026-10-01. Keywords printed on page 4: `Bitcoin, Implied Volatility, DVOL, Crypto Derivatives, On-Chain Analytics, SOPR, NUPL, GARCH, XGBoost, SHAP, Limits to Arbitrage, Vega, Belief Formation, Machine Learning, Behavioural Finance.` JEL printed on page 4: `G12, G13, G14, G17, G41, C53, C58`.

**Publication status:** preprint / master's dissertation only. There is no journal reference, no publisher DOI beyond the SSRN DOI, no peer-review statement, and no ORCID anywhere in the pinned text (`peer 0`, `orcid 0`; the single `referee` occurrence is the phrase `refereed finance journals` in Section 2.3). It is not a peer-reviewed paper and must not be read as one.

**Primary-source checksum (three artefacts, all fetched 2026-10-01):**
- Landing page HTML, `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7073558`, 72,179 bytes, SHA-256 `fe1f8d775cca3e481f6a52b9c8d737b7c3a21be207ca63b1bf347deb41946bb3`.
- Full text PDF through the landing-page `Open PDF in Browser` link `https://papers.ssrn.com/sol3/Delivery.cfm/7073558.pdf?abstractid=7073558&mirid=1&type=2`, which redirects to `download.ssrn.com/2026/7/7/7073558.pdf`: 852,159 bytes, magic `%PDF-1.7`, SHA-256 `9b5d2d878228712949c76268c09c67f9dc71ce99b911b291f08501d3d5539bde`. PDF metadata: `/Producer 3.0.38 (5.1.21)`, `/ModDate D:20260630174233+02'00'`, no `/Title` entry.
- Body extracted from that PDF with `pypdf` into 64 pages, 143,394 characters, 143,723 bytes, 2,133 lines, SHA-256 `ec00dbe59c2d48286128e443204ecf00e08aa26570d8a30d0ceb5326182f03d9`, read end to end covering the cover page, acknowledgements, abstract, keyword and JEL block, table of contents, `LIST OF TABLES` (Table 2.1, Table 4.1, Table 4.2), `LIST OF FIGURES` (Figures 4.1 to 4.4), Chapters 1 to 5 with Sections 1.1 to 1.6, 2.1 to 2.9, 3.1 to 3.10, 4.1 to 4.7 and 5.1 to 5.8, the full `REFERENCES` list, the `Data Sources and Software` block, and Appendices A.1 to A.5.

**Version and date:** a single SSRN version as posted (no v1/v2 suffix on the abstract page, no arXiv counterpart, no competing preprint located). Manuscript dateline 20 May 2026, cover-page submission date 20-05-2026, SSRN posting 24 July 2026.

**Sample period, universe, cost treatment and performance numbers** are recorded in `## Required data`, `## Execution assumptions` and `## Evidence` below, each with section or table provenance. A DOI redirect probe against `https://doi.org/10.2139/ssrn.7073558` returned HTTP 429 during this run, so the DOI string is taken from the SSRN `Suggested Citation` field on the pinned landing page rather than from a successful DOI resolution; that resolution gap is a `data gap` and is not treated as verification.

**Deduplication and spec resolution (this run).** The canonical specification was resolved read-only: `quant/strategy-research-record-spec-v2.md` was file-not-found in the Wiki Brain vault, so the run failed closed onto `quant/strategy-research-record-spec-v1.md`, canonical at 10,289 bytes, SHA-256 `4561578a2a991aaa8252b31a8b6fd0a46b98c853ef77599521436ee6ff2fcaa7`; zero Wiki pages were written. Pre-write dedup was run over the whole checkout hidden-inclusive (`*.md` under `.git`, `.mimo-worktrees`, `.agents`, `.hermes`, plus `coverage_manifest.csv` at 5,808 lines) for the canonical source-identity probes `7073558`, `ssrn.7073558`, `10.2139/ssrn.7073558`, the exact title `Forecasting Bitcoin Implied Volatility`, the title fragment `Belief Formation`, `Anuj Pal`, `ALOK YADAV`, `Arun Jaitley National Institute of Financial Management`, the abbreviation `AJNIFM`, and the target phrase `one-day-ahead change in DVOL`: every probe returned 0 files before the write and exactly this record after the write (the `AJNIFM` abbreviation still returns 0 after the write because this record spells the institution in full), and `coverage_manifest.csv` returned 0 for `7073558`. Mechanism probes counted with this record excluded, i.e. the pre-write state: `DVOL` 66 files hidden-inclusive and 26 at top level, `SOPR` 22 and 8, `NUPL` 8 and 4, `XGBoost` 120 and 52, `GARCH` 120 and 49, `implied volatility` 175 and 67, over 1,112 top-level records; none of those files pairs on-chain state variables with the DVOL change target. The positive control `novy-marx` counted 62 files before the write and 63 after, the sole increment being this record's own dedup sentence. `git log --oneline -20` was used as a convenience glance only (head `0be8c22`, one record, read in full before research), and `git pull origin main` was run before research and again before commit.

**Four-axis distinction against the closest existing repository records** (mechanism, signal construction, universe, horizon, material data dependency): `crypto-options-dvol-iv-premium-shock-spot-predictor-2026-09-13` runs DVOL shocks as a *spot* predictor from a GitHub signal implementation; `btc-option-implied-vov-predicts-excess-returns-risk-premia-2026-09-19` predicts *BTC excess returns* from option-implied volatility-of-volatility; `crypto-volatility-risk-premium-variance-swap-estimator-fragility-decay-2026-09-12` harvests a variance risk premium rather than forecasting the index change; `crypto-btc-iv-60d-30d-term-structure-regime-filter-2026-09-15` is an IV term-structure regime filter; `bitcoin-onchain-sopr-spent-output-profit-ratio-2026-08-31` and `bitcoin-onchain-net-unrealized-profit-loss-nupl-macro-cycle-2026-09-01` use SOPR and NUPL as *price and cycle* signals with no volatility target; `crypto-kalshi-prediction-market-macro-repricing-volatility-forecasting-2026-09-01` forecasts *realised* volatility from prediction-market repricing; `tradingview-bitcoin-dvol-implied-realized-range-regime-2026-09-21` is a chart-level regime indicator. Every pair differs in at least one of source identity, target variable, signal construction, information set, horizon or material data dependency.

## Economic mechanism

### Source-reported

The author's stated mechanism has three linked parts, all from Sections 1.1, 2.8 and 4.5:

1. **Statistical channel.** One-day-ahead changes in Deribit's 30-day Bitcoin implied volatility index `DVOL` are not a random walk; `publicly observable state variables` - short-horizon spot price dynamics, on-chain profit measures (`SOPR`, `NUPL`), macroeconomic momentum (effective federal funds rate, CPI, DXY) and sentiment or attention proxies - contain incremental information about the next-day change when combined by a nonlinear tree ensemble, beyond what a linear `AR(1)-GARCH(1,1)` benchmark extracts (H1, H2 in Section 2.8).
2. **Source-of-information channel.** The information is attributed to belief formation and balance-sheet stress: `SOPR` ranks second in gain-based importance behind the one-day price change, and federal funds rate momentum ranks third, which the author reads as `on-chain positioning and macro-financial integration` feeding the price of risk (Sections 4.3.1, 4.3.3, 4.5.2).
3. **Monetisation channel.** Statistical predictability does not survive translation into money because of (a) limits to arbitrage in a market with wide option spreads, episodic shocks and capital-constrained volatility sellers, and (b) an intentionally conservative payoff mapping that normalises IV-point PnL by spot price instead of option Vega (Sections 3.8, 4.4, 4.5.4, 5.7). The source's own words: the negative economic result `reflects payoff mis-specification and execution frictions consistent with limits-to-arbitrage interpretations` rather than model failure (H4, Section 4.5.4).

### Research interpretation

Falsifiable restatement of the hypothesis this record captures, using our terms rather than the author's:

- **Predictability claim (the alpha-relevant claim):** a fixed, chronologically trained nonlinear model over a 37-feature daily panel of price, on-chain, macro and sentiment state produces positive out-of-sample explanatory power for the next-day DVOL change against a constant-mean reference, and beats an AR(1)-GARCH(1,1) benchmark estimated on the identical training window. Source-reported magnitude: out-of-sample R-squared `0.0527` versus `-0.0107` (Table 4.1). This is a signal-existence claim about the *volatility price*, not about spot direction, and it is the part that could support a Vega-consistent implementation.
- **Economic claim (the source's own negative result):** under a *spot-normalised* payoff with a flat 5 basis point proportional cost the same signal loses money (`Total Return -1.18%`, `Sharpe Ratio -13.40`, `Win Rate (Days) 0.00%`, Table 4.2). We record this as evidence about *that mapping only*. Because the mapping divides an IV-point numerator (typically 1 to 2 points) by a spot denominator of order 10^5 USD, the author explicitly designed it as a stress test (Sections 1.5, 3.8), and Section 4.6 reports the strategy is still slightly negative at *zero* transaction cost. A cost-elimination that does not flip the sign therefore cannot distinguish "signal is uneconomic" from "payoff is mis-specified"; the two are only separable under a Vega-scaled, contract-level backtest, which the source did not run and which we label `research-proposed`.
- **Component roles (this is not a multi-component trading system):** there is no regime filter, no entry trigger family, no stop and no sizing rule in the source. The only operational choices are (i) the fitted model and its hyperparameters, (ii) the binary active-signal threshold `0.2510`, and (iii) the flat cost and daily loss cap of the evaluation harness. Any further operationalisation (which option, what Vega, what hedge, what size) is absent and must be `research-proposed` or `data gap`.

## Signal

**Formation timestamp and availability.** The unit of observation is one row per UTC daily close (Section 3.2: `day t corresponding to the UTC daily close`). Features are those observable at the close of day `t`; the target is `y_t = iv_(t+1) - iv_t`, the DVOL close-to-close change from day `t` to day `t+1` (Section 3.3). The forecast therefore becomes available at the close of day `t+1` if read at the same close convention; the source does not state an execution timestamp, so any signal-to-order timing is `underspecified`.

**Lookback.** All series are aligned to a common daily calendar. Rolling features: 7-day and 30-day realised volatility of daily log returns annualised by `sqrt(365)`; a 7d/30d volatility ratio; 1-day, 7-day and 30-day price changes; 20-day simple moving average; 14-day RSI; 14-day ATR; daily high-low ratio; trailing-average volume ratio; 30-day momentum (current value minus value 30 calendar days earlier) for effective federal funds rate, CPI and DXY; continuous wavelet transform features on close and on NUPL at scales `s7`, `s14`, `s30`. Panel burn-in means the sample starts 2021-05-12 although DVOL exists from 2021-03-24 (Section 3.2). Correlation filter: pairwise Pearson threshold `0.9`, dropping the member with lower univariate target correlation, leaving `37` features (Sections 3.4, 3.4.7). Macro momentum series are winsorised at the 0.5 and 99.5 percentiles (Section 3.4.7).

**Model (source-reported, exact from Section 3.6.1 and Appendix A.2).** XGBoost regression minimising RMSE, hyperparameters selected by Optuna inside the training sample under expanding-origin time-series cross-validation with fixed 90-day validation slices: `n_estimators 700`, `learning rate 0.17292525837569978`, `maximum depth 5`, `subsample 0.6975385443596863`, `colsample_bytree 0.706302795307037`, `min_child_weight 5.291902898025456`, `gamma 3.704663181116507`, `reg_lambda 3.9691391983558075`, `reg_alpha 2.512314360688117`, early stopping with patience 50 on the final fit. Benchmark: `AR(1)` conditional mean plus `GARCH(1,1)` conditional variance, quasi-maximum likelihood via the `arch` package, estimated on the same training window with parameters held fixed out of sample (Section 3.6.2). The Optuna search space, trial count and random seed are `not stated in source`.

**Entry / exit / holding (source-reported, Section 3.8 and Appendix A.4).**
- Active-signal indicator `signal_t in {0,1}`, equal to one on days where the predicted change exceeds a confidence threshold `0.2510`.
- `PnL_IV_t = signal_t * delta_iv_(t+1)`.
- `Return_raw_t = PnL_IV_t / P_t` where `P_t` is contemporaneous Bitcoin spot.
- `Return_net_t = Return_raw_t - (0.0005 * signal_t)`, a proportional five basis point cost on active days.
- Daily losses capped at `-5%`.
- Position size, direction convention, contract choice, re-entry, overlapping positions and stop rules: `underspecified`. The sign of `PnL_IV` implies a long-implied-volatility direction on active days, but the source never states a position, a strike, an expiry or a hedge, so this is an inference from the formula, not a source-reported trading rule.

**Parameters (all source-reported unless marked).** Threshold `0.2510` (units ambiguous, see contradiction 1); cost `5 bps` with robustness at `2` and `10 bps` and a `0 bps` case (Sections 3.8, 4.6); threshold sweep `0.1` to `0.4` standard deviations (Section 4.6); daily loss cap `-5%`; risk-free rate `2%` for Sharpe; wavelet block optional in a robustness run; rolling re-fit cadence `60 days` (Section 4.6). Anything not on that list is `research-proposed`.

**Whether the rule is fully specified:** no. The signal is reconstructable as a *forecast*, not as a *trade*. Reproducing the economic row of Table 4.2 additionally requires the threshold's unit and provenance (both contested) and the annualisation convention (see below).

## Required data

- **Instrument / universe:** Bitcoin spot (return and normalisation leg) and the Deribit 30-day `DVOL` index (target). Single asset, single index, no cross-section, no option chain used (Sections 1.5, 3.2).
- **Venue and market type:** Binance spot for OHLCV; Deribit for DVOL; on-chain data from public ledgers; macro from FRED; attention from Google Trends. Market type: crypto spot plus a crypto options *index*; no derivatives contract is traded in the source.
- **Timeframe:** daily, UTC close alignment (Section 3.2).
- **Fields used:** open, high, low, close, volume (Binance); DVOL level (Deribit public statistics endpoint); market capitalisation and realised capitalisation (CoinMetrics) for `NUPL = (Market Cap - Realised Cap) / Market Cap`; `SOPR` = aggregate realised value at spend divided by realised value at acquisition; miner outflow from known miner-associated address clusters (Google Cloud Public Datasets, BigQuery); effective federal funds rate, headline CPI, DXY (FRED); Google Trends daily `Bitcoin` search intensity; daily averages of transformer-based social-media sentiment (`avg_sentiment`, `sentiment_volume`); wavelet coefficients via PyWavelets.
- **Point-in-time:** strictly chronological split; train `2021-05-12` to `2024-09-20` (about 1,225 rows), sealed test `2024-09-21` to `2025-07-25` (about 308 rows), panel about 1,540 rows (Section 3.5). Lower-frequency macro series are forward-filled *respecting release calendars* so a monthly CPI print is visible only on or after its release date (Section 3.2). Hyperparameter selection uses only training-window folds (Sections 3.6.1, 3.9).
- **Timestamp and timezone:** daily UTC close; clock source and intraday precision `not stated in source`. Out-of-order record handling `not stated in source`.
- **Missing data:** XGBoost default-direction splits handle missing values; macro momentum clipped at 0.5/99.5 percentiles; no explicit imputation policy is stated beyond that, and any other null, stale or suspended-row treatment is a `data gap`.
- **Provider gaps (`data gap`, reproducibility-relevant):** `SOPR is reconstructed from publicly available historical series following the standard methodology` - provider, heuristics and version are `not stated in source` (Section 3.2). The sentiment transformer, training corpus and platform are `not stated in source`; `TimeLMs` is cited only in the literature review, not declared as the construction actually used (Section 2.4.6 versus Appendix A.1.4). On-chain miner tagging relies on judgement-call entity heuristics, which the source itself flags (Section 3.9).
- **Availability window and staleness:** DVOL exists from 2021-03-24; the sample stops `2025-07-25`, so the pinned evidence is roughly fourteen months stale relative to `source_as_of: 2026-10-01`.
- **Funding / fee / spread needs:** none are *used* by the signal; all are `data gap` in the evaluation (see next section).

## Execution assumptions

**Source-reported (Sections 3.8, 4.6, Appendix A.4; census over the pinned 143,394-character text layer).**
- The only modelled friction is a flat proportional `five basis point` cost applied to active days (`Return_net = Return_raw - 0.0005 * signal`), robustness-checked at `2` to `10 basis points` and at zero.
- A `-5%` daily loss cap truncates the left tail of every performance statistic (Table 4.2 note: `Daily losses are capped at -5%`).
- Sharpe uses a `2% annual risk-free rate`; annualisation is implicit in the printed metrics - recomputing `(1 - 0.0118)^(365/308) - 1 = -1.40%` and `(1 + 0.8566)^(365/308) - 1 = 108.18%` reproduces the printed `-1.40%` and `108.19%` to two decimals, so the source annualises on a 365-day, 24/7 crypto convention (research-recomputed, Table 4.2).
- The evaluation is explicitly `a deliberately conservative payoff mapping` and `not intended to represent the true payoff of a Vega-weighted option position` (Section 3.8).

**Cost and fill census at Methods level (Sections 1 to 5, Appendices A.1 to A.5, ligature-normalised whole-text counts):** `fee 4` and `fees 1` all inside prose about managed funds or option-market friction, never a schedule; `transaction cost 16` / `transaction costs 13` all describing the flat 5 bps assumption and its robustness; `basis point 5` + `basis points 3` + `bps 0`; `slippage 0`, `bid-ask 1` (one qualitative sentence about wide bid-ask spreads in Section 5.5), `commission 0`, `maker 0`, `taker 0`, `market impact 0`, `impact 2` (both meaning feature impact, not price impact), `latency 0`, `turnover 0`, `borrow 0`, `liquidation 0`, `funding 3` (all generic literature prose about funding constraints, never a crypto funding rate), `margin 15` (all prose about option margin requirements, none modelled), `capacity 4` (all prose about volatility-selling capacity), `leverage 4` (all the equity *leverage effect*, never balance-sheet leverage), `fill 6` (forward-fill and `gaps that this study attempts to fill`, never an order fill), `spread 18` / `spreads 9` (all qualitative or statistical spreads, never a charged spread), `backtest 4` (all referring to the *future* Vega-weighted backtest the author recommends), and no reproducibility surface: `repository 0`, `github 1` (only the Binance API documentation URL), `code 3` (supply-schedule `fixed by code` and prose), `seed 0`, `reproduc 2`, `data availability 0`, `walk-forward 0`, `holdout 0`, `survivorship 0`, `point-in-time 0`, `bootstrap 0`, `benjamini 0`, `fdr 0`, `bonferroni 0`, `multiple testing 0`, `look-ahead 5` (as a bias the design claims to rule out), `p-value 0`, `standard error 0`, `confidence interval 0`, `t-statistic 1` (the unvalued Diebold-Mariano mention), `cagr 0`.
- Therefore: **no option fee schedule, no bid-ask or slippage model, no fill, queue, participation, latency or market-impact model, no funding or margin or collateral model, no capacity statement, and no statistical-inference machinery** anywhere in the pinned text. Every one of those fields is a `data gap`, never a zero-valued result.

**Assumptions we would have to add to make this tradable are all `research-proposed`:** contract selection (which strike and expiry), Vega scaling and its sign, delta hedging, option spread and fee schedule at the chosen venue, order type and fill model, position sizing, and signal-to-order delay.

## Evidence

### Source-reported

All figures below are third-party claims from the pinned PDF and have **not** been independently reproduced. Provenance is given for each block.

**Table 4.1 - Out-of-Sample Forecasting Performance (Section 4.2; test window `2024-09-21` to `2025-07-25`, approximately 308 daily observations; R-squared computed against the training-window constant mean).**

| Metric | XGBoost (Nonlinear) | AR(1)-GARCH(1,1) |
|---|---|---|
| Out-of-sample R2 | 0.0527 | -0.0107 |
| RMSE | 1.2943 | 1.3369 |
| MAE | 0.8976 | 0.9311 |

Research-recomputed from the printed cells: RMSE reduction `(1.3369 - 1.2943) / 1.3369 = 3.186%` and MAE reduction `(0.9311 - 0.8976) / 0.9311 = 3.598%`, matching the source's prose `approximately 3.2 percent` and `approximately 3.6 percent` (Section 4.2).

**Table 4.2 - Performance Comparison, IV Prediction Strategy vs Buy and Hold Bitcoin (Section 4.4; notes: Sharpe assumes a 2% annual risk-free rate, daily losses capped at -5%, win rate reflects that no active-signal day produces a positive *net* return after costs, profit factor undefined because gross profits are zero, Buy and Hold is close-to-close on Bitcoin spot over the same test window).**

| Metric | IV Prediction Strategy | Buy and Hold Bitcoin |
|---|---|---|
| Total Return | -1.18% | 85.66% |
| Annualised Return | -1.40% | 108.19% |
| Annualised Volatility | 0.25% | 45.85% |
| Sharpe Ratio | -13.40 | 1.78 |
| Maximum Drawdown | -1.18% | -28.10% |
| Calmar Ratio | -1.18 | 3.85 |
| Signal Active Ratio | 7.79% | N/A |
| Win Rate (Days) | 0.00% | N/A |
| Profit Factor | NaN | N/A |

Research-recomputed identities: active days `7.79% x 308 = 24.0`; cost bite `24.0 x 0.05% = 1.20%` of notional against a printed total of `-1.18%`, implying a gross contribution of about `+0.02%` before the flat cost; strategy Sharpe `(-1.40 - 2) / 0.25 = -13.6` against the printed `-13.40`; Calmar `-1.40 / -1.18 = 1.186` in magnitude against a printed `-1.18`, which equals the printed maximum drawdown; Buy-and-Hold Sharpe `(108.19 - 2) / 45.85 = 2.32` (log-return variant 1.56) against the printed `1.78` (see contradiction 2).

**Feature importance (Sections 4.3.1, 4.3.3, Figures 4.2 and 4.3 captions):** `price_change_1d` is the single most important feature with gain roughly twice the median of the top 20; `SOPR` ranks second, ahead of all macro and most realised-volatility variables; `Fed_Rate_mom` ranks third; `price_change_7d`, `vol_7d_rv` and `vol_30d_rv` sit in the upper tier; sentiment and Google Trends sit mid-tier; wavelet-derived features sit mid-to-lower tier. The top feature accounts for `about 8 percent of total gain` and the top five together `under 30 percent`.

**Descriptive statistics (Section 4.1):** DVOL full-sample range `approximately 35 to over 130 IV points`, mean `around 65`, standard deviation `around 17`, level autocorrelation `above 0.95`; the target change has mean `close to zero`, standard deviation `approximately 2.6 IV points`, autocorrelation `close to zero`; 30-day realised volatility `roughly 25% to over 90%`; the variance risk premium defined as DVOL minus subsequent 30-day realised volatility is `persistently positive` with sharp negative excursions; leverage asymmetry - average DVOL change conditional on a spot return below the fifth percentile `approximately +1.8 IV points`, above the ninety-fifth percentile `approximately -0.4 IV points`; SOPR daily values typically `0.98 to 1.02` in normal trading.

**Robustness, Section 4.6 (reported in summary form, no table, so these values have no printed table provenance and are `data gap` as to their exact derivation):** dropping the wavelet block gives out-of-sample R-squared in `0.045 to 0.050`; EGARCH(1,1) and GJR-GARCH(1,1) benchmarks produce figures `still slightly negative or close to zero`; costs swept `2 to 10 basis points` change the magnitude but not the sign, and at `zero transaction cost` the strategy is `small but still negative`; threshold sweep `0.1 to 0.4` standard deviations moves the active ratio from `approximately 25 percent` to `under 3 percent` with no configuration positive after costs; removing sentiment and Google Trends gives `approximately 0.045` against the `0.053` headline; a rolling `60 days` re-fit gives `approximately 0.048`; test-window halves give `0.041` (October 2024 to mid-February 2025) and `0.062` (mid-February to July 2025); a feature-permutation exercise reproduces the top-3 gain ranking as the top-3 R-squared declines.

**Hypothesis decisions (Sections 4.5.1 to 4.5.4):** H1 rejected in favour of the alternative (positive OOS R-squared for the nonlinear model, negative for the benchmark); H2 rejected in favour of the alternative (on-chain and macro variables materially contribute); H3 - `The null hypothesis is rejected, and the alternative is supported`, i.e. the strategy fails economically under this mapping; H4 reported only as `qualitatively consistent with the alternative` (see contradiction 5).

**Statistical-inference claim:** Section 3.9 states that `A formal Diebold-Mariano test on the squared forecast errors ... produces a t-statistic that supports rejection of the null of equal forecast accuracy at the conventional five percent level`. The t-statistic value, its standard error and its p-value are `not stated in source` (`t-statistic 1` occurrence, `p-value 0`, `standard error 0`, `confidence interval 0`). No interval, no stars and no multiplicity correction appear anywhere.

**Other source-reported design claims:** strictly chronological split with the test window sealed during training (Section 3.9); benchmark denied access to on-chain and sentiment variables by design (Section 3.9); wavelet-removal rerun `qualitatively similar` (Section 3.9); NUPL cross-checked against independent providers (Section 3.9).

### Independently reproduced

`not independently reproduced.`

Only arithmetic identities were checked against the printed cells, with no market data, no model fitting and no third-party code executed in this run:
- RMSE and MAE percentage reductions reproduce the printed `approximately 3.2` and `approximately 3.6 percent`.
- 365-day annualisation reproduces printed `-1.40%` and `108.19%` from printed `-1.18%` and `85.66%` over 308 test observations, identifying the annualisation convention.
- 1,225 + 308 = 1,533 against the printed `approximately 1,540` panel (7 observations unreconciled, contradiction 4).
- Active-day count 24.0, cost bite 1.20% of notional against printed total -1.18% (gross about +0.02%, research-computed).
- Strategy Sharpe identity holds approximately; Buy-and-Hold Sharpe identity does not reconcile under either standard convention (contradiction 2).
- Print-literal tracing of `0.0527` (5 occurrences), `1.2943`, `1.3369`, `0.8976`, `0.9311`, `108.19%`, `85.66%`, `7.79%`, `0.2510` (2), `0.0005` (2), `0.048`, `0.062`, `0.041`, `0.045`, `0.17292525837569978`, `Arun Jaitley` (2), `Anuj Pal`, `Turnitin`, `1,225`, `1,540`, `308`.

### Negative evidence

1. The economic result is negative on every printed metric: total return `-1.18%`, annualised `-1.40%`, Sharpe `-13.40`, Calmar `-1.18`, daily win rate `0.00%`, profit factor `NaN` (Table 4.2).
2. The linear benchmark is worse than a constant: out-of-sample R-squared `-0.0107` (Table 4.1), so the only positive result depends on one boosted-tree specification.
3. Explanatory power is small by construction: R-squared `0.0527` leaves about 95 percent of next-day DVOL-change variance unexplained, and Section 4.2 concedes predictions cluster near zero while actuals are far wider.
4. The model misses tails: Section 4.2 describes it as `more as a conditional-expectation estimator than as a tail-event detector`, which is precisely where the volatility risk premium lives.
5. The economic conclusion rests on a payoff the author calls deliberately wrong: spot-normalised IV-point PnL `does not capture any of that structure` of Vega (Section 3.8), so the printed loss is not evidence about a tradable option position.
6. At zero transaction cost the strategy is still `small but still negative` (Section 4.6), so the spot normalisation alone - not costs - mechanically suppresses the return series; the source's own attribution of the loss to costs is therefore only partly supported by its own zero-cost run.
7. No option-level execution is modelled at all: slippage 0, commission 0, maker 0, taker 0, market impact 0, latency 0, turnover 0, bid-ask charged 0 (census above).
8. No inference machinery: p-value 0, standard error 0, confidence interval 0, bootstrap 0, no stars, and the single Diebold-Mariano reference carries no statistic.
9. No multiplicity control despite a 37-feature panel, an Optuna hyperparameter search and eight robustness reruns: benjamini 0, fdr 0, bonferroni 0, multiple testing 0; the Optuna trial count is `not stated in source`.
10. Threshold provenance is contaminated as written: Section 3.8 says the threshold is `set in the test period`, which would be tuning inside the held-out window (contradiction 1).
11. The test window is a single roughly ten-month path with no deep bear market (Sections 1.6, 5.7), and it overlaps a strong Bitcoin rally, which is why the Buy and Hold reference compounds to `108.19%`.
12. Regime split evidence is thin: sub-half R-squared `0.041` and `0.062`, rolling re-fit `0.048`, wavelet-free `0.045 to 0.050` - all from prose, none tabulated.
13. Feature concentration is low and fragile in the other direction: top feature `about 8 percent` of gain, top five `under 30 percent`, so the signal is a bundle of weak contributions whose stability the author labels `a conjecture rather than a tested claim` (Section 4.3.3).
14. Attribution is associative, not causal: SHAP and gain `describe associations conditional on the trained model; they do not identify structural mechanisms` (Section 1.6).
15. Provider and construction gaps block exact replication: SOPR reconstruction source `not stated in source`; the sentiment model, corpus and platform `not stated in source`; miner address tagging is heuristic (Sections 3.2, 3.9, A.1.4).
16. No artefact exists: `repository 0`, `github 1` (a Binance documentation URL), `code 3` (prose), `seed 0`, `data availability 0`, `reproduc 2`, no repository, no commit, no environment, no data snapshot.
17. The source is an unreviewed master's dissertation posted to SSRN with `0 References / 0 Citations` metadata and no peer-review statement; it is not evidence of a validated result.
18. The panel cannot be reconstructed from the source alone: the `Data Sources and Software` block gives endpoint URLs and single access dates (Binance docs 28 August 2025, CoinMetrics 27 August 2025, Deribit DVOL 10 October 2025, FRED 28 August 2025, Google Cloud BigQuery 3 September 2025, Google Trends 30 August 2025) with no data snapshot, query, version or schema, while the sample itself stops `2025-07-25`, about fourteen months before `source_as_of`.
19. The Buy and Hold comparator is not a like-for-like benchmark and the source says so: it `is not what the strategy is being designed to beat` and is included `solely to provide context` (Sections 3.8, 4.4), yet it is the row that carries `108.19%` and `1.78`.
20. The printed Buy and Hold Sharpe does not reconcile with its own row (contradiction 2), and the printed Calmar `-1.18` equals the printed maximum drawdown rather than the ratio -1.40/1.18.
21. Panel arithmetic does not close (contradiction 4).
22. H4 is declared supported without a test (contradiction 5).
23. H3 is stated as rejecting a null whose alternative is the observed failure, so the framing reverses the usual evidential direction; the practical content is a null economic result.
24. The loss cap at `-5%` truncates the distribution used for every risk statistic, and the profit-factor cell is `NaN`, so the return distribution is not fully described.
25. Prior literature already reports that daily machine-learning volatility gains are `modest in absolute terms` and the source itself says an OOS R-squared of `0.05` `should not be expected to deliver large alpha after costs` (Section 2.4.4), i.e. the negative economic outcome is anticipated by the framing rather than discovered.

## Falsification plan

All thresholds below are `research-defined falsification threshold` unless explicitly marked `research-proposed`, and every operational choice not stated by the source is marked `research-proposed`. A single `no-retuning` rule applies to the whole plan.

**No-retuning rule (binding, `research-defined`):** freeze the source's design exactly as pinned - daily UTC-close sampling, the sample window `2021-05-12` to `2025-07-25`, the 80/20 chronological split at `2024-09-20` / `2024-09-21`, the 37-feature set after the 0.9 correlation filter, the listed feature families and their windows (7d/30d RV annualised by sqrt(365), 1d/7d/30d price changes, 30-day macro momentum, s7/s14/s30 wavelets), the XGBoost hyperparameters exactly as printed in Appendix A.2, the Optuna expanding-origin 90-day validation scheme, the AR(1)-GARCH(1,1) benchmark, the target `iv_(t+1) - iv_t`, the active-signal threshold semantics, the flat 5 bps active-day cost, the -5% daily loss cap, the 2% risk-free rate, the 365-day annualisation, and every threshold stated below. Failing gates must be reported as failures; a rerun that changes any frozen element and then passes does not clear the gate.

- **F1 - Print-literal reproduction.** *Threshold (`research-defined`):* every value in Table 4.1 and Table 4.2, the Appendix A.2 hyperparameters, the three sample dates, the 37-feature count and the `0.2510` threshold appear verbatim in the pinned text. *Action:* on any miss, withdraw the record's numbers and re-pin the source.
- **F2 - Provenance integrity.** *Threshold (`research-defined`):* all three digests above (72,179 / 852,159 / 143,723 bytes and their SHA-256 values) recompute exactly from the pinned artefacts. *Action:* on mismatch, treat the source version as changed, re-read and re-verify or fail closed.
- **F3 - Statistical predictability replication.** *Threshold (`research-defined`):* re-running the pinned pipeline on the pinned split yields out-of-sample R-squared >= `0.0527` for XGBoost and <= `-0.0107` for AR(1)-GARCH(1,1), with RMSE `1.2943` and MAE `0.8976` within `0.005` absolute. *Action:* below threshold, classify the predictability claim as not reproduced and stop treating H1 as settled.
- **F4 - Benchmark-adequacy gate.** *Threshold (`research-defined`):* at least one additional linear baseline (EGARCH(1,1), GJR-GARCH(1,1) or a HAR-type realised-volatility regression, `research-proposed` choice) must be beaten on the same window; the source reports these only as `slightly negative or close to zero` in prose. *Action:* if any tuned linear baseline matches or beats XGBoost, record the nonlinear gain as specification-dependent.
- **F5 - Diebold-Mariano disclosure gate.** *Threshold (`research-defined`):* the squared-error DM statistic must be reported with its value, standard error and two-sided p-value, and must reject equal accuracy at 5 percent. *Action:* if the source cannot supply the number and our recomputation does not reject, mark Section 3.9's claim unsupported.
- **F6 - Threshold-provenance gate.** *Threshold (`research-defined`):* the `0.2510` threshold must be selected using training-window or validation data only, with its unit stated as IV points or as standard deviations of the predicted distribution. *Action:* if the threshold was chosen in the test window or its unit cannot be established, the economic row of Table 4.2 is invalidated and H3 must be re-run on a fresh sealed window.
- **F7 - Gross-to-net sign gate under the source's own mapping.** *Threshold (`research-defined`):* recomputed total return must equal `-1.18%` within `0.05` percentage points and the implied gross contribution must be about `+0.02%` given 24.0 active days at 5 bps. *Action:* if the gross leg is materially negative rather than approximately zero, the source's `cost-dominated` attribution (H4) fails on its own terms.
- **F8 - Vega-consistent payoff gate (`research-proposed`).** *Threshold (`research-defined`):* re-map the identical predictions into a specified option position - for example a delta-hedged at-the-money straddle position sized to unit Vega for one day (`research-proposed` construction, contract, strike rule, delta-hedge cadence and rebalance price all `research-proposed`) - and charge observed bid-ask, exchange fees and hedge slippage from the chosen venue. *Action:* if net Sharpe over the pinned test window is <= `0.00`, record that the predictability claim does not monetise under any tested mapping; if it is > `0.00`, record the source's economic conclusion as mapping-dependent and keep the claim at `research-only`.
- **F9 - Cost ladder.** *Threshold (`research-defined`):* sweep `0 / 2 / 5 / 10 / 20` bps per active day (`research-proposed` ladder extension to 20 bps) under both the spot-normalised and the Vega-consistent mapping. *Action:* report the exact cost at which the sign flips under each mapping; no single favourable cost point may be reported in isolation.
- **F10 - Placebo and permutation gate.** *Threshold (`research-defined`):* 1,000 circular-shift or 24-hour-block-shuffle permutations of the target against the fixed feature set must leave real-model out-of-sample R-squared above the 95th percentile of the placebo distribution. *Action:* below the 95th percentile, reclassify the predictability as indistinguishable from in-sample structure.
- **F11 - Multiple-testing gate.** *Threshold (`research-defined`):* with 37 features, an Optuna search of unknown trial count and eight robustness reruns, apply Benjamini-Hochberg at `q < 0.10` across every reported model variant (`research-proposed` family definition). *Action:* if the headline R-squared does not survive, label the result exploratory.
- **F12 - Sub-period and forward-window stability.** *Threshold (`research-defined`):* positive out-of-sample R-squared in both printed test halves (`0.041` and `0.062` reproduced), in the rolling 60-day re-fit (`0.048` reproduced), and in a frozen forward window `2025-07-26` to `2026-09-30` that the source never saw (`research-proposed` extension). *Action:* any non-positive window downgrades the claim to regime-specific.
- **F13 - Provider-reconstruction gate.** *Threshold (`research-defined`):* SOPR, NUPL, sentiment and miner-outflow series must be rebuilt from at least two independently sourced reconstructions each, with the two versions correlating at `>= 0.95` over the pinned window. *Action:* lower agreement makes the panel a `data gap` and stops replication until resolved.
- **F14 - Artefact gate.** *Threshold (`research-defined`):* pinned source must expose code, data snapshot or an environment lockfile sufficient to rerun Tables 4.1 and 4.2. *Action:* with `repository 0`, `seed 0` and `data availability 0` currently failing this gate, no adoption-scope change may be proposed until an artefact exists.
- **F15 - Boundary gate.** *Threshold (`research-defined`):* no sizing, venue, latency, capacity or deployment statement may be made while F6, F8 and F14 are failing. *Action:* any such statement is out of scope for this record and must be removed.

## Crypto portability

`direct` for the mechanism as studied, `adapted` for any implementation.

- The source is crypto-native end to end: Bitcoin spot from Binance, the Deribit DVOL index as target, public-ledger on-chain features, a 24/7 daily calendar annualised by `sqrt(365)`. There is no traditional-asset mechanism being ported, so no `adapted` label is needed for the *hypothesis*.
- Implementing it, however, requires instruments the source never touches: Deribit option contracts, their bid-ask, fees, Vega, delta and margin. That layer - including funding on any perpetual hedge, mark-versus-index divergence, liquidation and leverage behaviour - is `adapted` and entirely `data gap` here.
- Venue and index caveats: DVOL is a single-venue index; the spot leg is a single venue; cross-venue option flow, venue market share after 2025 and DVOL methodology revisions are `not stated in source`.
- Timestamp caveat: daily UTC close alignment means candle boundaries differ from any venue's session convention; intraday dynamics are excluded by design (Section 5.7).
- Staleness caveat: the pinned sample ends `2025-07-25`; any 2026 claim about the same effect is `unproven` until F12's forward window is run.

## Limitations

- `not independently reproduced` - only arithmetic identities were checked; no data was downloaded, no model was fitted, no third-party code was executed.
- `underspecified`: signal-to-order timing, position direction statement, contract, strike, expiry, hedge, sizing, exit, re-entry, overlap handling, Optuna search space and trial count, random seeds, threshold unit, annualisation statement (it is inferable but never printed as a convention).
- `data gap`: SOPR provider and heuristics, sentiment model and corpus, missing-data policy beyond default-direction splits, out-of-order and stale-row handling, any option fee, spread, slippage, fill, latency, funding, margin, impact or capacity model, Diebold-Mariano statistic, all p-values and intervals, robustness tables (Section 4.6 is prose only), code, data snapshot, environment and seed.
- `not stated in source`: publication or peer-review status beyond the SSRN license cell, competing-interest or funding declarations (none found; `competing 1` is the single word inside `competing interest`-free prose context in the bibliography scan and carries no declaration), ORCID, data-availability statement.
- Source-quality limit: an unreviewed master's dissertation from a single author with `0 References / 0 Citations` on the platform; its own literature claims are relayed, not independently checked here.
- Sample limit: one asset, one index, one venue per leg, daily frequency, ten-month sealed test path containing a bull phase, sample ends `2025-07-25`.
- Identification limit: predictive, not causal; feature attribution is associative.
- Inference limit: no significance machinery, no multiplicity control, unknown hyperparameter trial count.
- Economic limit: the printed economic result is a property of a mapping the author calls deliberately conservative; it is evidence about the mapping, and only weak evidence about tradability.
- Incremental-value limit relative to existing records: the record's distinctive content is the *on-chain-plus-macro state set applied to the DVOL change target* and the *gross-to-net divergence under two different payoff mappings*; the direction DVOL-shock-to-spot, option-VRP harvesting and option-IV term-structure regime filtering are already captured elsewhere (see Related Wiki records).

## Implementation status

`implementation_status: not-implemented`. Nothing has been implemented in any research stack: no panel was rebuilt, no XGBoost or GARCH model was fitted, no strategy was coded, no backtest was run, no market data was downloaded, and no dependency was installed. No Qlib full-backtest validation, no Paper, no Testnet and no Live verification occurred or is implied. The falsification gates above are a plan, not results.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. This record's presence in the staging repository does not mean: passed Research Intake Review, entered Hermes Wiki Brain, entered the production candidate pool, completed Qlib full-backtest validation, became a frozen survivor or leaderboard entry, profitable, validated alpha, approved for implementation, approved for paper trading, approved for testnet, or approved for live trading. Nothing here authorises deployment, sizing, venue selection or capital allocation.

## Related Wiki records

- [[quant/crypto-options-dvol-iv-premium-shock-spot-predictor-2026-09-13]] - same index family, opposite direction: DVOL level shocks used as a short-horizon *spot* predictor from a GitHub signal implementation, whereas this record forecasts the DVOL change itself from on-chain and macro state with no spot-direction claim.
- [[quant/crypto-volatility-risk-premium-variance-swap-estimator-fragility-decay-2026-09-12]] - concerns harvesting the variance risk premium with implied-versus-realised variance estimators; this record never harvests a premium and never uses realised-versus-implied spread, it predicts the next-day index change and reports a failed monetisation under a spot-normalised payoff.
- [[quant/crypto-kalshi-prediction-market-macro-repricing-volatility-forecasting-2026-09-01]] - also a crypto volatility *forecasting* record, but the information set is prediction-market repricing and the target is realised volatility; this record's information set is price, on-chain, macro and sentiment state and the target is the implied-volatility index change.

No other Wiki Brain page was found on read-only search for DVOL-implied-volatility forecasting, on-chain SOPR/NUPL signal pages or this source identity, and zero Wiki pages were written in this run.

## Sources

- https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7073558
- https://papers.ssrn.com/sol3/Delivery.cfm/7073558.pdf?abstractid=7073558&mirid=1&type=2
- https://doi.org/10.2139/ssrn.7073558
