---
schema: strategy-research-record-v1
title: "End-to-End Actor-Critic Trading vs LSTM Forecast-Then-Rule on 20 Mega-Cap S&P 500 Stocks, Evaluated Under Forward Retraining (2019-2020 Backtest)"
created: 2026-09-30
updated: 2026-09-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - reinforcement-learning
  - actor-critic
  - deep-rl
  - lstm
  - technical-indicators
  - us-equities
  - sp500
  - walk-forward
  - backtest-benchmark
status: research-only
confidence: medium
source_as_of: 2026-09-25
sources:
  - "https://arxiv.org/abs/2609.31870"
  - "https://arxiv.org/pdf/2609.31870"
  - "https://doi.org/10.48550/arXiv.2609.31870"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# End-to-End Actor-Critic Trading vs LSTM Forecast-Then-Rule on 20 Mega-Cap S&P 500 Stocks, Evaluated Under Forward Retraining (2019-2020 Backtest)

## Provenance

- **Paper:** Bicheng Wang, Xinyi Zhang, "Deep Reinforcement Learning for Equity Trading: Benchmarking Actor-Critic Methods with Forward Retraining."
- **Author list (exactly as printed on page 1 and in the PDF `/Author` metadata):** `Bicheng Wang; Xinyi Zhang`. Two authors, identical ordering in the landing-page `citation_author` meta tags (`Wang, Bicheng` then `Zhang, Xinyi`), the page-1 title block and the PDF `/Author` field.
- **Affiliations / contact (page 1):** both authors printed as `Stanford University`, with `bichengw@stanford.edu` and `xyzh@stanford.edu`.
- **Manuscript dateline (page 1):** `June 8, 2021`, i.e. the manuscript content carries a 2021 dateline while the arXiv posting is 2026-09-25; the acknowledgments state the work was carried out under the guidance of Ayush Kanodia and thank Huizi Mao, Andrew Ng and Kian Katanforoosh, "the instructors of Stanford CS230, whose course informed our choices of LSTM hyperparameters, loss functions and their derivatives, evaluation metrics and reinforcement learning methods." The empirical sample ends in 2020 (see below), so no evidence in this paper postdates calendar 2020.
- **Preprint:** arXiv:2609.31870v1 [cs.LG]; landing submission history shows exactly one version, `[v1] Fri, 25 Sep 2026 18:10:14 UTC (16 KB)`, with the submitting-account display name printed as `Bichng Wang` (arXiv account spelling; not a third author). The arXiv API returns a single `<entry>` with `published` = `2026-09-25T18:10:14Z` and `updated` = `2026-09-30T08:29:19Z`; because the landing page lists only `[v1]` and no `[v2]`, that later `updated` value is an API/feed metadata refresh rather than a new version, and `totalResults` = 1.
- **Subjects:** primary Machine Learning `cs.LG`, cross-lists Artificial Intelligence `cs.AI`, Computational Engineering, Finance, and Science `cs.CE`, Multiagent Systems `cs.MA`.
- **Comments field:** absent - the landing metatable has no `Comments` row and the API returns no `arxiv:comment`.
- **Journal reference:** absent - no `Journal reference` row on the landing page and no `arxiv:journal_ref` in the API.
- **Publication status:** **preprint only.** The word `peer` appears 0 times in the pinned PDF text and there is no peer-review or acceptance statement. The only DOI is the arXiv-issued DataCite value `10.48550/arXiv.2609.31870`, whose landing tooltip reads `arXiv-issued DOI via DataCite (pending registration)`; the API returns no `arxiv:doi`.
- **Licence:** the arXiv **non-exclusive distribution licence 1.0** (landing licence link and PDF `/License` field both carry that identifier) - this is *not* a Creative Commons reuse licence.
- **Stable URLs:** abstract `https://arxiv.org/abs/2609.31870`; PDF `https://arxiv.org/pdf/2609.31870`; DOI `https://doi.org/10.48550/arXiv.2609.31870`; API `https://export.arxiv.org/api/query?id_list=2609.31870`.
- **Primary-source checksum (fetched 2026-09-30):**
  - PDF: **165,275 bytes**, SHA-256 `97a2f345d9158f5cdc10e5f0739ab5d8027a02777c2cbd302d33adb5b4b229dc`, extracted with pypdf 6.16.2 into **8 pages / 26,981 characters / 369 lines**, read end to end covering the Abstract, Sections 1-6, Table 1 (raw-data sample), Table 2 (processed-data sample), Table 3 (LSTM training/validation metrics, every printed cell), Table 4 (backtest performance, every printed cell), the Figure 1 overview caption, the Author Contributions and Acknowledgments blocks, and the 23-item reference list. PDF `/Title` is byte-identical to the printed title, `/Author` = `Bicheng Wang; Xinyi Zhang`, `/arXivID` = `https://arxiv.org/abs/2609.31870v1`.
  - Landing page: **42,935 bytes**, SHA-256 `205721be80b5b10611b8d46675e7141dda413c8eaaa2b312546c7a5a6f2c53b8` - used for the two `citation_author` tags, `citation_date 2026/09/25`, the absence of Comments and Journal-reference rows, the four Subjects, the DataCite tooltip, the licence identifier and the single `[v1]` submission-history line.
  - API: **3,024 bytes**, SHA-256 `326204bdc22bc5b81480db738cd6fdff51b36a89eafbc0ba17473d77f5fbaadb` - single entry, `published 2026-09-25T18:10:14Z`, `updated 2026-09-30T08:29:19Z`, no `comment`, no `journal_ref`, no `doi`, two `<name>` authors, four categories.
  - **Text-layer caveats recorded, not reconciled:** (a) PDF bold is lost on extraction, so the "best value in each metric column in bold" markings of Tables 3 and 4 are **not recoverable** - this record therefore cites raw cell values and separately reports research-computed column minima; (b) negative numbers extract with a Unicode minus and were normalised to ASCII for token checks; (c) all 69 numeric tokens of Table 4 and all 56 numeric tokens of Table 3 were located verbatim in the pinned text.
- **Data as-of:** daily OHLCV plus day-of-week for **20 large-capitalisation S&P 500 constituents, 2000-2020**, "obtained from the Yahoo Finance API" (Section 3; no vendor URL, no ticker list, no membership date given); 105,680 rows "in total (20 stocks x 5,284 trading days)"; chronological split **train 2000-2018, test 2019-2020, "approximately a 90/10 split."** Universe construction: "the 20 stocks with the largest market capitalization among S&P 500 constituents", restricted to companies with complete 2000-2020 histories because "long, complete historical records are limited", with "companies that went public after 2000 ... excluded so that every stock has complete data over the entire period."
- **Cost/slippage treatment - determined at Methods level**, by reading Section 3 (Dataset and Features, including 3.1 indicators and 3.2 logarithmic scaling), Section 4 (Methods, including 4.1 LSTM forecasting, 4.1.3 trading strategy, 4.2 DRL with 4.2.1 model definition, 4.2.2 algorithms, 4.2.3 forward retraining), Section 5 (Results, 5.1 metrics, 5.2 discussion) and Section 6 (Conclusion, Limitations, Author Contributions, Acknowledgments), **plus a whole-document word census of the pinned 26,981-character text layer**: `transaction cost` 0, `transaction costs` 0, `costs` 0, `slippage` 0, `commission` 0, `bid-ask` 0, `spread` 0, standalone `fee`/`fees` 0, `funding` 0, `borrow` 0, `turnover` 0, `capacity` 0, `market impact` 0, `impact` 0, `latency` 0, `order type` 0, `limit order` 0, `market order` 0, `maker` 0, `taker` 0, `participation` 0, `margin` 0, `fill` 0, `transaction` 0, `rebalanc` 0, `execution` 0. The token `cost` appears **exactly once**, only as "increased computational cost without improving the metrics" about LSTM regularisation (Section 4.1.2). `leverage` 5 and `leveraged` 4 occurrences all describe the LSTM position multiplier of Section 4.1.3 / Table 4 / Section 5.2 with **no financing cost attached anywhere**. **There is therefore no transaction-cost, spread, fill, latency, leverage-cost or market-impact model anywhere in the paper - every one of those fields is a data gap and must never be read as zero, and all printed returns must be treated as gross of unspecified trading frictions with even the gross-vs-net label absent from the source.**
- **Statistical machinery census (same text layer):** `p-value` 0, `t-stat` 0, `confidence interval` 0, `bootstrap` 0, `significan` 1 (the prose phrase "a significant advantage" in Section 5.2, with no test behind it), `benjamini` 0, `bonferroni` 0, `holm` 0, `fdr` 0, `multiple test` 0, `seed` 2 / `seeds` 2 (both inside the Limitations: "we do not report variability across runs" and "Future work ... multiple random seeds"), `walk-forward` 2 (the Section 4.2.3 protocol and the future-work sentence), `holdout` 0, `out-of-sample` 1 (Introduction), `baseline` 7 (every occurrence means either "the supervised price-forecasting baseline", the `Baseline` model row of Table 3, or reference material), `naive` 0, `persistence` 0, `climatolog` 0, `buy-and-hold` 1 (Section 4.1.3, describing the LSTM rule itself as "a simple modified buy-and-hold strategy", i.e. a conditional long-or-cash rule) - **Table 4 therefore carries no trivial benchmark of any kind**: no unconditional buy-and-hold row, no equal-weight basket row, and the S&P 500 index's own return is never printed. `annualized`/`annualised` 0, `cagr` 0, `win rate` 0, `pnl` 0, `roi` 0, `survivorship` 1 (Limitations), `repository` 1 and `github` 2 (both inside reference [18], the cited Stable-Baselines3 library), `source code` 0, `data availability` 0, `acknowledg` 1 (Section 6), `orcid` 0, `conflict` 0, `crypto` 0, `bitcoin` 0, `perpetual` 0, `peer` 0.
- **Source-identity deduplication (2026-09-30, hidden-inclusive ripgrep across the entire checkout including `.git`, `.mimo-worktrees`, `.agents`, `.hermes` and `coverage_manifest.csv`):** `2609.31870` 0 files, `10.48550/arXiv.2609.31870` 0, exact title fragment `Benchmarking Actor-Critic Methods with Forward Retraining` 0, `Deep Reinforcement Learning for Equity Trading` 0, `Bicheng Wang` 0, manifest hits for `31870` and `forward retraining` 0. Adjacent-token probes: `Xinyi Zhang` 3 files (one record - `pure-momentum-wild-bootstrap-drift-significance-filter-us-equities-2026-09-26`, a different source identity, Amundi Working Paper 188 "Pure Momentum Strategies", whose three authors include Xinyi Zhang - plus two `.git` log files); `forward retraining` 3 files (`archetype-trader-vq-rl-hierarchical-crypto-perpetual-2026-09-13` plus its two `.mimo-worktrees` copies, where the matching phrase is "walk-forward retraining" in a falsification section); `Stable-Baselines3` 9 files (3 distinct records outside the worktrees, all different sources that cite the same library). Positive control `novy-marx` = 47 files case-sensitive and 56 case-insensitive. `git log --oneline -20` was used as a convenience glance only, not as dedup.

## Economic mechanism

### Source-reported

The paper's claim is a **methodological comparison of two decision pipelines plus a robustness protocol**, not a documented premium (Abstract, Sections 1 and 5):

- Abstract: "Consistently profitable trading is difficult because equity markets are noisy, non-stationary, and only partially predictable from historical data."
- Section 1 / Figure 1: two approaches. The **indirect** approach "uses time-series forecasting: an LSTM network predicts the market price, and a basic trading strategy acts on the prediction"; the **direct** approach "uses deep reinforcement learning: an agent observes the market and outputs trading actions end to end to build the portfolio."
- Section 4.1.1 rationale for the loss: "The choice of loss function and evaluation metric strongly influences what a model ultimately optimizes, and for stock price prediction the appropriate loss differs from that of a generic regression problem" - MSE on price levels weights a $20 move on a $20 stock 40,000 times more heavily than a $0.10 move on a $1 stock, so "MSE therefore underweights low-price periods and produces an unbalanced fit"; MAPE is chosen because it "better captures the relationship between predicted and actual prices over long periods in which price levels change substantially."
- Section 4.2.1 (the DRL formulation): the reward "is the change in portfolio value when action `a` is taken in state `s`, leading to the new state `s'`", `r(s,a,s') = v' - v` (Eq. 5); the agent observes "available cash balance, closing prices, the number of shares held of each stock, and the technical indicators."
- Section 4.2.3 (the robustness claim): "In forward retraining, the test period is divided into consecutive time slices; before each slice, the agent is retrained on all historical data available up to that point and then trades during that slice. This is a walk-forward scheme with an expanding training window: the model never sees data from the slice it trades."
- Section 5.2 (why retraining matters): "DDPG sometimes performed very well but was frequently brittle with respect to hyperparameters and other tuning choices, which caused instability" (Section 4.2.2); "In our experience, DDPG is difficult to tune to a suitable configuration for every retraining window, which may explain the gap between the individually tuned, once-trained DDPG and its retrained counterpart"; "TD3 substantially stabilized training in our experiments, making results far less dependent on hyperparameters and tuning, which is a significant advantage in a market that is hard to predict."
- Section 6 (the authors' own framing of the result): "the DRL agents achieved the highest returns, led by DDPG with a 55.51% annual return; the LSTM strategy offered the smallest drawdown and market exposure; and TD3 combined strong risk-adjusted performance with stability across training strategies."

### Research interpretation

Two separable, falsifiable hypotheses are implicit in the paper and are the alpha claim worth testing:

- **H1 (decision-policy alpha):** an end-to-end actor-critic policy driven by OHLCV plus trend indicators extracts daily large-cap US equity return that a supervised "predict-then-trade" rule does not, *after* costs and after removing market beta.
- **H2 (protocol claim):** the ranking of candidate trading policies is materially changed by an expanding-window walk-forward retraining protocol, so a once-trained backtest is not trustworthy evidence of algorithm quality. The source's own Table 4 supports H2 only partly (A2C, PPO, SAC improve; TD3 unchanged; DDPG loses 46.3% relative), which is itself the interesting, testable content.

Component roles (the source supplies the first three; nothing here is a documented premium):

```text
Regime: none required by the source. Research-proposed (optional) cash/drawdown gate - not in the source.
Primary signal (indirect pipeline): LSTM point forecast of next-day price; position w_t = lambda * 1[p_hat(t+1) >= p_t] (Eq. 4).
Primary signal (direct pipeline): the learned actor-critic policy itself, mapping [cash, prices, holdings, 14 indicator columns] to an integer share-count action in {-k, ..., k}.
Confirmation / risk: none in the source - no stop, no drawdown control, no exposure limit, no cost term in the reward (Eq. 5).
Robustness protocol: forward retraining (Section 4.2.3), the paper's actual contribution.
Decision layer (research-proposed, NOT source-reported): daily position change charged a cost ladder, benchmarked against buy-and-hold of the same basket.
```

The alpha statement under test is narrow: *does a learned daily long/cash policy on 20 mega-cap US stocks beat (a) its own always-long basket, (b) the S&P 500, and (c) the trivial forecast-then-trade rule, on a net, point-in-time, multiple-seed basis?* The source does not answer (a) at all, never prints the index return for (b), charges zero costs for all three, and reports no seed variability - so every performance figure below is a gross, single-run, survivorship-selected number.

## Signal

All items are **source-reported** unless explicitly marked research-proposed / research-defined / `underspecified` / `data gap`.

- **Formation timestamp:** `not stated in source`. The paper never states when on a trading day the state is observed, whether a decision is made before or after the close, or at which price an action is executed. `data gap`.
- **Raw inputs (Section 3):** per record - date, open, high, low, close, trading volume, ticker symbol, day of the week; "Raw data are obtained from the Yahoo Finance API"; missing data are checked ("We first check for missing data") but no missing-data rule is printed (`underspecified`).
- **Technical indicators (Section 3.1):** seven trend-following indicators added - MACD, RSI, Bollinger bands (BOLL), commodity channel index (CCI), directional movement index (DX), simple moving average (SMA), exponential moving average (EMA), "several of them computed over multiple look-back windows (see Section 4.2.1 for the full list)."
- **State vector (Section 4.2.1):** `s = [b, p, h, x]` where `b` = available cash balance, `p` = closing prices, `h` = shares held of each stock, and `x` = the indicator list printed in full: `macd`, `boll_ub`, `boll_lb`, `rsi_10`, `rsi_20`, `cci_10`, `cci_20`, `dx_30`, `close_20_sma`, `close_60_sma`, `close_120_sma`, `close_20_ema`, `close_60_ema`, `close_120_ema` (numeric suffix = look-back window in trading days). Table 2 shows the processed frame carrying `macd`, `boll_ub`, `cci_10`, `dx_30`, `close_120_sma`, `close_120_ema` plus a `Day` column (printed as 0 for the first trading day, 2000-01-03, a Monday; the day-of-week encoding convention is not stated - `underspecified`).
- **Feature transform (Section 3.2, Eq. 1):** log min-max scaling `x_tilde = (log x - min(log x)) / (max(log x) - min(log x))` applied to price-level features such as the price itself, SMAs and EMAs. **`data gap`: the window over which `min`/`max` are taken is never stated** - if it spans 2000-2020 the transform leaks test-window extrema into training features.
- **Warm-up (research-computed observation on Tables 1-2):** on the first trading day Table 2 prints `macd` 0, `boll_ub` 0.9256, `cci_10` -66.67, `dx_30` 100 identically for all five sample tickers and `close_120_sma = close_120_ema = close` (0.859 / 16.274 / 89.375 / 13.952 / 35.299, matching Table 1's Close column to three decimals), i.e. the 120-day windows contain a single observation. **The source states no warm-up or row-discard rule** (`underspecified`).
- **LSTM forecaster (Section 4.1.2):** "A two-layer LSTM followed by a single dense layer yielded the most stable predictive model"; compared variants are bidirectional LSTMs, stacked LSTMs and LSTMs with multiple dense layers; dropout / added regularisation "increased computational cost without improving the metrics (Table 3)"; three training regimes are compared - train on all stocks (chosen), train on a single stock, and train on all then fine-tune. Loss candidates: MSE, MAPE, MSLE, Huber, log-cosh, with MAPE selected (Eq. 2 and its derivative Eq. 3). Exact unit counts, learning rate, batch size, epochs and validation split are `not stated in source` except through the Table 3 row labels `Fewer units` / `More units` (which print no numbers).
- **Indirect trading rule (Section 4.1.3, Eq. 4):** `w_t = lambda * 1[p_hat(t+1) >= p_t]` - "If the predicted price is lower than the current price, the strategy holds cash; if it is higher than or equal to the current price, it buys shares and holds them"; `lambda = 1` unleveraged, `lambda > 1` leveraged. **The leveraged `lambda` value is never printed** (`data gap`); research-computed from Table 4 it is approximately 2 (see Evidence).
- **DRL action space (Section 4.2.1):** `a in {-k, ..., -1, 0, 1, ..., k}` where `k` is "the maximum number of shares per trade" (example given: `a = 10` = buy 10 shares). **`k` is never stated** (`data gap`), so position scale, capital base and cash constraint are unrecoverable.
- **DRL reward (Eq. 5):** `r = v' - v`, change in total portfolio value - **gross of any cost, because no cost term exists**.
- **Algorithms (Section 4.2.2):** PPO (clipped surrogate), A2C (synchronous A3C), DDPG (off-policy, deterministic policy, "Our DDPG implementation builds on Stable-Baselines3"), TD3 (clipped double-Q, delayed policy updates, target policy smoothing), SAC (entropy-regularised). **No hyperparameter table of any kind is printed** - no learning rates, discount factors, network sizes, replay sizes, exploration noise, update counts, batch sizes or tuning procedure; Section 5.2 refers only to "the individually tuned, once-trained DDPG" without stating the tuning data set (`underspecified`, and see Negative evidence 9 and gate F3).
- **Forward retraining (Section 4.2.3):** test period split into "consecutive time slices", expanding training window, no training on the traded slice. **Number, length and boundaries of the slices are not stated** (`underspecified`), so the retrained rows cannot be reproduced.
- **Entry / exit / holding period / re-entry / sizing:** for the LSTM pipeline these are Eq. 4 (all-in or all-cash per stock, no explicit exit other than the forecast flipping sign, no stated holding-period cap, no sizing beyond `lambda`); for the DRL pipeline they are *implicit in the learned policy* and therefore `underspecified` from the paper alone.
- **Evaluation window and benchmark:** test set 2019-2020, benchmark = the S&P 500 index (Table 4 caption); metrics = annual return, cumulative return, Sharpe ratio, maximum drawdown, alpha and beta (Section 5.1), with alpha/beta "the intercept and slope of a regression of strategy returns on benchmark returns." **Sharpe convention (risk-free rate, return frequency, annualisation) is not stated**; regression frequency is not stated; the index's own return is not printed.
- *Research-proposed operationalization (not source-reported), offered only so the hypothesis is testable:* observe the 14-column state at the daily close, emit the policy's share-count action, fill at the next trading day's open (research-proposed because the source states no execution timing), charge a research-defined per-side cost ladder, hold until the next decision, and compare net of costs against (a) always-long the same 20-stock equal-weight basket, (b) the S&P 500 total-return series, and (c) the Eq. 4 LSTM rule. **All thresholds, fill rules, cost levels and benchmark choices in this paragraph are research-proposed/research-defined and have no source support.**

## Required data

- **Instrument / universe:** 20 large-capitalisation S&P 500 constituents selected by largest market capitalisation among constituents, restricted to names with complete 2000-2020 histories; the exact ticker list and the membership/selection date are `not stated in source`.
- **Venue / market type:** US listed cash equities (Yahoo Finance as the data source); no futures, options, derivatives or crypto (`crypto`, `bitcoin`, `perpetual` all 0 occurrences).
- **Timeframe:** daily bars, 5,284 trading days, 2000-2020; decision cadence daily (implied by the state and rule); test window 2019-2020.
- **Fields:** date, open, high, low, close, volume, ticker, day of the week (Section 3); derived features per Section 3.1/3.2 and the 14-column list of Section 4.2.1; portfolio fields `b` (cash), `h` (holdings) in the DRL state.
- **Adjustment policy:** Table 1's caption states "Close is the split- and dividend-adjusted closing price, which is why it can lie outside the unadjusted low-high range", so the printed raw record mixes an adjusted Close with an unadjusted low-high range (BAC 2000-01-03 prints Close 13.952057 against Low 24.000000). **No adjustment rule is stated for Open, High or Low, and no split/dividend policy is given for the feature pipeline** - `data gap`.
- **Point-in-time:** `not stated in source`. There is no index-membership point-in-time rule, no reconstitution schedule, no delisting handling, and no disclosure of whether the top-20 selection date is fixed ex ante or chosen in-sample; the authors themselves name the resulting survivorship bias (Limitations).
- **Timestamp / timezone:** `not stated in source` - no session, timezone, calendar or out-of-order convention is given (Yahoo Finance daily bars are exchange-session based, but the paper never says so).
- **Missing data:** "We first check for missing data" is the only statement; no imputation, suspension or stale-price rule is printed (`underspecified`).
- **Benchmarks:** S&P 500 index series for alpha/beta (series identity, total-return vs price-return, data source all `not stated in source`).
- **Funding/fee/spread needs:** `not stated in source` - the paper models no fees, spreads, financing or slippage (census in Provenance).

## Execution assumptions

- **Signal-to-order timing / next-bar vs same-bar:** `not stated in source`. This is the single largest execution gap: the rule of Eq. 4 and the DRL actions have no stated fill price, and a daily rule evaluated against daily closes is as consistent with same-bar fills as with next-open fills.
- **Order type / fill model / partial fills / latency:** `not stated in source` (`order type`, `limit order`, `market order`, `fill`, `latency` all 0 occurrences).
- **Fees / spread / slippage / impact / capacity / participation / turnover:** **none modeled.** Sections 3-6 contain no cost, spread, fill, latency or impact treatment whatsoever (census in Provenance). **Do not read this as "costs are zero"; it is a costless backtest of daily long/cash switches on 20 mega-cap names.**
- **Leverage / margin / borrow:** the LSTM leveraged variant is defined (`lambda > 1`, value unstated) and Section 5.2 states that leverage "roughly doubles its annual return, maximum drawdown, alpha, and beta while leaving the Sharpe ratio unchanged" - an invariant that is only possible if **financing cost is zero**, i.e. leverage is modeled as free. Margin, borrow availability and shorting are never discussed; the DRL action space permits negative share counts but the paper never states whether the portfolio can be short (`underspecified`).
- **Position limits / sizing:** bounded only by the unstated `k`; no capital base, no notional constraint, no per-name cap.
- **Failure handling / rejected orders / delistings:** `not stated in source`.
- Whether these policies survive realistic execution frictions is **not addressed by the source** and is the central open question for any adoption decision.

## Evidence

### Source-reported

All figures below are source-reported from arXiv:2609.31870v1, are **backtest metrics on a costless simulation**, and have not been independently reproduced. Each is tied to its table/section.

**Table 1 - sample of the raw data (first row date 2000-01-03; caption as printed).**

| Date | Open | High | Low | Close | Volume | Ticker |
| --- | --- | --- | --- | --- | --- | --- |
| 2000-01-03 | 0.936384 | 1.004464 | 0.907924 | 0.859423 | 535,796,800 | AAPL |
| 2000-01-03 | 16.812500 | 16.875000 | 16.062500 | 16.274673 | 7,384,400 | ADBE |
| 2000-01-03 | 81.500000 | 89.562500 | 79.046875 | 89.375000 | 16,117,600 | AMZN |
| 2000-01-03 | 25.125000 | 25.125000 | 24.000000 | 13.952057 | 13,705,800 | BAC |
| 2000-01-03 | 36.500000 | 36.580002 | 34.820000 | 35.299999 | 875,000 | BRK-B |

Caption: "Close is the split- and dividend-adjusted closing price, which is why it can lie outside the unadjusted low-high range."

**Table 2 - sample of the processed dataset (caption: "first trading day; intermediate columns omitted").**

| Ticker | Day | macd | boll_ub | ... | cci_10 | dx_30 | close_120_sma | close_120_ema |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AAPL | 0 | 0 | 0.9256 | ... | -66.67 | 100 | 0.859 | 0.859 |
| ADBE | 0 | 0 | 0.9256 | ... | -66.67 | 100 | 16.274 | 16.274 |
| AMZN | 0 | 0 | 0.9256 | ... | -66.67 | 100 | 89.375 | 89.375 |
| BAC | 0 | 0 | 0.9256 | ... | -66.67 | 100 | 13.952 | 13.952 |
| BRK-B | 0 | 0 | 0.9256 | ... | -66.67 | 100 | 35.299 | 35.299 |

**Table 3 - training and validation metrics of the LSTM variants** (columns: Loss, MAE, MAPE, MSE x10^-6, MAE_val, MAPE_val, MSE_val x10^-6; caption: "Loss is each model's training objective, which is MAPE except for the MSE, Huber, and log-cosh models. Metrics are computed on scaled prices").

| Model | Loss | MAE | MAPE | MSE (x10^-6) | MAE val | MAPE val | MSE val (x10^-6) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Baseline | 1.052367 | 0.004578 | 1.052367 | 38 | 0.004099 | 0.972073 | 32 |
| Dropout | 2.371855 | 0.011330 | 2.371855 | 271 | 0.007442 | 1.535101 | 95 |
| MSE | 0.000336 | 0.006153 | 1.412530 | 336 | 0.004355 | 1.036787 | 38 |
| Huber | 0.000098 | 0.005407 | 1.253396 | 196 | 0.004077 | 0.974119 | 35 |
| Log-cosh | 0.000066 | 0.005286 | 1.226172 | 133 | 0.003798 | 0.898953 | 29 |
| MAPE | 0.935923 | 0.004015 | 0.935923 | 31 | 0.003789 | 0.888290 | 29 |
| Single ticker | 2.464035 | 0.010135 | 2.464035 | 172 | 0.010011 | 2.582896 | 145 |
| Fewer units | 0.995828 | 0.004298 | 0.995828 | 35 | 0.003565 | 0.856291 | 27 |
| More units | 1.074033 | 0.004663 | 1.074033 | 39 | 0.005058 | 1.143134 | 44 |

**Table 4 - backtest performance on the 2019-2020 test set; the benchmark is the S&P 500** ("Retrained denotes forward retraining (Section 4.2.3); other DRL rows are trained once").

| Model | Annual return | Cumulative return | Sharpe ratio | Max drawdown | Alpha | Beta |
| --- | --- | --- | --- | --- | --- | --- |
| LSTM | 16.99% | 36.85% | 1.19 | -9.57% | 0.09 | 0.31 |
| LSTM (leveraged) | 34.25% | 80.22% | 1.19 | -19.14% | 0.20 | 0.61 |
| A2C | 20.47% | 45.23% | 0.82 | -31.11% | -0.03 | 1.02 |
| A2C (retrained) | 29.83% | 68.73% | 0.99 | -33.52% | 0.03 | 1.14 |
| PPO | 27.89% | 63.71% | 1.09 | -25.33% | 0.05 | 0.91 |
| PPO (retrained) | 32.16% | 74.84% | 1.30 | -22.84% | 0.10 | 0.84 |
| DDPG | 55.51% | 142.26% | 1.38 | -33.52% | 0.22 | 1.24 |
| DDPG (retrained) | 29.82% | 68.72% | 1.09 | -33.52% | 0.04 | 1.02 |
| TD3 | 42.00% | 101.93% | 1.37 | -25.24% | 0.18 | 0.89 |
| TD3 (retrained) | 41.89% | 101.61% | 1.27 | -28.68% | 0.13 | 1.11 |
| SAC | 38.95% | 93.32% | 1.33 | -24.19% | 0.15 | 0.90 |
| SAC (retrained) | 40.44% | 97.51% | 1.28 | -23.20% | 0.19 | 0.83 |

**Prose-level claims (Sections 1, 4.1, 5.1, 5.2, 6) - all verified against the printed tables unless noted:**

1. Abstract/Section 5.2: "DDPG achieves the highest annual return (55.5%), Sharpe ratio (1.38), and alpha (0.22), but also the highest market beta (1.24)" - matches Table 4 (55.51%).
2. Abstract: "Forward retraining improves A2C, PPO, and SAC, leaves TD3 essentially unchanged, and reduces DDPG's annual return from 55.5% to 29.8%" - matches Table 4 (55.51% -> 29.82%).
3. Section 5.2: "Forward retraining improves the annual return of A2C (20.47% -> 29.83%), PPO (27.89% -> 32.16%), and SAC (38.95% -> 40.44%), and leaves TD3 essentially unchanged (42.00% vs. 41.89%)" - all six values match Table 4.
4. Section 5.2: "The resulting alpha of 0.20 is second only to DDPG (0.22), and the beta of 0.61 remains well below that of every DRL agent (0.83-1.24)" - matches Table 4 (DRL beta range 0.83 to 1.24).
5. Section 5.2: "The unleveraged LSTM strategy has the lowest annual return (16.99%), but its Sharpe ratio of 1.19 lies in the middle of the range, and it has the smallest maximum drawdown (-9.57%) and the lowest beta (0.31) of all strategies" - matches Table 4.
6. Section 5.2: "Leverage roughly doubles its annual return, maximum drawdown, alpha, and beta while leaving the Sharpe ratio unchanged" - matches Table 4 (see research-computed diagnostics).
7. Section 4.1.1 / Conclusion: MAPE "gives the lowest validation error among the losses we compare" / "MAPE to be the most effective loss among those compared" - supported **within the loss comparison only**: among the MAPE-, MSE-, Huber- and log-cosh-trained rows the MAPE row has the lowest MAPE_val (0.888290 vs 1.036787, 0.974119, 0.898953); the overall lowest MAPE_val in Table 3 belongs to the `Fewer units` row (0.856291), which is an architecture variant, not a loss.
8. Section 5.1 metric definitions: "The Sharpe ratio measures return per unit of volatility" (no risk-free rate is mentioned anywhere), "maximum drawdown is the largest peak-to-trough decline in portfolio value", "alpha and beta are the intercept and slope of a regression of strategy returns on benchmark returns."
9. Figure 1 caption: "(a) An LSTM forecasts prices and a rule-based strategy turns the forecasts into positions. (b) A DRL agent interacts with a trading environment and learns trading actions end to end. Both are trained on 2000-2018 and backtested on 2019-2020."

**Research-computed consistency checks on the printed values (arithmetic only - these do not constitute an independent reproduction of the backtest):**

- Row count identity: 20 stocks x 5,284 trading days = 105,680, matching the stated dataset size.
- Annual-vs-cumulative identity over a two-year window: `(1 + cumulative)^(1/2) - 1` reproduces the printed annual return to within **0.137 percentage points** in every row (largest gap: DDPG, implied 55.647% vs printed 55.51%; LSTM implied 16.983% vs printed 16.99%). The annualisation convention itself is never stated, so this is consistency, not verification.
- Leverage identity: `34.25 / 16.99 = 2.016`, `19.14 / 9.57 = 2.000`, `0.61 / 0.31 = 1.968`, `0.20 / 0.09 = 2.22` (alpha at two-decimal rounding), Sharpe `1.19 = 1.19` - i.e. the leveraged LSTM row is consistent with `lambda = 2` **and with zero financing cost**, although the source never prints `lambda`.
- Three separate rows print an identical maximum drawdown of `-33.52%` (A2C retrained, DDPG, DDPG retrained); the source offers no explanation. Recorded as an unexplained printed coincidence, not a contradiction.
- Forecast-vs-DRL Sharpe: the LSTM baseline's `1.19` exceeds 4 of the 10 DRL rows - A2C (0.82), A2C retrained (0.99), PPO (1.09) and DDPG retrained (1.09).
- Forward-retraining deltas: A2C +45.7% relative, PPO +15.3%, SAC +3.8%, TD3 -0.26%, DDPG **-46.3%** (55.51 -> 29.82).
- DRL betas all lie in `[0.83, 1.24]`; A2C trained once has **negative alpha (-0.03)** against the S&P 500.
- Table 3 column minima (substituting for unrecoverable bold): training columns are minimised by the `MAPE` row (MAE 0.004015, MAPE 0.935923, MSE 31); validation columns are minimised by the `Fewer units` row (MAE_val 0.003565, MAPE_val 0.856291, MSE_val 27).

### Independently reproduced

not independently reproduced

(The checks above are arithmetic identities over the source's own printed numbers; no dataset, model or backtest was re-executed, and no code from this paper exists to run.)

### Negative evidence

1. **Zero cost modeling:** the Methods and Results sections contain no transaction-cost, spread, slippage, fill, latency, participation, turnover, capacity, leverage-cost or market-impact treatment (census in Provenance) - a data gap, never a zero. Every printed return and Sharpe is therefore implicitly gross of unspecified frictions, and the paper does not even label them gross.
2. **Free leverage:** Section 5.2's own claim that leverage doubles return and drawdown "while leaving the Sharpe ratio unchanged" proves no financing cost is charged; with `lambda` unstated, the leveraged row is not reconstructible either.
3. **No statistical inference at all:** `p-value` 0, `t-stat` 0, `confidence interval` 0, `bootstrap` 0; `significan` occurs once, as prose about TD3. The authors state outright: "DRL performance is known to be sensitive to random seeds and hyperparameters, and we do not report variability across runs."
4. **No seeds reported:** the word `seeds` appears only in the Limitations and future-work sentence; every Table 4 row is a single run of a stochastic algorithm.
5. **Survivorship bias, author-acknowledged:** "Our stock universe consists of large companies with complete 2000-2020 histories, which introduces survivorship bias", compounded by "companies that went public after 2000 are excluded" and by the selection date for "largest market capitalization" being unstated.
6. **Two-year test window, author-acknowledged:** "The test period covers only two years (2019-2020), which include both a strong bull market and the COVID-19 crash of early 2020, so the results may not generalize to other market regimes"; `holdout` 0, no regime breakdown, no test after 2020 despite the 2026 posting.
7. **The headline ranking refutes itself under the paper's own protocol:** DDPG's 55.51% annual return falls to 29.82% (-46.3% relative) once forward retraining is applied, i.e. the once-trained "best" configuration is presented alongside evidence that it does not survive walk-forward evaluation.
8. **Returns are largely beta:** all DRL betas in [0.83, 1.24]; alpha is 0.03-0.22 for 9 of 10 DRL rows and -0.03 for A2C trained once, measured against an index whose own return is never printed, so excess performance cannot be recomputed from the paper.
9. **DRL rows are not reproducible from the paper:** no hyperparameters (`k`, network sizes, learning rates, discount, exploration, replay, tuning data set), no code for this paper (`source code` 0, `repository`/`github` hits only inside the cited Stable-Baselines3 reference [18]), and no slice boundaries for forward retraining. Section 5.2's "individually tuned, once-trained DDPG" never says which data the tuning used, leaving open the possibility of test-set tuning.
10. **Trivial baselines absent:** `naive` 0, `persistence` 0, `climatolog` 0; Table 4 has no unconditional always-long basket row and never prints the index's own return. The nearest thing to a control is the LSTM rule itself, which Section 4.1.3 calls "a simple modified buy-and-hold strategy" - but that is a conditional long-or-cash rule, not a static benchmark - so the paper never shows that any policy beats holding its own 20 names, the cheapest possible control for a long/cash strategy in a 2019-2020 bull-plus-crash window.
11. **Execution timing unstated:** no fill price, order type, latency or next-bar rule anywhere (`execution`, `fill`, `latency`, `order type` all 0), so same-bar look-ahead cannot be excluded from the printed numbers.
12. **Feature-scaling look-ahead risk:** Eq. 1 does not state the min/max window; if it spans 2000-2020 the log min-max transform imports test-window extrema into the training state.
13. **Mixed adjustment basis in the raw record:** Table 1's caption confirms Close is split- and dividend-adjusted while the low-high range is unadjusted (BAC Close 13.952057 below Low 24.000000); no adjustment policy is given for Open/High/Low or for the derived features.
14. **Warm-up rows with no stated handling:** on day 1 all indicator windows contain one observation (`macd` 0, `boll_ub` 0.9256, `cci_10` -66.67, `dx_30` 100 identical across sample tickers; `close_120_sma = close_120_ema = close`), and the paper says nothing about discarding or seeding these rows.
15. **Metric definitions sourced from Investopedia:** references [21]-[23] are Investopedia pages for cumulative return, Sharpe ratio and maximum drawdown, and the LSTM design is traced to a Kaggle notebook plus the TensorFlow time-series tutorial - a source-quality signal for the evaluation methodology.
16. **Sharpe and annualisation conventions unstated:** no risk-free rate, no return frequency, no annualisation factor, no regression frequency; "return per unit of volatility" is not a complete definition.
17. **Unexplained printed coincidence:** three rows share MDD -33.52%.
18. **No multiplicity control over the algorithm comparison:** 12 Table 4 configurations (5 algorithms x 2 training regimes plus 2 LSTM rows) are compared and a winner is declared with `benjamini`/`bonferroni`/`holm`/`fdr`/`multiple test` all 0 and no seed replication.
19. **No capacity, liquidity or turnover analysis** (`turnover` 0, `capacity` 0, `participation` 0) despite an all-in share-count action space on 20 names.
20. **No point-in-time membership or rebalance disclosure**; the index used for alpha/beta is not identified (price vs total return).
21. **Provenance gap between manuscript and posting:** page-1 dateline `June 8, 2021` against arXiv v1 `2026-09-25` - a ~5-year gap during which the hypotheses were presumably visible to the authors, with no registered version history before v1.
22. **Publication status:** preprint only - no Comments, no Journal-reference, no peer-review statement (`peer` 0), arXiv-issued DataCite DOI pending registration, non-exclusive-distribution licence rather than a reuse licence.
23. **Zero crypto content** (`crypto`, `bitcoin`, `perpetual` all 0) and no derivative, funding or shorting mechanics, so nothing here is crypto evidence.
24. **No independent replication or contrary published study on this preprint was found in this run; absence is not evidence of no negative result.**

## Falsification plan

Every threshold below is **research-defined** (a Scout-chosen acceptance/failure cutoff) unless explicitly quoted from the source. Each gate names a fail condition and an action.

**No-retuning rule:** the 20-name 2000-2020 universe definition, the 14-column state, log min-max scaling (Eq. 1), the two-layer-plus-dense LSTM with MAPE loss, the Eq. 4 rule including `lambda`, the integer action space `{-k..k}`, the Eq. 5 costless reward, the five algorithms, the expanding-window forward-retraining protocol, the train 2000-2018 / test 2019-2020 split, the S&P 500 benchmark and the Table 4 metric set are **frozen**. Any change to these requires a new record; results from a changed configuration may not be used to rescue a failed gate.

- **F1 - printed-value reproduction.** Fail condition: any numeric cell of Tables 1-4 re-extracted from the pinned PDF differs from this record. **Action:** halt, mark the record unreliable, correct or withdraw it before any further use.
- **F2 - prose-versus-table claim integrity.** Fail condition: a Section 5.1/5.2/6 numerical claim does not hold in Table 4. **Status: currently passing** (all nine prose claims checked above, with claim 7 recorded as holding only within the loss comparison). **Action:** treat table cells as truth and any failing sentence as partially unreliable.
- **F3 - hyperparameter and protocol disclosure gate.** Fail condition: the source (or released code) does not supply `k`, network sizes, optimiser settings, exploration/replay configuration, the tuning data set, `lambda`, and the forward-retraining slice boundaries. **Status: currently FAILING as printed** (no hyperparameter table, no code). **Action:** treat every DRL row as non-reproducible; no adoption decision may rest on a DRL row until this gate passes.
- **F4 - cost-ladder net gate (research-defined, the core economic test).** Fail condition: attaching a research-defined per-side cost ladder of {0, 1, 2, 5, 10, 25} basis points (commission + spread + slippage combined) and a research-defined signal-to-fill delay of {0, 1, 2} trading days leaves the best DRL row's net Sharpe at or below the LSTM rule's net Sharpe, or any net Sharpe <= 0.25 at 5 bps per side. **Action:** record remains `research-only` permanently; no implementation candidate may be advanced on costless numbers.
- **F5 - always-long and index gate (research-defined).** Fail condition: under the same cost ladder, the best policy's net alpha against an equal-weight buy-and-hold basket of the same 20 names, and against the S&P 500 total-return series over 2019-2020, is <= 0. **Action:** reject H1 ("end-to-end RL adds value") and keep only the protocol claim H2.
- **F6 - forward-retraining stability gate (research-defined).** Fail condition: any model's annual return moves by more than 25% relative between once-trained and retrained evaluation. **Status: currently FAILING for DDPG (-46.3%).** **Action:** once-trained rows may not be quoted as evidence; only retrained rows are usable, and the paper's "DDPG attains the highest annual return" framing must be reported as protocol-dependent.
- **F7 - seed-stability gate (research-defined).** Fail condition: over 10 seeds per algorithm, the sign of (DRL minus LSTM) annual return flips in more than 30% of seeds, or the cross-seed standard deviation of Sharpe exceeds 0.30. **Action:** withdraw all algorithm-ranking statements; retain only point estimates with explicit single-run caveats.
- **F8 - survivorship / point-in-time universe gate.** Fail condition: rebuilding the universe as point-in-time top-20 S&P 500 members by market capitalisation, with delistings, IPO dates and reconstitutions, drops the best policy's net alpha vs index to <= 0, or flips the LSTM-vs-DRL Sharpe ordering. **Action:** record the 2019-2020 result as a survivorship artefact and stay `research-only`.
- **F9 - execution-timing gate (research-defined).** Fail condition: re-running with next-open fills (the source states no execution timing) drops the best policy's Sharpe by >= 0.30 or drives its alpha <= 0. **Action:** withdraw all return claims; keep only the qualitative protocol observation.
- **F10 - data-consistency gate.** Fail condition: a single documented adjustment basis for OHLC, an explicit warm-up/discard rule for the first 120 days, and a stated day-of-week encoding cannot be established, or headline metrics move by > 10% relative once they are. **Action:** treat the printed tables as non-reconstructible and block any replication claim.
- **F11 - feature-scaling look-ahead gate.** Fail condition: the min/max of Eq. 1 are computed over any window that includes test-period data (currently unstated, so the gate is **open**), or recomputing with training-only extrema moves any headline metric by > 10% relative. **Action:** reject the affected row and re-run; no post hoc re-selection of variants.
- **F12 - multiplicity gate (research-defined).** Fail condition: any "best algorithm" claim fails Benjamini-Hochberg at q < 0.10 over the 12 Table 4 configurations (and their seed replicates), or a deflated-Sharpe check with trial count >= 12 removes the winner. **Status: open** - the source performs no test at all. **Action:** withdraw ranking language; retain effect sizes only.
- **F13 - out-of-window regime gate (frozen).** Fail condition: extending the frozen configuration over 2021-2025 yields net alpha vs index <= 0 in at least 2 of 5 years, or the LSTM rule beats every DRL row in at least 3 of 5 years. **Action:** treat the 2019-2020 table as a single-regime artefact.
- **F14 - data-availability gate.** Fail condition: Yahoo Finance daily OHLCV with a documented adjustment policy plus point-in-time S&P 500 membership cannot be obtained with the required provenance. **Action:** the record stays `research-only` permanently; no replication claim and no adoption may proceed.

Action on failure for every gate: retain the record as research-only, record the failure in this record's negative evidence, and do not retune the frozen configuration post hoc.

## Crypto portability

**adapted** - the source demonstrates its mechanism only in US listed cash equities and contains zero occurrences of `crypto`, `bitcoin` or `perpetual`, so any crypto version is a ported hypothesis, not crypto empirical evidence.

- **What ports:** the *protocol* claim is instrument-agnostic - an expanding-window walk-forward retraining evaluation that can flip algorithm rankings, evaluated against an always-long basket and a cost ladder. The state/action recipe (price/volume indicators -> integer position changes -> portfolio-value reward) transfers mechanically to perpetual futures or spot.
- **What does not port unchanged:** the economic setting (US mega-cap equities with a 2019-2020 index benchmark, exchange sessions, dividend/split adjustments) has no direct crypto counterpart; day-of-week and session features assume exchange calendars; the Eq. 1 scaling and 120-day warm-up assume long continuous histories that many tokens lack.
- **Crypto-specific risks:** 24/7 sessions and candle-boundary differences; venue fragmentation and per-venue OHLCV divergence; funding as path-dependent carry during holding windows (funding is `not stated in source` and unmodeled); mark/index vs last-price divergence; maker/taker fee tiers, liquidation mechanics and partial fills (all absent from the source's cost model); survivorship and delisting in the underlying token set, which is far more severe than for S&P 500 constituents.
- No crypto backtest of this mechanism exists in our stack; portability remains unproven. It is not authorization to trade.

## Limitations

- **Source status:** arXiv preprint v1 (submitted 2026-09-25, manuscript dateline 2021-06-08), 8 pages / 1 figure / 4 tables / 23 references, not peer-reviewed, no Comments, no journal reference, no code or data-availability statement, non-exclusive-distribution licence.
- **No trading layer details:** entry timing, execution price, order type, fill model, `k`, `lambda`, capital base, holding-period cap and all costs are `not stated in source`; the reward contains no cost term.
- **`data gap`:** ticker list and selection date, index series identity, adjustment policy for Open/High/Low, Eq. 1 min/max window, Sharpe/annualisation/regression conventions, DRL hyperparameters, forward-retraining slice boundaries, missing-data rule, timezone/session convention.
- **`underspecified`:** warm-up row handling, day-of-week encoding, the LSTM unit counts behind `Fewer units`/`More units`, whether the DRL portfolio may take a short book, whether tuning used test data.
- **No contradictions found:** every Section 5/6 numerical claim reconciles with Table 4 and Tables 1-2 agree to rounding on the sampled tickers, so `contested: false`; three rows nonetheless share an identical printed MDD of -33.52%, unexplained by the source.
- **Evidence is single-run, costless, survivorship-selected and two years long**, on a window containing both a bull run and the COVID crash (author-acknowledged), with no seed variability, no significance testing and no holdout.
- **No trivial benchmark of any kind** (always-long basket, index return, persistence) - the cheapest controls for a long/cash rule are missing.
- **Not independently reproduced;** every performance figure above is third-party source-reported and gross of unstated frictions.
- **Crypto porting is `adapted`, not `direct`.**

## Implementation status

`not-implemented`. No implementation, backtest, prototype, paper trading or validation exists in our research stack. Nothing in Qlib, Paper, Testnet or Live has been touched by this record. The source ships no code of its own - its only repository references are to the cited Stable-Baselines3 library (reference [18]) - so there was nothing from this paper to run.

## Adoption boundary

This record is research material only. Its presence in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading.

## Related Wiki records

- Read-only Wiki Brain resolution on 2026-09-30: `quant/strategy-research-record-spec-v2.md` returned **file not found**, so this run failed closed onto `quant/strategy-research-record-spec-v1.md` (canonical, 10,289 bytes, SHA-256 `4561578a2a991aaa8252b31a8b6fd0a46b98c853ef77599521436ee6ff2fcaa7`).
- Four read-only `kb_search` queries were run: `deep reinforcement learning equity trading actor-critic backtest` (5 pages), `walk-forward retraining robustness backtest survivorship bias` (1 page), `LSTM stock price forecasting technical indicator trading rule` (0 pages), `S&P 500 survivorship bias point-in-time universe backtest costs` (8 pages), plus `actor-critic forward retraining expanding window S&P 500 20 stocks` (0 pages). A vault-wide grep for `2609.31870` returned **no Wiki page for this source**; the only vault hit for the phrase `forward retraining` is the archetype-trader record's "walk-forward retraining" sentence. **Zero pages were written.**
- Verified adjacent Wiki pages (exist on disk; linked with their mechanism difference stated):
  - [[quant/sentiment-augmented-drl-alpha-reward-ddpg-active-trading-2026-09-05]] - a single DDPG-style active-trading policy with a sentiment-augmented excess-alpha reward; different source, single-algorithm design, sentiment data dependency, and no walk-forward retraining protocol.
  - [[quant/crypto-rl-pair-trading-dynamic-scaling-a2c-2026-09-12]] - A2C applied to high-frequency crypto pairs with empirical "algorithmic fragility" findings; same algorithm family, but a different market (crypto pairs), horizon and mechanism, and it does study robustness rather than headline returns.
  - [[quant/alphazerobeta-recurrent-ppo-market-neutral-portfolio-2026-09-02]] - PPO with multi-objective reward shaping and a dollar-neutral projection, with a transaction-cost layer; different source, market-neutral long-short mechanism, and cost modeling that this source lacks.
  - [[quant/sp500-statistical-arbitrage-johansen-ou-ablation-multiple-testing-2026-09-12]] - S&P 500 universe adjacency only; cross-sectional cointegration/OU arbitrage with family-wise multiple-testing deflation, a control this source has none of.
- Repository-adjacent records (same checkout, different source identities and materially distinct mechanisms):
  - `global-equity-sac-hierarchical-dirichlet-adaptive-retraining-2026-09-04` - arXiv:2605.17307. **Five-axis distinction:** (1) *source identity* different; (2) *mechanism* different - a single SAC agent with a hierarchical Dirichlet allocation policy and adaptive retraining as the proposed strategy, versus a five-algorithm benchmark whose contribution is the forward-retraining evaluation protocol; (3) *signal construction* different - continuous portfolio weights over a multi-asset universe versus integer share-count actions over 14 technical indicators plus an Eq. 4 price-forecast rule; (4) *universe* different - global multi-asset equities versus 20 US mega-caps; (5) *data dependency* different - allocation data set versus Yahoo Finance OHLCV plus indicators. Materially distinct on all five axes.
  - `alphazerobeta-recurrent-ppo-market-neutral-portfolio-2026-09-02` - arXiv:2607.18001 (Springer Financial Innovation accepted): dollar-neutral, multi-objective, cost-modeled; different source, mechanism, universe type (market-neutral long-short) and data dependency.
  - `archetype-trader-vq-rl-hierarchical-crypto-perpetual-2026-09-13` - AAAI 2026, DOI 10.1609/aaai.v40i34.40166; vector-quantised archetype policies on crypto perpetuals. Matched only on the phrase "walk-forward retraining" in a falsification section; different source, market and mechanism.
  - `pure-momentum-wild-bootstrap-drift-significance-filter-us-equities-2026-09-26` - Amundi Working Paper 188 (three authors, one of them Xinyi Zhang); matched only on the shared author name `Xinyi Zhang`. Different source identity, an explicit tradable momentum signal with wild-bootstrap inference, and none of this paper's RL machinery.
  - `ai-crypto-trading-backtest-paper-live-gap-three-stage-benchmark-arxiv-2609.34510-2026-09-29` - a three-stage benchmark of the backtest-to-live gap in crypto; different asset class and a benchmark-design mechanism rather than an algorithm comparison.
  - None of these shares this source identity, and none benchmarks five actor-critic algorithms plus an LSTM forecast-then-trade rule under an expanding-window forward-retraining protocol on 20 S&P 500 mega-caps.

## Sources

1. Wang, B., & Zhang, X. (2026). "Deep Reinforcement Learning for Equity Trading: Benchmarking Actor-Critic Methods with Forward Retraining." arXiv:2609.31870v1 [cs.LG], submitted 25 September 2026; manuscript dateline 8 June 2021. Abstract: `https://arxiv.org/abs/2609.31870`; PDF (pinned, 165,275 bytes, SHA-256 `97a2f345d9158f5cdc10e5f0739ab5d8027a02777c2cbd302d33adb5b4b229dc`): `https://arxiv.org/pdf/2609.31870`; DOI: `https://doi.org/10.48550/arXiv.2609.31870`. All quantitative claims above trace to Tables 1-4, Figure 1, Sections 1-6 and the Author Contributions/Acknowledgments of that preprint; all are labelled source-reported.
2. arXiv API record used only for version/date/publication-status verification: `https://export.arxiv.org/api/query?id_list=2609.31870` (3,024 bytes, SHA-256 `326204bdc22bc5b81480db738cd6fdff51b36a89eafbc0ba17473d77f5fbaadb`).
3. Data and benchmark named by the primary paper (used by it, not directly by us): the Yahoo Finance API for daily OHLCV (no URL stated in the source) and the S&P 500 index as the Table 4 benchmark (series identity not stated in the source).
4. Cited implementation dependency of the primary paper (reference [18], not this paper's code): Stable-Baselines3, `https://github.com/DLR-RM/stable-baselines3`, on which "Our DDPG implementation builds".
